#!/usr/bin/env python3
"""
Hexo 构建产物一键部署脚本

默认流程:
  1. 在本地执行 `hexo generate` 生成 public/
  2. 用 rsync 把 public/ 同步到远程服务器的目标目录
  3. 调起 refresh_cdn.py 刷新腾讯云 CDN 缓存

输出原则（默认安静模式）:
  - 只打印每个阶段做了什么、结果对不对
  - 失败时打印错误末尾
  - 不打印 hexo 构建过程、不打印 rsync 文件级进度

环境变量:
  TENCENT_SERVER_HOST    必填，服务器 host (IP 或域名)
  TENCENT_SERVER_USER    可选，默认 root
  TENCENT_SERVER_PORT    可选，默认 22
  TENCENT_SSH_KEY        可选，默认 ~/.ssh/id_rsa
  REMOTE_DIR             可选，默认 /opt/website/opc-website/python4office.cn
  LOCAL_PUBLIC_DIR       可选，默认 <repo>/hexo/hexo/public
  SKIP_BUILD=true        跳过构建，使用现有 public/
  SKIP_CDN_REFRESH=true  跳过部署后的 CDN 刷新
  SKIP_INDEXNOW=true     跳过部署后的 IndexNow 提交
  DRY_RUN=true           只打印 rsync 命令不实际执行
  DEPLOY_VERBOSE=true    显示每个子进程的完整命令（调试用）
  HEXO_DIR               可选，默认 <repo>/hexo/hexo
"""

from __future__ import annotations

import contextlib
import os
import shlex
import shutil
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

# ---------- 配置 ----------
SCRIPT_DIR = Path(__file__).resolve().parent
# scripts/deploy/deploy.py -> 项目根
REPO_ROOT = SCRIPT_DIR.parent.parent

DEFAULT_HEXO_DIR = REPO_ROOT / "hexo" / "hexo"
DEFAULT_PUBLIC_DIR = DEFAULT_HEXO_DIR / "public"
DEFAULT_REMOTE_DIR = "/opt/website/opc-website/python4office.cn"
DEFAULT_SSH_KEY = Path.home() / ".ssh" / "id_rsa"

# 已经是压缩格式的文件类型，rsync 传输时不再二次压缩
SKIP_COMPRESS_EXTS = ",".join([
    "jpg", "jpeg", "png", "gif", "webp", "svg", "ico",
    "zip", "gz", "tgz", "bz2", "7z", "rar",
    "mp4", "mov", "webm", "mkv", "avi",
    "mp3", "ogg", "flac",
    "woff", "woff2", "ttf", "otf", "eot",
    "pdf",
])

# 调试模式：显示子进程完整命令
VERBOSE = os.environ.get("DEPLOY_VERBOSE", "").lower() in ("1", "true", "yes")

# ---------- 日志 ----------
USE_COLOR = sys.stdout.isatty()
RESET = "\033[0m" if USE_COLOR else ""
RED = "\033[0;31m" if USE_COLOR else ""
GREEN = "\033[0;32m" if USE_COLOR else ""
YELLOW = "\033[1;33m" if USE_COLOR else ""
BLUE = "\033[0;34m" if USE_COLOR else ""
BOLD = "\033[1m" if USE_COLOR else ""

# 脚本启动时间（用于统计总耗时）
SCRIPT_START = time.monotonic()


def _ts() -> str:
    return datetime.now().strftime("%H:%M:%S")


def _elapsed() -> str:
    """脚本启动至今耗时，例如 '12.3s'。"""
    return f"{time.monotonic() - SCRIPT_START:.1f}s"


def log(msg: str) -> None:
    """普通信息，写到 stdout。"""
    print(f"{BLUE}[{_ts()}]{RESET} {msg}")


def ok(msg: str) -> None:
    """成功标记，写到 stdout。"""
    print(f"{GREEN}✓{RESET} {msg}")


def warn(msg: str) -> None:
    """警告（不致命），写到 stderr。"""
    print(f"{YELLOW}⚠{RESET} {msg}", file=sys.stderr)


def err(msg: str) -> None:
    """错误，写到 stderr。"""
    print(f"{RED}✗{RESET} {msg}", file=sys.stderr)


def title(text: str) -> None:
    """脚本级别的总标题。"""
    print()
    print(f"{BOLD}========== {text} =========={RESET}")


def footer(text: str) -> None:
    """脚本级别的总结尾，附带总耗时。"""
    print()
    print(f"{BOLD}========== {text} (总耗时 {_elapsed()}) =========={RESET}")


def header(text: str) -> None:
    """阶段标题。"""
    print(f"{BOLD}── {text} ──{RESET}")


@contextlib.contextmanager
def step(name: str):
    """阶段上下文管理器。失败时不打印"完成"消息。"""
    log(f"开始 {name}...")
    start = time.monotonic()
    failed = False
    try:
        yield
    except BaseException:
        failed = True
        raise
    finally:
        elapsed = time.monotonic() - start
        if not failed:
            ok(f"{name} 完成 ({elapsed:.1f}s)")


def die(msg: str, code: int = 1) -> None:
    err(msg)
    sys.exit(code)


# ---------- 校验 ----------
def require_tools() -> None:
    for tool in ("rsync", "ssh"):
        if shutil.which(tool) is None:
            die(f"未找到 {tool}，请先安装 (brew install {tool})")


def load_config() -> dict:
    host = os.environ.get("TENCENT_SERVER_HOST", "").strip()
    if not host:
        die(
            "缺少环境变量 TENCENT_SERVER_HOST\n"
            "  方式 1: export TENCENT_SERVER_HOST=1.2.3.4\n"
            "  方式 2: 在项目根目录建 .env 文件写入 TENCENT_SERVER_HOST=1.2.3.4"
        )

    cfg = {
        "host": host,
        "user": os.environ.get("TENCENT_SERVER_USER", "root").strip() or "root",
        "port": int(os.environ.get("TENCENT_SERVER_PORT", "22") or "22"),
        "ssh_key": Path(os.environ.get("TENCENT_SSH_KEY", str(DEFAULT_SSH_KEY))).expanduser(),
        "remote_dir": os.environ.get("REMOTE_DIR", DEFAULT_REMOTE_DIR).strip() or DEFAULT_REMOTE_DIR,
        "hexo_dir": Path(os.environ.get("HEXO_DIR", str(DEFAULT_HEXO_DIR))).expanduser().resolve(),
        "public_dir": Path(
            os.environ.get("LOCAL_PUBLIC_DIR", str(DEFAULT_PUBLIC_DIR))
        ).expanduser()
        .resolve(),
        "skip_build": os.environ.get("SKIP_BUILD", "").lower() in ("1", "true", "yes"),
        "skip_cdn_refresh": os.environ.get("SKIP_CDN_REFRESH", "").lower() in ("1", "true", "yes"),
        "skip_indexnow": os.environ.get("SKIP_INDEXNOW", "").lower() in ("1", "true", "yes"),
        "dry_run": os.environ.get("DRY_RUN", "").lower() in ("1", "true", "yes"),
    }

    if not cfg["ssh_key"].exists():
        die(f"SSH 私钥不存在: {cfg['ssh_key']}")

    return cfg


# ---------- 辅助 ----------
def _stat_public(path: Path) -> tuple[int, str]:
    """单次遍历统计文件数和总大小，返回 (count, human_size)。"""
    count = 0
    total = 0
    for p in path.rglob("*"):
        if p.is_file():
            count += 1
            total += p.stat().st_size
    for unit in ("B", "K", "M", "G"):
        if total < 1024:
            return count, f"{total:.1f}{unit}"
        total /= 1024
    return count, f"{total:.1f}T"


# ---------- 步骤 ----------
def _run_hexo_generate(cfg: dict) -> None:
    if not (cfg["hexo_dir"] / "node_modules").exists():
        die(f"hexo 未安装依赖: {cfg['hexo_dir']}（先执行 cd hexo/hexo && yarn install）")
    cmd_list = [
        "node",
        "--max-old-space-size=8192",
        str(cfg["hexo_dir"] / "node_modules" / "hexo" / "bin" / "hexo"),
        "generate",
        "--draft",
    ]
    run(cmd_list, cwd=cfg["hexo_dir"], label="hexo generate")


def step_build(cfg: dict) -> None:
    if cfg["skip_build"]:
        log("SKIP_BUILD=true，跳过本地构建")
        return

    _run_hexo_generate(cfg)

    if not cfg["public_dir"].is_dir():
        die(f"public 目录不存在: {cfg['public_dir']}")

    file_count, size = _stat_public(cfg["public_dir"])
    log(f"public 就绪: {file_count} 个文件，{size}")


def step_sync(cfg: dict) -> None:
    rsync_cmd = [
        "rsync",
        "-az",
        "--delete",
        f"--skip-compress={SKIP_COMPRESS_EXTS}",
        "--exclude=.git",
        "--exclude=.DS_Store",
        "-e",
        f"ssh -i {shlex.quote(str(cfg['ssh_key']))} -p {cfg['port']} -o StrictHostKeyChecking=accept-new",
        f"{cfg['public_dir']}/",
        f"{cfg['user']}@{cfg['host']}:{cfg['remote_dir']}/",
    ]

    if cfg["dry_run"]:
        log("[DRY_RUN] 跳过实际同步")
        log("将执行: " + " ".join(shlex.quote(c) for c in rsync_cmd))
        return

    run(rsync_cmd, label="rsync 同步")


def step_refresh_cdn(cfg: dict) -> None:
    """部署成功后调用 refresh_cdn.py 刷新腾讯云 CDN 缓存。

    CDN 刷新失败不影响整体部署（仅 warn）；失败时打印 stdout/stderr 便于排查。
    失败也返回 OK 让流程继续，但输出"需手动重试"提示，避免用户认为已生效。
    """
    if cfg.get("skip_cdn_refresh"):
        log("SKIP_CDN_REFRESH=true，跳过 CDN 刷新")
        return

    refresh_script = SCRIPT_DIR.parent / "cdn" / "purge_static_assets.py"
    if not refresh_script.is_file():
        warn(f"未找到 CDN 刷新脚本: {refresh_script}，跳过")
        return

    cmd_list = [sys.executable, str(refresh_script)]
    if VERBOSE:
        log("执行: " + " ".join(shlex.quote(c) for c in cmd_list))

    result = subprocess.run(
        cmd_list,
        stdout=subprocess.PIPE,  # 改为 PIPE，失败时能看到输出
        stderr=subprocess.STDOUT,
        text=True,
    )
    if result.returncode == 0:
        ok("CDN 缓存已刷新")
    else:
        warn(f"CDN 刷新失败 (exit {result.returncode})")
        # 全部打印 stdout+stderr（限制 30 行避免刷屏）
        out = (result.stdout or "").strip().splitlines()[-30:]
        for line in out:
            err(f"  {line}")
        warn("CDN 刷新失败，但部署已完成")
        warn("⚠  重要：CDN 仍会返回旧缓存，请手动重试：")
        warn("   python3 scripts/cdn/purge_static_assets.py")
        warn("（或 SKIP_CDN_REFRESH=true 跳过此步骤）")


def step_indexnow(cfg: dict) -> None:
    """部署成功后调用 IndexNow 通知 Bing/Yandex 收录新页面。

    失败不影响整体部署（仅 warn）。
    """
    if cfg.get("skip_indexnow"):
        log("SKIP_INDEXNOW=true，跳过 IndexNow 提交")
        return

    submit_script = REPO_ROOT / "scripts" / "indexnow-submit.js"
    if not submit_script.is_file():
        warn(f"未找到 IndexNow 提交脚本: {submit_script}，跳过")
        return

    # node 命令必须在 PATH 上（macOS 自带 /usr/bin/node，但 brew 安装可能在 /opt/homebrew）
    node_bin = shutil.which("node")
    if not node_bin:
        warn("未找到 node，跳过 IndexNow 提交（需先安装 Node.js）")
        return

    # 默认只提交最近 7 天更新的 URL，避免全量推送
    cmd_list = [node_bin, str(submit_script), "--recent", "7"]
    if VERBOSE:
        log("执行: " + " ".join(shlex.quote(c) for c in cmd_list))

    result = subprocess.run(
        cmd_list,
        cwd=str(REPO_ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        timeout=60,
    )
    if result.returncode == 0:
        ok("IndexNow 提交成功")
        # 打印最后一行关键信息（状态码）
        last = (result.stdout or "").strip().splitlines()[-1] if result.stdout else ""
        if last:
            log(f"  {last}")
    else:
        warn(f"IndexNow 提交失败 (exit {result.returncode})")
        for line in (result.stderr or "").strip().splitlines()[-10:]:
            err(f"  {line}")
        warn("IndexNow 提交失败，但部署已完成，忽略")


def run(args: list[str], cwd: Path | None = None, label: str = "") -> None:
    """静默执行子命令。成功时静默，失败时 die 并显示 stderr 末尾。

    设置 DEPLOY_VERBOSE=true 可在执行前看到完整命令。
    """
    if VERBOSE:
        log("$ " + " ".join(shlex.quote(c) for c in args))

    result = subprocess.run(
        args,
        cwd=str(cwd) if cwd else None,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )

    if result.returncode != 0:
        err(f"{label or '命令'} 失败 (exit {result.returncode})")
        for line in (result.stderr or "").strip().splitlines()[-15:]:
            err(f"  {line}")
        sys.exit(result.returncode)


# ---------- 入口 ----------
def main() -> int:
    title("Hexo 一键部署")
    require_tools()
    cfg = load_config()

    log(f"目标: {cfg['user']}@{cfg['host']}:{cfg['remote_dir']}")
    log(f"本地: {cfg['public_dir']}")

    header("Step 1/4  构建")
    with step("hexo generate"):
        step_build(cfg)

    header("Step 2/4  同步")
    with step("rsync 同步"):
        step_sync(cfg)

    header("Step 3/4  CDN 刷新")
    log("开始 CDN 刷新...")
    step_refresh_cdn(cfg)

    header("Step 4/4  IndexNow 提交")
    log("开始 IndexNow 提交...")
    step_indexnow(cfg)

    footer("部署完成")
    ok(f"已部署到 {cfg['user']}@{cfg['host']}:{cfg['remote_dir']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        die("用户中断")
