#!/usr/bin/env python3
"""
Hexo 构建产物一键部署脚本

默认流程:
  1. 在本地执行 `hexo generate` 生成 public/
  2. 用 rsync 把 public/ 同步到远程服务器的目标目录

环境变量:
  TENCENT_SERVER_HOST    必填，服务器 host (IP 或域名)
  TENCENT_SERVER_USER    可选，默认 root
  TENCENT_SERVER_PORT    可选，默认 22
  TENCENT_SSH_KEY        可选，默认 ~/.ssh/id_rsa
  REMOTE_DIR             可选，默认 /opt/website/opc-website/python4office.cn
  LOCAL_PUBLIC_DIR       可选，默认 <repo>/hexo/hexo/public
  SKIP_BUILD=true        跳过构建，使用现有 public/
  SKIP_CDN_REFRESH=true  跳过部署后的 CDN 刷新
  DRY_RUN=true           只打印 rsync 命令不实际执行
  HEXO_DIR               可选，默认 <repo>/hexo/hexo
"""

from __future__ import annotations

import os
import shlex
import shutil
import subprocess
import sys
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

# ---------- 颜色 ----------
USE_COLOR = sys.stdout.isatty()
RESET = "\033[0m" if USE_COLOR else ""
RED = "\033[0;31m" if USE_COLOR else ""
GREEN = "\033[0;32m" if USE_COLOR else ""
YELLOW = "\033[1;33m" if USE_COLOR else ""
BLUE = "\033[0;34m" if USE_COLOR else ""
BOLD = "\033[1m" if USE_COLOR else ""


def log(msg: str) -> None:
    print(f"{BLUE}[{datetime.now().strftime('%H:%M:%S')}]{RESET} {msg}")


def ok(msg: str) -> None:
    print(f"{GREEN}✓{RESET} {msg}")


def warn(msg: str) -> None:
    print(f"{YELLOW}⚠{RESET} {msg}")


def err(msg: str) -> None:
    print(f"{RED}✗{RESET} {msg}", file=sys.stderr)


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
    log(f"开始构建: {cfg['hexo_dir']}")
    cmd = [
        "node",
        "--max-old-space-size=8192",
        str(cfg["hexo_dir"] / "node_modules" / "hexo" / "bin" / "hexo"),
        "generate",
        "--draft",
    ]
    run(cmd, cwd=cfg["hexo_dir"], label="hexo generate")


def step_build(cfg: dict) -> None:
    if cfg["skip_build"]:
        log("SKIP_BUILD=true，跳过本地构建")
    else:
        _run_hexo_generate(cfg)

    if not cfg["public_dir"].is_dir():
        die(f"public 目录不存在: {cfg['public_dir']}")

    file_count, size = _stat_public(cfg["public_dir"])
    ok(f"public 就绪: {file_count} 个文件，{size}")


def step_sync(cfg: dict) -> None:
    ssh_target = f"{cfg['user']}@{cfg['host']}"

    log(f"开始同步: {cfg['public_dir']} -> {ssh_target}:{cfg['remote_dir']}")

    rsync_cmd = [
        "rsync",
        "-az",
        "--progress",
        "--delete",
        f"--skip-compress={SKIP_COMPRESS_EXTS}",
        "--exclude=.git",
        "--exclude=.DS_Store",
        "-e",
        f"ssh -i {shlex.quote(str(cfg['ssh_key']))} -p {cfg['port']} -o StrictHostKeyChecking=accept-new",
        f"{shlex.quote(str(cfg['public_dir']) + '/')}",
        f"{ssh_target}:{cfg['remote_dir']}/",
    ]

    print(f"{BLUE}[cmd]{RESET} {' '.join(shlex.quote(c) for c in rsync_cmd)}")

    if cfg["dry_run"]:
        warn("DRY_RUN=true，未实际执行")
        return

    run(rsync_cmd, label="rsync")


def step_refresh_cdn(cfg: dict) -> None:
    """部署成功后调用 refresh_cdn.py 刷新腾讯云 CDN 缓存。"""
    if cfg.get("skip_cdn_refresh"):
        log("SKIP_CDN_REFRESH=true，跳过 CDN 刷新")
        return

    refresh_script = SCRIPT_DIR / "refresh_cdn.py"
    if not refresh_script.is_file():
        warn(f"未找到 CDN 刷新脚本: {refresh_script}，跳过")
        return

    log("开始刷新 CDN 缓存...")
    cmd = [sys.executable, str(refresh_script)]
    print(f"{BLUE}[cmd]{RESET} {' '.join(shlex.quote(c) for c in cmd)}")
    result = subprocess.run(cmd)
    if result.returncode == 0:
        ok("CDN 缓存已刷新")
    else:
        warn(f"CDN 刷新失败 (exit {result.returncode})，但部署已完成，忽略")


def run(cmd: list[str], cwd: Path | None = None, label: str = "") -> None:
    printable = " ".join(shlex.quote(c) for c in cmd)
    print(f"{BLUE}[cmd]{RESET} {printable}")
    result = subprocess.run(cmd, cwd=str(cwd) if cwd else None)
    if result.returncode != 0:
        die(f"{label or '命令'} 失败 (exit {result.returncode})")


# ---------- 入口 ----------
def main() -> int:
    print(f"{BOLD}========== Hexo 一键部署 =========={RESET}")
    require_tools()
    cfg = load_config()

    log(f"目标: {cfg['user']}@{cfg['host']}:{cfg['remote_dir']}")
    log(f"本地: {cfg['public_dir']}")

    step_build(cfg)
    step_sync(cfg)
    step_refresh_cdn(cfg)

    print(f"{BOLD}========== 部署完成 =========={RESET}")
    ok(f"已部署到 {cfg['user']}@{cfg['host']}:{cfg['remote_dir']}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        die("用户中断")
