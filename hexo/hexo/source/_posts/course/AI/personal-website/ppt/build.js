// 第 4 讲：域名与主机选择 - PPT 生成脚本
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");
const md = require("react-icons/md");

const FaGlobe = fa.FaGlobe, FaShieldAlt = fa.FaShieldAlt, FaServer = fa.FaServer;
const FaCheckCircle = fa.FaCheckCircle, FaTimesCircle = fa.FaTimesCircle;
const FaLightbulb = fa.FaLightbulb, FaHome = fa.FaHome, FaMapMarkerAlt = fa.FaMapMarkerAlt;
const FaKey = fa.FaKey, FaLink = fa.FaLink, FaCloud = fa.FaCloud, FaLock = fa.FaLock;
const FaCertificate = fa.FaCertificate, FaExclamationTriangle = fa.FaExclamationTriangle;
const FaArrowRight = fa.FaArrowRight, FaSearch = fa.FaSearch, FaUserShield = fa.FaUserShield;
const FaHttps = fa.FaLock, FaRoute = fa.FaRoute, FaDollarSign = fa.FaDollarSign;
const FaTags = fa.FaTags, FaList = fa.FaList, FaBookOpen = fa.FaBookOpen;
const FaTools = fa.FaTools, FaNetworkWired = fa.FaNetworkWired, FaCode = fa.FaCode;
const FaFlag = fa.FaFlag, FaGraduationCap = fa.FaGraduationCap, FaRocket = fa.FaRocket;
const FaQuestionCircle = fa.FaQuestionCircle;
const MdLanguage = md.MdLanguage, MdDomain = md.MdDomain;
const MdStorage = md.MdStorage, MdPublic = md.MdPublic;

const C = {
  primary: "065A82", secondary: "1C7293", deep: "21295C",
  accent: "F5B800", danger: "DC2626", success: "059669",
  bg: "F8FAFC", white: "FFFFFF", text: "1E293B",
  textMuted: "64748B", border: "E2E8F0",
};
const FH = "Calibri", FB = "Calibri Light";

async function iconToBase64Png(IconComponent, color, size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(
    React.createElement(IconComponent, { color, size: String(size) })
  );
  const pngBuffer = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + pngBuffer.toString("base64");
}

const icons = {};
async function preBuildIcons() {
  const W = "#FFFFFF", A = "#F5B800", P = "#065A82", D = "#DC2626", S = "#059669";
  const set1 = [
    ["globeW", FaGlobe, W], ["shieldW", FaShieldAlt, W], ["serverW", FaServer, W],
    ["checkW", FaCheckCircle, W], ["crossW", FaTimesCircle, W], ["bulbW", FaLightbulb, W],
    ["warnW", FaExclamationTriangle, W],
  ];
  for (const [k, c, col] of set1) icons[k] = await iconToBase64Png(c, col);

  const set2 = [
    ["homeA", FaHome, A], ["mapA", FaMapMarkerAlt, A], ["keyA", FaKey, A],
    ["linkA", FaLink, A], ["cloudA", FaCloud, A], ["lockA", FaLock, A],
    ["certA", FaCertificate, A], ["warnA", FaExclamationTriangle, D],
    ["arrowA", FaArrowRight, A], ["searchA", FaSearch, A], ["userA", FaUserShield, A],
    ["httpsA", FaHttps, A], ["routeA", FaRoute, A], ["dollarA", FaDollarSign, A],
    ["tagsA", FaTags, A], ["listA", FaList, A], ["bookA", FaBookOpen, A],
    ["toolsA", FaTools, A], ["networkA", FaNetworkWired, A], ["codeA", FaCode, A],
    ["flagA", FaFlag, A], ["gradA", FaGraduationCap, A], ["rocketA", FaRocket, A],
    ["questionA", FaQuestionCircle, A],
  ];
  for (const [k, c, col] of set2) icons[k] = await iconToBase64Png(c, col);

  const set3 = [
    ["globeP", FaGlobe, P], ["shieldP", FaShieldAlt, P], ["serverP", FaServer, P],
    ["httpsD", FaHttps, P], ["httpsW", FaHttps, W], ["domainP", MdDomain, P],
    ["publicP", MdPublic, P], ["storageP", MdStorage, P], ["langP", MdLanguage, P],
    ["checkS", FaCheckCircle, S], ["crossD", FaTimesCircle, D],
  ];
  for (const [k, c, col] of set3) icons[k] = await iconToBase64Png(c, col);
}

function drawHeader(s, title, subtitle, sectionLabel) {
  s.addShape("rect", { x: 0, y: 0, w: 10, h: 0.7, fill: { color: C.deep }, line: { color: C.deep } });
  s.addShape("rect", { x: 0, y: 0, w: 0.15, h: 0.7, fill: { color: C.accent }, line: { color: C.accent } });
  if (sectionLabel) {
    s.addText(sectionLabel, {
      x: 0.3, y: 0.05, w: 4, h: 0.25,
      fontSize: 10, color: C.accent, fontFace: FH, bold: true, margin: 0
    });
  }
  s.addText(title, {
    x: 0.3, y: sectionLabel ? 0.28 : 0.1, w: 9.4, h: 0.4,
    fontSize: 22, color: C.white, fontFace: FH, bold: true, margin: 0
  });
  if (subtitle) {
    s.addText(subtitle, {
      x: 0.3, y: 0.75, w: 9.4, h: 0.3,
      fontSize: 11, color: C.textMuted, fontFace: FB, italic: true, margin: 0
    });
  }
}

function drawFooter(s, pageNum, totalPages) {
  s.addShape("line", {
    x: 0.4, y: 5.35, w: 9.2, h: 0,
    line: { color: C.border, width: 0.5 }
  });
  s.addText("AI 编程训练营 · 第 4 讲：域名与主机选择", {
    x: 0.4, y: 5.4, w: 6, h: 0.25,
    fontSize: 9, color: C.textMuted, fontFace: FB, margin: 0
  });
  s.addText(pageNum + " / " + totalPages, {
    x: 8.5, y: 5.4, w: 1.1, h: 0.25,
    fontSize: 9, color: C.textMuted, fontFace: FB, align: "right", margin: 0
  });
}

async function build() {
  await preBuildIcons();
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.author = "程序员晚枫";
  pres.title = "第 4 讲：域名与主机选择";
  const TOTAL = 18;

  // ============ Slide 1: 封面 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.deep };
    s.addShape("rect", { x: 0, y: 0, w: 0.3, h: 5.625, fill: { color: C.accent }, line: { color: C.accent } });
    s.addImage({ data: icons.globeW, x: 0.8, y: 0.7, w: 1.0, h: 1.0 });
    s.addImage({ data: icons.shieldW, x: 1.7, y: 0.7, w: 1.0, h: 1.0 });
    s.addImage({ data: icons.httpsW, x: 0.8, y: 1.7, w: 1.0, h: 1.0 });
    s.addImage({ data: icons.serverW, x: 1.7, y: 1.7, w: 1.0, h: 1.0 });
    s.addText("AI 编程训练营 · 第 4 讲", {
      x: 3.5, y: 1.0, w: 6, h: 0.4,
      fontSize: 14, color: C.accent, fontFace: FH, bold: true, margin: 0, charSpacing: 4
    });
    s.addText("域名与主机选择", {
      x: 3.5, y: 1.6, w: 6.3, h: 1.0,
      fontSize: 48, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    s.addText("给你的网站安个家", {
      x: 3.5, y: 2.6, w: 6.3, h: 0.7,
      fontSize: 30, color: C.accent, fontFace: FH, margin: 0
    });
    s.addShape("line", {
      x: 3.5, y: 3.5, w: 1.2, h: 0,
      line: { color: C.accent, width: 3 }
    });
    s.addText([
      { text: "选对域名 = ", options: { color: C.white, fontFace: FH } },
      { text: "省心三年", options: { color: C.accent, bold: true, fontFace: FH } },
      { text: "    ·    选对主机 = ", options: { color: C.white, fontFace: FH } },
      { text: "不再搬家", options: { color: C.accent, bold: true, fontFace: FH } }
    ], { x: 3.5, y: 3.7, w: 6, h: 0.4, fontSize: 16, margin: 0 });
    s.addText("讲师：程序员晚枫", {
      x: 3.5, y: 4.5, w: 6, h: 0.3,
      fontSize: 12, color: "94A3B8", fontFace: FB, margin: 0
    });
    s.addText("Python 自动化办公社区  ·  公众号：CoderWanFeng", {
      x: 3.5, y: 4.85, w: 6, h: 0.3,
      fontSize: 10, color: "64748B", fontFace: FB, margin: 0
    });
  }

  // ============ Slide 2: 目录 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "本讲内容", "Domain & Hosting Mastery", "课程导览");
    const items = [
      { num: "01", icon: icons.searchA, title: "什么是域名", desc: "域名是门牌号，主机是房子" },
      { num: "02", icon: icons.tagsA, title: "好域名 5 标准 + 6 个坑", desc: "用 AI 帮你取名" },
      { num: "03", icon: icons.listA, title: "后缀价格表 + 注册平台", desc: "Cloudflare / 阿里云 怎么选" },
      { num: "04", icon: icons.networkA, title: "一个域名 = N 个项目", desc: "子域名 / 子目录 / 多后缀" },
      { num: "05", icon: icons.lockA, title: "HTTPS 与 SSL 证书", desc: "为什么域名主机要同一家" },
      { num: "06", icon: icons.serverP, title: "主机类型 + 备案", desc: "3 种主机对比 + 备案流程" },
    ];
    items.forEach((item, i) => {
      const col = i % 3, row = Math.floor(i / 3);
      const x = 0.4 + col * 3.1, y = 1.3 + row * 1.9;
      s.addShape("rect", {
        x: x, y: y, w: 2.9, h: 1.7,
        fill: { color: C.white }, line: { color: C.border, width: 1 },
        shadow: { type: "outer", color: "000000", blur: 6, offset: 2, angle: 135, opacity: 0.06 }
      });
      s.addShape("rect", {
        x: x, y: y, w: 0.1, h: 1.7,
        fill: { color: C.primary }, line: { color: C.primary }
      });
      s.addText(item.num, {
        x: x + 0.2, y: y + 0.1, w: 0.7, h: 0.4,
        fontSize: 18, color: C.accent, fontFace: FH, bold: true, margin: 0
      });
      s.addImage({ data: item.icon, x: x + 2.4, y: y + 0.15, w: 0.35, h: 0.35 });
      s.addText(item.title, {
        x: x + 0.2, y: y + 0.55, w: 2.6, h: 0.4,
        fontSize: 14, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      s.addText(item.desc, {
        x: x + 0.2, y: y + 1.0, w: 2.6, h: 0.6,
        fontSize: 10, color: C.textMuted, fontFace: FB, margin: 0
      });
    });
    drawFooter(s, 2, TOTAL);
  }

  // ============ Slide 3: 引子 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "域名选错，后悔三年", "Domain mistakes that cost you", "01 · 痛点引子");
    s.addShape("rect", {
      x: 0.5, y: 1.4, w: 5, h: 3.6,
      fill: { color: C.white }, line: { color: C.border, width: 1 }
    });
    s.addShape("rect", {
      x: 0.5, y: 1.4, w: 0.1, h: 3.6,
      fill: { color: C.danger }, line: { color: C.danger }
    });
    s.addImage({ data: icons.warnA, x: 0.75, y: 1.55, w: 0.4, h: 0.4 });
    s.addText("真实案例", {
      x: 1.2, y: 1.55, w: 4, h: 0.4,
      fontSize: 16, color: C.danger, fontFace: FH, bold: true, margin: 0
    });
    s.addText([
      { text: "2019 年", options: { bold: true, color: C.text, fontFace: FH, breakLine: true } },
      { text: "我朋友注册了 ", options: { color: C.text, fontFace: FB } },
      { text: "wanfeng.cn", options: { bold: true, color: C.danger, fontFace: "Consolas" } },
      { text: "，当时觉得便宜。", options: { color: C.text, fontFace: FB, breakLine: true } },
      { text: " ", options: { breakLine: true } },
      { text: "一年后", options: { bold: true, color: C.text, fontFace: FH, breakLine: true } },
      { text: "续费涨到 ", options: { color: C.text, fontFace: FB } },
      { text: "150 元/年", options: { bold: true, color: C.danger, fontFace: FH } },
      { text: "，想换 .com。", options: { color: C.text, fontFace: FB, breakLine: true } },
      { text: " ", options: { breakLine: true } },
      { text: "结果", options: { bold: true, color: C.text, fontFace: FH, breakLine: true } },
      { text: "wanfeng.com ", options: { bold: true, color: C.danger, fontFace: "Consolas" } },
      { text: "已被投资人抢注，", options: { color: C.text, fontFace: FB, breakLine: true } },
      { text: "开价 ", options: { color: C.text, fontFace: FB } },
      { text: "5 万", options: { bold: true, color: C.danger, fontSize: 20, fontFace: FH } },
      { text: "。", options: { color: C.text, fontFace: FB } }
    ], {
      x: 0.8, y: 2.1, w: 4.5, h: 2.7,
      fontSize: 13, margin: 0, valign: "top"
    });

    s.addShape("rect", {
      x: 6, y: 1.4, w: 3.6, h: 3.4,
      fill: { color: C.deep }, line: { color: C.deep }
    });
    s.addImage({ data: icons.bulbW, x: 6.3, y: 1.65, w: 0.5, h: 0.5 });
    s.addText("晚枫的话", {
      x: 6.85, y: 1.65, w: 2.5, h: 0.5,
      fontSize: 14, color: C.accent, fontFace: FH, bold: true, margin: 0
    });
    s.addText("域名就像门牌号", {
      x: 6.3, y: 2.4, w: 3.1, h: 0.5,
      fontSize: 18, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    s.addText("选好了跟着你一辈子", {
      x: 6.3, y: 2.85, w: 3.1, h: 0.4,
      fontSize: 14, color: "CBD5E1", fontFace: FB, margin: 0
    });
    s.addShape("line", { x: 6.3, y: 3.4, w: 0.8, h: 0, line: { color: C.accent, width: 2 } });
    s.addText("主机就像房子", {
      x: 6.3, y: 3.6, w: 3.1, h: 0.5,
      fontSize: 18, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    s.addText("租错了还能搬，但搬家很麻烦", {
      x: 6.3, y: 4.05, w: 3.1, h: 0.4,
      fontSize: 14, color: "CBD5E1", fontFace: FB, margin: 0
    });
    drawFooter(s, 3, TOTAL);
  }

  // ============ Slide 4: 什么是域名 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "什么是域名", "What is a Domain Name", "02 · 入门");
    s.addText("域名 = 你的网站地址", {
      x: 0.5, y: 1.3, w: 5.5, h: 0.5,
      fontSize: 22, color: C.primary, fontFace: FH, bold: true, margin: 0
    });
    s.addText("Domain Name，是 IP 地址的人类可读版本", {
      x: 0.5, y: 1.85, w: 5.5, h: 0.5,
      fontSize: 14, color: C.textMuted, fontFace: FB, margin: 0
    });
    s.addShape("rect", {
      x: 0.5, y: 2.5, w: 5.5, h: 2.6,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addImage({ data: icons.homeA, x: 0.75, y: 2.65, w: 0.4, h: 0.4 });
    s.addText("一个生动的比喻", {
      x: 1.25, y: 2.65, w: 4.5, h: 0.4,
      fontSize: 14, color: C.text, fontFace: FH, bold: true, margin: 0
    });
    s.addText([
      { text: "🌐 IP 地址", options: { bold: true, color: C.primary, fontFace: FH, breakLine: true } },
      { text: "142.250.80.46", options: { color: "64748B", fontFace: "Consolas", breakLine: true } },
      { text: "  —— 机器看得懂，但人记不住", options: { color: C.textMuted, fontFace: FB, breakLine: true } },
      { text: " ", options: { breakLine: true } },
      { text: "🏠 域名", options: { bold: true, color: C.primary, fontFace: FH, breakLine: true } },
      { text: "google.com", options: { color: C.accent, fontFace: "Consolas", bold: true, breakLine: true } },
      { text: "  —— 人能记住，浏览器自动解析", options: { color: C.textMuted, fontFace: FB, breakLine: true } },
      { text: " ", options: { breakLine: true } },
      { text: "📌 没有域名的网站 = 没有门牌号的房子", options: { bold: true, color: C.text, fontFace: FH } }
    ], { x: 0.85, y: 3.15, w: 5.0, h: 1.85, fontSize: 11, margin: 0 });

    s.addShape("rect", {
      x: 6.3, y: 1.3, w: 3.3, h: 3.6,
      fill: { color: C.deep }, line: { color: C.deep }
    });
    s.addText("知名域名举例", {
      x: 6.5, y: 1.5, w: 3, h: 0.4,
      fontSize: 14, color: C.accent, fontFace: FH, bold: true, margin: 0
    });
    const examples = [["baidu.com", "百度"], ["google.com", "谷歌"], ["python-office.com", "我的"]];
    examples.forEach((ex, i) => {
      const y = 2.05 + i * 0.65;
      s.addText(ex[0], {
        x: 6.5, y: y, w: 3, h: 0.3,
        fontSize: 13, color: C.white, fontFace: "Consolas", bold: true, margin: 0
      });
      s.addText(ex[1], {
        x: 6.5, y: y + 0.3, w: 3, h: 0.25,
        fontSize: 10, color: "94A3B8", fontFace: FB, margin: 0
      });
    });
    s.addText("→ 域名就是互联网的门牌号", {
      x: 6.5, y: 4.2, w: 3, h: 0.3,
      fontSize: 10, color: C.accent, fontFace: FB, italic: true, margin: 0
    });
    drawFooter(s, 4, TOTAL);
  }

  // ============ Slide 5: 好域名 5 标准 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "好域名的 5 个标准", "5 Standards of a Good Domain", "03 · 取名");
    s.addShape("rect", {
      x: 0.4, y: 1.3, w: 4.5, h: 3.7,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addShape("rect", {
      x: 0.4, y: 1.3, w: 4.5, h: 0.5,
      fill: { color: C.success }, line: { color: C.success }
    });
    s.addText("✅ 5 个推荐标准", {
      x: 0.6, y: 1.35, w: 4.2, h: 0.4,
      fontSize: 14, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    const goods = [
      ["简短好记", "最好 10 个字母以内"],
      ["容易拼写", "避免生僻词"],
      ["与品牌相关", "或与个人品牌相关"],
      ["优先 .com 后缀", "最通用、最专业"],
      ["易口头传播", "我的网站是 xxx.com"]
    ];
    goods.forEach((g, i) => {
      const y = 1.95 + i * 0.58;
      s.addImage({ data: icons.checkS, x: 0.55, y: y + 0.05, w: 0.25, h: 0.25 });
      s.addText(g[0], {
        x: 0.85, y: y, w: 3.9, h: 0.3,
        fontSize: 13, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      s.addText(g[1], {
        x: 0.85, y: y + 0.28, w: 3.9, h: 0.25,
        fontSize: 10, color: C.textMuted, fontFace: FB, margin: 0
      });
    });

    s.addShape("rect", {
      x: 5.1, y: 1.3, w: 4.5, h: 3.7,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addShape("rect", {
      x: 5.1, y: 1.3, w: 4.5, h: 0.5,
      fill: { color: C.danger }, line: { color: C.danger }
    });
    s.addText("❌ 5 个常见坑", {
      x: 5.3, y: 1.35, w: 4.2, h: 0.4,
      fontSize: 14, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    const bads = [
      ["太长", "超过 15 个字母"],
      ["连字符", "wan-feng.com 不易口头传播"],
      ["数字", "wanfeng123.com 很 low"],
      ["生僻单词", "别人拼不出来"],
      ["易拼错的组合", "发音和拼写不一致"]
    ];
    bads.forEach((b, i) => {
      const y = 1.95 + i * 0.58;
      s.addImage({ data: icons.crossD, x: 5.25, y: y + 0.05, w: 0.25, h: 0.25 });
      s.addText(b[0], {
        x: 5.55, y: y, w: 3.9, h: 0.3,
        fontSize: 13, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      s.addText(b[1], {
        x: 5.55, y: y + 0.28, w: 3.9, h: 0.25,
        fontSize: 10, color: C.textMuted, fontFace: FB, margin: 0
      });
    });
    drawFooter(s, 5, TOTAL);
  }

  // ============ Slide 6: 用 AI 取域名 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "用 AI 帮你取域名", "Use AI to Generate Domain Ideas", "03 · 取名");
    s.addShape("rect", {
      x: 0.5, y: 1.3, w: 9, h: 2.6,
      fill: { color: "0F172A" }, line: { color: "0F172A" }
    });
    s.addImage({ data: icons.codeA, x: 0.75, y: 1.5, w: 0.35, h: 0.35 });
    s.addText("AI Prompt 模板", {
      x: 1.2, y: 1.5, w: 5, h: 0.35,
      fontSize: 14, color: C.accent, fontFace: FH, bold: true, margin: 0
    });
    s.addText([
      { text: "我想注册一个个人网站域名，我的情况是：", options: { color: "E2E8F0", fontFace: "Consolas", breakLine: true } },
      { text: "  • 名字/昵称：[填写你的名字]", options: { color: "94A3B8", fontFace: "Consolas", breakLine: true } },
      { text: "  • 职业/领域：[填写你的领域]", options: { color: "94A3B8", fontFace: "Consolas", breakLine: true } },
      { text: "  • 目标用户：[填写目标用户]", options: { color: "94A3B8", fontFace: "Consolas", breakLine: true } },
      { text: "  • 网站目标：[展示/获客/内容/电商]", options: { color: "94A3B8", fontFace: "Consolas", breakLine: true } },
      { text: " ", options: { breakLine: true } },
      { text: "请帮我推荐 10 个域名，要求：", options: { color: C.accent, fontFace: "Consolas", bold: true, breakLine: true } },
      { text: "  1. 简短好记（10 个字母以内）", options: { color: "CBD5E1", fontFace: "Consolas", breakLine: true } },
      { text: "  2. 优先 .com 或 .cn 后缀", options: { color: "CBD5E1", fontFace: "Consolas", breakLine: true } },
      { text: "  3. 与我的个人品牌相关", options: { color: "CBD5E1", fontFace: "Consolas", breakLine: true } },
      { text: "  4. 每个域名说明含义，考虑 SEO 价值", options: { color: "CBD5E1", fontFace: "Consolas" } }
    ], { x: 0.85, y: 1.95, w: 8.5, h: 1.85, margin: 0, fontSize: 11 });

    s.addShape("rect", {
      x: 0.5, y: 4.1, w: 9, h: 0.95,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addShape("rect", {
      x: 0.5, y: 4.1, w: 0.1, h: 0.95,
      fill: { color: C.accent }, line: { color: C.accent }
    });
    s.addImage({ data: icons.bulbW, x: 0.75, y: 4.25, w: 0.35, h: 0.35 });
    s.addText("5 个常见取名思路", {
      x: 1.2, y: 4.25, w: 5, h: 0.35,
      fontSize: 13, color: C.primary, fontFace: FH, bold: true, margin: 0
    });
    s.addText("你的名字 (wanfeng.com) · 名字+职业 (designerwan.com) · 品牌名 (pythonoffice.cn) · 动词+名词 (learnai.com) · 行业+名字 (aiwanfeng.com)", {
      x: 1.2, y: 4.6, w: 8.2, h: 0.4,
      fontSize: 10, color: C.textMuted, fontFace: FB, margin: 0
    });
    drawFooter(s, 6, TOTAL);
  }

  // ============ Slide 7: 后缀价格表 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "域名后缀价格指南", "Price & SEO Guide for TLDs", "04 · 后缀选择");
    const headers = ["后缀", "价格/年", "适合人群", "SEO", "专业度"];
    const rows = [
      [".com", "60-80元", "所有人", "5/5", "最高"],
      [".cn", "30-50元", "国内市场", "4/5", "高"],
      [".ai", "400-600元", "AI / 科技", "4/5", "很高"],
      [".io", "300-400元", "技术 / 开发者", "3/5", "高"],
      [".dev", "150-200元", "开发者", "3/5", "高"],
      [".me", "80-120元", "个人网站", "3/5", "中"],
      [".xyz", "10-30元", "预算有限", "2/5", "低"]
    ];
    const tableData = [headers.map(h => ({
      text: h,
      options: { bold: true, color: C.white, fill: { color: C.primary },
        fontFace: FH, fontSize: 12, align: "center", valign: "middle" }
    }))];
    rows.forEach((r, i) => {
      tableData.push([
        { text: r[0], options: { bold: true, color: i === 0 ? C.accent : C.text, fontFace: "Consolas", fontSize: 12, align: "left", valign: "middle" } },
        { text: r[1], options: { color: C.text, fontFace: FH, fontSize: 11, align: "center", valign: "middle" } },
        { text: r[2], options: { color: C.text, fontFace: FB, fontSize: 11, align: "center", valign: "middle" } },
        { text: r[3], options: { color: C.text, fontFace: FH, fontSize: 11, align: "center", valign: "middle" } },
        { text: r[4], options: { color: C.text, fontFace: FB, fontSize: 11, align: "center", valign: "middle", bold: true } }
      ]);
    });
    s.addTable(tableData, {
      x: 0.4, y: 1.3, w: 6.2, h: 3.2,
      colW: [0.9, 1.3, 1.7, 1.4, 0.9],
      rowH: 0.4,
      border: { pt: 0.5, color: C.border }
    });

    s.addShape("rect", {
      x: 6.8, y: 1.3, w: 2.9, h: 3.6,
      fill: { color: C.deep }, line: { color: C.deep }
    });
    s.addText("晚枫的建议", {
      x: 7.0, y: 1.5, w: 2.5, h: 0.4,
      fontSize: 13, color: C.accent, fontFace: FH, bold: true, margin: 0
    });
    const recs = [
      "首选 .com（最通用）",
      "国内市场可以 .cn",
      "AI 领域可以 .ai（贵）"
    ];
    recs.forEach((r, i) => {
      const y = 2.0 + i * 0.4;
      s.addImage({ data: icons.arrowA, x: 7.0, y: y, w: 0.25, h: 0.25 });
      s.addText(r, {
        x: 7.3, y: y, w: 2.3, h: 0.3,
        fontSize: 11, color: C.white, fontFace: FH, bold: true, margin: 0
      });
    });
    s.addShape("rect", {
      x: 7.0, y: 3.3, w: 2.5, h: 1.4,
      fill: { color: C.danger }, line: { color: C.danger }
    });
    s.addImage({ data: icons.warnW, x: 7.15, y: 3.45, w: 0.3, h: 0.3 });
    s.addText("千万别选 .xyz", {
      x: 7.5, y: 3.45, w: 2, h: 0.3,
      fontSize: 12, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    s.addText("为了省钱选 .xyz，\n看起来非常不专业，\n做正经项目请绕开", {
      x: 7.15, y: 3.85, w: 2.3, h: 0.8,
      fontSize: 10, color: C.white, fontFace: FB, margin: 0
    });
    drawFooter(s, 7, TOTAL);
  }

  // ============ Slide 8: 注册平台推荐 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "域名注册平台推荐", "Where to Register Your Domain", "05 · 平台");
    s.addShape("rect", {
      x: 0.4, y: 1.3, w: 4.5, h: 3.6,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addShape("rect", {
      x: 0.4, y: 1.3, w: 4.5, h: 0.55,
      fill: { color: C.primary }, line: { color: C.primary }
    });
    s.addText("🌍 国际平台（推荐）", {
      x: 0.6, y: 1.4, w: 4.2, h: 0.4,
      fontSize: 14, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    const intl = [
      { name: "Cloudflare", score: "成本价，最便宜", rec: "推荐", color: C.success },
      { name: "Namecheap",  score: "便宜，界面友好", rec: "备选", color: C.textMuted },
      { name: "GoDaddy",    score: "最大，但续费贵", rec: "不推荐", color: C.danger }
    ];
    intl.forEach((p, i) => {
      const y = 2.05 + i * 0.95;
      s.addShape("rect", {
        x: 0.55, y: y, w: 4.2, h: 0.8,
        fill: { color: C.bg }, line: { color: C.border }
      });
      s.addText(p.name, {
        x: 0.7, y: y + 0.1, w: 2.3, h: 0.35,
        fontSize: 14, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      s.addText(p.score, {
        x: 0.7, y: y + 0.42, w: 2.3, h: 0.3,
        fontSize: 10, color: C.textMuted, fontFace: FB, margin: 0
      });
      s.addShape("rect", {
        x: 3.1, y: y + 0.2, w: 1.5, h: 0.4,
        fill: { color: p.color }, line: { color: p.color }
      });
      s.addText(p.rec, {
        x: 3.1, y: y + 0.2, w: 1.5, h: 0.4,
        fontSize: 10, color: C.white, fontFace: FH, bold: true, align: "center", valign: "middle", margin: 0
      });
    });

    s.addShape("rect", {
      x: 5.1, y: 1.3, w: 4.5, h: 3.6,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addShape("rect", {
      x: 5.1, y: 1.3, w: 4.5, h: 0.55,
      fill: { color: C.secondary }, line: { color: C.secondary }
    });
    s.addText("🇨🇳 国内平台", {
      x: 5.3, y: 1.4, w: 4.2, h: 0.4,
      fontSize: 14, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    const cn = [
      { name: "阿里云", score: "国内最大，.cn 首选", rec: "推荐", color: C.success },
      { name: "腾讯云", score: "也不错", rec: "备选", color: C.textMuted },
      { name: "西部数码", score: "便宜", rec: "考虑", color: C.textMuted }
    ];
    cn.forEach((p, i) => {
      const y = 2.05 + i * 0.95;
      s.addShape("rect", {
        x: 5.25, y: y, w: 4.2, h: 0.8,
        fill: { color: C.bg }, line: { color: C.border }
      });
      s.addText(p.name, {
        x: 5.4, y: y + 0.1, w: 2.3, h: 0.35,
        fontSize: 14, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      s.addText(p.score, {
        x: 5.4, y: y + 0.42, w: 2.3, h: 0.3,
        fontSize: 10, color: C.textMuted, fontFace: FB, margin: 0
      });
      s.addShape("rect", {
        x: 7.8, y: y + 0.2, w: 1.5, h: 0.4,
        fill: { color: p.color }, line: { color: p.color }
      });
      s.addText(p.rec, {
        x: 7.8, y: y + 0.2, w: 1.5, h: 0.4,
        fontSize: 10, color: C.white, fontFace: FH, bold: true, align: "center", valign: "middle", margin: 0
      });
    });
    drawFooter(s, 8, TOTAL);
  }

  // ============ Slide 9: 一个域名 = N 个项目 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "一个域名 = N 个项目", "One Domain, Many Projects", "06 · 子域名技巧");
    const methods = [
      { title: "子域名前缀", rec: "推荐", color: C.success, code: "blog.python-office.com", desc: "在主域名前加前缀\n指向完全独立的网站" },
      { title: "子目录后缀", rec: "路径形式", color: C.secondary, code: "python-office.com/blog/", desc: "在主域名下用路径区分\n适合所有项目同主机部署" },
      { title: "多后缀保护", rec: "防抢注", color: C.accent, code: ".com / .cn / .net", desc: "同名不同后缀全买下来\n都指向同一个网站" }
    ];
    methods.forEach((m, i) => {
      const x = 0.4 + i * 3.15;
      s.addShape("rect", {
        x: x, y: 1.3, w: 3.0, h: 3.5,
        fill: { color: C.white }, line: { color: C.border },
        shadow: { type: "outer", color: "000000", blur: 8, offset: 2, angle: 135, opacity: 0.08 }
      });
      s.addShape("rect", {
        x: x, y: 1.3, w: 3.0, h: 0.5,
        fill: { color: m.color }, line: { color: m.color }
      });
      s.addText(m.rec, {
        x: x + 0.15, y: 1.35, w: 2.7, h: 0.4,
        fontSize: 11, color: C.white, fontFace: FH, bold: true, charSpacing: 3, margin: 0
      });
      s.addText(m.title, {
        x: x + 0.15, y: 1.95, w: 2.7, h: 0.45,
        fontSize: 18, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      s.addShape("rect", {
        x: x + 0.15, y: 2.5, w: 2.7, h: 0.55,
        fill: { color: "0F172A" }, line: { color: "0F172A" }
      });
      s.addText(m.code, {
        x: x + 0.25, y: 2.5, w: 2.5, h: 0.55,
        fontSize: 11, color: C.accent, fontFace: "Consolas", bold: true, valign: "middle", margin: 0
      });
      s.addText(m.desc, {
        x: x + 0.15, y: 3.2, w: 2.7, h: 1.0,
        fontSize: 11, color: C.textMuted, fontFace: FB, margin: 0
      });
    });
    s.addShape("rect", {
      x: 0.4, y: 4.95, w: 9.2, h: 0.45,
      fill: { color: C.deep }, line: { color: C.deep }
    });
    s.addImage({ data: icons.rocketA, x: 0.6, y: 5.02, w: 0.3, h: 0.3 });
    s.addText("一个人买一个域名，可以承载十几个项目 —— 关键是做好 DNS 解析", {
      x: 1.0, y: 5.0, w: 8.5, h: 0.4,
      fontSize: 12, color: C.white, fontFace: FH, bold: true, valign: "middle", margin: 0
    });
    drawFooter(s, 9, TOTAL);
  }

  // ============ Slide 10: HTTPS 与 SSL ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "HTTPS 与 SSL 证书", "Why HTTPS & SSL Matter", "07 · 安全");
    s.addShape("rect", {
      x: 0.4, y: 1.3, w: 9.2, h: 1.6,
      fill: { color: C.danger }, line: { color: C.danger }
    });
    s.addImage({ data: icons.warnW, x: 0.65, y: 1.55, w: 0.5, h: 0.5 });
    s.addText("为什么要开 HTTPS？", {
      x: 1.25, y: 1.55, w: 4, h: 0.4,
      fontSize: 16, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    s.addText([
      { text: "🔒 没有 HTTPS → ", options: { color: C.white, bold: true, fontFace: FH } },
      { text: "Chrome 标记「不安全」", options: { color: C.white, fontFace: FB, breakLine: true } },
      { text: "🚫 没有 HTTPS → ", options: { color: C.white, bold: true, fontFace: FH } },
      { text: "微信分享链接被拦截", options: { color: C.white, fontFace: FB, breakLine: true } },
      { text: "🔑 没有 HTTPS → ", options: { color: C.white, bold: true, fontFace: FH } },
      { text: "用户根本不敢输入密码", options: { color: C.white, fontFace: FB } }
    ], { x: 1.25, y: 2.0, w: 8.0, h: 0.85, fontSize: 12, margin: 0 });

    s.addShape("rect", {
      x: 0.4, y: 3.05, w: 4.4, h: 2.0,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addText("SSL 证书两种方案", {
      x: 0.6, y: 3.15, w: 4, h: 0.35,
      fontSize: 13, color: C.text, fontFace: FH, bold: true, margin: 0
    });
    s.addTable([
      [
        { text: "方案", options: { bold: true, color: C.white, fill: { color: C.primary }, fontSize: 11, align: "center", valign: "middle" } },
        { text: "价格", options: { bold: true, color: C.white, fill: { color: C.primary }, fontSize: 11, align: "center", valign: "middle" } },
        { text: "适合", options: { bold: true, color: C.white, fill: { color: C.primary }, fontSize: 11, align: "center", valign: "middle" } }
      ],
      [
        { text: "Let's Encrypt", options: { color: C.success, bold: true, fontSize: 11, align: "left", valign: "middle" } },
        { text: "0 元", options: { color: C.text, fontSize: 11, align: "center", valign: "middle" } },
        { text: "个人站", options: { color: C.textMuted, fontSize: 10, align: "center", valign: "middle" } }
      ],
      [
        { text: "付费 DV/OV", options: { color: C.text, bold: true, fontSize: 11, align: "left", valign: "middle" } },
        { text: "几百起/年", options: { color: C.text, fontSize: 11, align: "center", valign: "middle" } },
        { text: "企业 / 电商", options: { color: C.textMuted, fontSize: 10, align: "center", valign: "middle" } }
      ]
    ], {
      x: 0.55, y: 3.55, w: 4.1, h: 1.3,
      colW: [1.4, 1.2, 1.5], rowH: 0.4,
      border: { pt: 0.5, color: C.border }
    });

    s.addShape("rect", {
      x: 5.0, y: 3.05, w: 4.6, h: 2.0,
      fill: { color: C.deep }, line: { color: C.deep }
    });
    s.addImage({ data: icons.keyA, x: 5.25, y: 3.2, w: 0.4, h: 0.4 });
    s.addText("关键结论", {
      x: 5.7, y: 3.2, w: 3.5, h: 0.4,
      fontSize: 14, color: C.accent, fontFace: FH, bold: true, margin: 0
    });
    s.addText([
      { text: "证书签发依赖 DNS 控制权", options: { color: C.white, fontFace: FH, bold: true, breakLine: true } },
      { text: "  → 域名主机必须同一家", options: { color: "CBD5E1", fontFace: FB, breakLine: true } },
      { text: " ", options: { breakLine: true } },
      { text: "✅ 同一家 → ", options: { color: C.success, fontFace: FH } },
      { text: "一键自动配置", options: { color: C.white, fontFace: FH, breakLine: true } },
      { text: "❌ 分两家 → ", options: { color: C.danger, fontFace: FH } },
      { text: "手动两边配，续期会想哭", options: { color: C.white, fontFace: FB } }
    ], { x: 5.25, y: 3.65, w: 4.2, h: 1.35, fontSize: 12, margin: 0 });
    drawFooter(s, 10, TOTAL);
  }

  // ============ Slide 11: 同服务商策略 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "域名 + 主机怎么搭？", "Domain & Hosting Strategy", "07 · 部署策略");

    s.addShape("rect", {
      x: 0.4, y: 1.3, w: 4.5, h: 3.5,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addShape("rect", {
      x: 0.4, y: 1.3, w: 4.5, h: 0.55,
      fill: { color: C.danger }, line: { color: C.danger }
    });
    s.addImage({ data: icons.crossW, x: 0.6, y: 1.4, w: 0.35, h: 0.35 });
    s.addText("❌ 反面教材：三家分立", {
      x: 1.05, y: 1.4, w: 4, h: 0.4,
      fontSize: 14, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    const bads = [
      { label: "域名", value: "Cloudflare" },
      { label: "主机", value: "阿里云" },
      { label: "CDN", value: "另一家" }
    ];
    bads.forEach((b, i) => {
      const y = 2.0 + i * 0.5;
      s.addText(b.label, {
        x: 0.6, y: y, w: 1.5, h: 0.35,
        fontSize: 12, color: C.textMuted, fontFace: FH, margin: 0
      });
      s.addShape("rect", {
        x: 2.1, y: y, w: 2.6, h: 0.35,
        fill: { color: C.danger, transparency: 80 }, line: { color: C.danger }
      });
      s.addText(b.value, {
        x: 2.1, y: y, w: 2.6, h: 0.35,
        fontSize: 11, color: C.danger, fontFace: "Consolas", bold: true, align: "center", valign: "middle", margin: 0
      });
    });
    s.addShape("rect", {
      x: 0.55, y: 3.7, w: 4.2, h: 1.0,
      fill: { color: "FEE2E2" }, line: { color: "FEE2E2" }
    });
    s.addText("→ HTTPS 证书两边手动配，\n→ 续期经常出错，\n→ 维护成本翻 3 倍", {
      x: 0.7, y: 3.75, w: 4, h: 0.9,
      fontSize: 11, color: C.danger, fontFace: FB, bold: true, margin: 0
    });

    s.addShape("rect", {
      x: 5.1, y: 1.3, w: 4.5, h: 3.5,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addShape("rect", {
      x: 5.1, y: 1.3, w: 4.5, h: 0.55,
      fill: { color: C.success }, line: { color: C.success }
    });
    s.addImage({ data: icons.checkW, x: 5.3, y: 1.4, w: 0.35, h: 0.35 });
    s.addText("✅ 推荐：同一家搞定", {
      x: 5.75, y: 1.4, w: 4, h: 0.4,
      fontSize: 14, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    const goods = [
      { label: "国内站", value: "阿里云 / 腾讯云" },
      { label: "国际站", value: "Cloudflare + Vercel" },
      { label: "HTTPS", value: "一键自动配置" }
    ];
    goods.forEach((g, i) => {
      const y = 2.0 + i * 0.5;
      s.addText(g.label, {
        x: 5.3, y: y, w: 1.5, h: 0.35,
        fontSize: 12, color: C.textMuted, fontFace: FH, margin: 0
      });
      s.addShape("rect", {
        x: 6.8, y: y, w: 2.6, h: 0.35,
        fill: { color: C.success, transparency: 80 }, line: { color: C.success }
      });
      s.addText(g.value, {
        x: 6.8, y: y, w: 2.6, h: 0.35,
        fontSize: 11, color: C.success, fontFace: "Consolas", bold: true, align: "center", valign: "middle", margin: 0
      });
    });
    s.addShape("rect", {
      x: 5.25, y: 3.7, w: 4.2, h: 1.0,
      fill: { color: "D1FAE5" }, line: { color: "D1FAE5" }
    });
    s.addText("→ 证书自动签发、自动续期，\n→ 一键开启 HTTPS，\n→ 维护成本接近 0", {
      x: 5.4, y: 3.75, w: 4, h: 0.9,
      fontSize: 11, color: C.success, fontFace: FB, bold: true, margin: 0
    });
    drawFooter(s, 11, TOTAL);
  }

  // ============ Slide 12: 主机类型 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "主机类型详解", "3 Types of Web Hosting", "08 · 主机选择");
    const types = [
      { name: "共享主机", en: "Shared", price: "100-300元/年", fit: "个人网站、小流量", pros: "便宜", cons: "邻居影响", icon: icons.serverP, color: C.secondary },
      { name: "云服务器", en: "VPS", price: "300-1000元/年", fit: "中等流量、可控", pros: "独立", cons: "需运维", icon: icons.cloudA, color: C.primary },
      { name: "托管主机", en: "Managed", price: "500-2000元/年", fit: "不想折腾", pros: "省心", cons: "贵", icon: icons.userA, color: C.accent }
    ];
    types.forEach((t, i) => {
      const x = 0.4 + i * 3.15;
      s.addShape("rect", {
        x: x, y: 1.3, w: 3.0, h: 3.5,
        fill: { color: C.white }, line: { color: C.border },
        shadow: { type: "outer", color: "000000", blur: 6, offset: 2, angle: 135, opacity: 0.06 }
      });
      s.addShape("rect", {
        x: x, y: 1.3, w: 3.0, h: 0.9,
        fill: { color: t.color }, line: { color: t.color }
      });
      s.addImage({ data: t.icon, x: x + 0.2, y: 1.45, w: 0.5, h: 0.5 });
      s.addText(t.name, {
        x: x + 0.8, y: 1.45, w: 2.0, h: 0.35,
        fontSize: 16, color: C.white, fontFace: FH, bold: true, margin: 0
      });
      s.addText(t.en, {
        x: x + 0.8, y: 1.78, w: 2.0, h: 0.3,
        fontSize: 11, color: "F1F5F9", fontFace: FB, margin: 0
      });
      s.addText("价格", {
        x: x + 0.2, y: 2.35, w: 2.6, h: 0.25,
        fontSize: 10, color: C.textMuted, fontFace: FB, margin: 0
      });
      s.addText(t.price, {
        x: x + 0.2, y: 2.6, w: 2.6, h: 0.3,
        fontSize: 14, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      s.addText("适合", {
        x: x + 0.2, y: 3.0, w: 2.6, h: 0.25,
        fontSize: 10, color: C.textMuted, fontFace: FB, margin: 0
      });
      s.addText(t.fit, {
        x: x + 0.2, y: 3.25, w: 2.6, h: 0.3,
        fontSize: 12, color: C.text, fontFace: FH, margin: 0
      });
      s.addShape("rect", {
        x: x + 0.2, y: 3.7, w: 1.25, h: 0.35,
        fill: { color: "D1FAE5" }, line: { color: "D1FAE5" }
      });
      s.addText("+ " + t.pros, {
        x: x + 0.2, y: 3.7, w: 1.25, h: 0.35,
        fontSize: 11, color: C.success, fontFace: FH, bold: true, align: "center", valign: "middle", margin: 0
      });
      s.addShape("rect", {
        x: x + 1.55, y: 3.7, w: 1.25, h: 0.35,
        fill: { color: "FEE2E2" }, line: { color: "FEE2E2" }
      });
      s.addText("- " + t.cons, {
        x: x + 1.55, y: 3.7, w: 1.25, h: 0.35,
        fontSize: 11, color: C.danger, fontFace: FH, bold: true, align: "center", valign: "middle", margin: 0
      });
    });
    drawFooter(s, 12, TOTAL);
  }

  // ============ Slide 13: 主机性能对比 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "主机方案性能对比", "Performance Comparison", "08 · 主机选择");
    const headers = ["方案", "访客容量", "响应", "可用性", "成本/年"];
    const rows = [
      ["Notion+Super", "无限", "3-5秒", "99.9%", "100元"],
      ["Framer", "无限", "1-2秒", "99.9%", "1200元"],
      ["SiteGround", "1万+", "1-3秒", "99.9%", "300元"],
      ["阿里云轻量", "5万+", "0.5-2秒", "99.95%", "200-500元"],
      ["GitHub Pages", "10万+", "0.5-1秒", "99.9%", "免费"]
    ];
    const tableData = [headers.map(h => ({
      text: h,
      options: { bold: true, color: C.white, fill: { color: C.primary },
        fontFace: FH, fontSize: 12, align: "center", valign: "middle" }
    }))];
    rows.forEach((r, i) => {
      const highlight = (i === 4);
      tableData.push([
        { text: r[0], options: { bold: true, color: highlight ? C.success : C.text, fontFace: "Consolas", fontSize: 11, align: "left", valign: "middle" } },
        { text: r[1], options: { color: C.text, fontFace: FH, fontSize: 11, align: "center", valign: "middle" } },
        { text: r[2], options: { color: C.text, fontFace: FH, fontSize: 11, align: "center", valign: "middle" } },
        { text: r[3], options: { color: C.text, fontFace: FH, fontSize: 11, align: "center", valign: "middle" } },
        { text: r[4], options: { color: highlight ? C.success : C.text, fontFace: FH, fontSize: 11, bold: true, align: "center", valign: "middle" } }
      ]);
    });
    s.addTable(tableData, {
      x: 0.4, y: 1.3, w: 9.2, h: 2.8,
      colW: [2.0, 1.8, 1.8, 1.8, 1.8],
      rowH: 0.45,
      border: { pt: 0.5, color: C.border }
    });
    s.addShape("rect", {
      x: 0.4, y: 4.2, w: 9.2, h: 0.85,
      fill: { color: C.deep }, line: { color: C.deep }
    });
    s.addImage({ data: icons.bulbW, x: 0.6, y: 4.35, w: 0.4, h: 0.4 });
    s.addText("新手首选 GitHub Pages（免费 + 性能强）；国内业务选阿里云轻量（需备案）", {
      x: 1.1, y: 4.3, w: 8.4, h: 0.4,
      fontSize: 13, color: C.white, fontFace: FH, bold: true, valign: "middle", margin: 0
    });
    drawFooter(s, 13, TOTAL);
  }

  // ============ Slide 14: 网站备案 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "网站备案（国内必看）", "ICP Filing for China Sites", "09 · 备案");
    // 左：需要 vs 不需要
    s.addShape("rect", {
      x: 0.4, y: 1.3, w: 4.4, h: 3.7,
      fill: { color: C.white }, line: { color: C.border }
    });
    s.addText("我需要备案吗？", {
      x: 0.6, y: 1.45, w: 4, h: 0.4,
      fontSize: 14, color: C.text, fontFace: FH, bold: true, margin: 0
    });
    // 需要
    s.addShape("rect", {
      x: 0.55, y: 1.95, w: 4.1, h: 1.4,
      fill: { color: "FEE2E2" }, line: { color: "FEE2E2" }
    });
    s.addImage({ data: icons.crossD, x: 0.7, y: 2.05, w: 0.3, h: 0.3 });
    s.addText("需要备案", {
      x: 1.05, y: 2.05, w: 3, h: 0.3,
      fontSize: 13, color: C.danger, fontFace: FH, bold: true, margin: 0
    });
    s.addText("主机在国内（阿里云 / 腾讯云等）\n面向国内用户", {
      x: 0.7, y: 2.45, w: 4, h: 0.85,
      fontSize: 11, color: C.text, fontFace: FB, margin: 0
    });
    // 不需要
    s.addShape("rect", {
      x: 0.55, y: 3.5, w: 4.1, h: 1.4,
      fill: { color: "D1FAE5" }, line: { color: "D1FAE5" }
    });
    s.addImage({ data: icons.checkS, x: 0.7, y: 3.6, w: 0.3, h: 0.3 });
    s.addText("不需要备案", {
      x: 1.05, y: 3.6, w: 3, h: 0.3,
      fontSize: 13, color: C.success, fontFace: FH, bold: true, margin: 0
    });
    s.addText("主机在国外（推荐新手）\n免主机方案 / GitHub Pages / Vercel", {
      x: 0.7, y: 4.0, w: 4, h: 0.85,
      fontSize: 11, color: C.text, fontFace: FB, margin: 0
    });

    // 右：7 步流程
    s.addShape("rect", {
      x: 5.0, y: 1.3, w: 4.6, h: 3.7,
      fill: { color: C.deep }, line: { color: C.deep }
    });
    s.addText("备案流程（以阿里云为例）", {
      x: 5.2, y: 1.45, w: 4.2, h: 0.4,
      fontSize: 14, color: C.accent, fontFace: FH, bold: true, margin: 0
    });
    const steps = [
      "购买国内主机",
      "登录阿里云备案系统",
      "填写个人信息",
      "上传身份证照片",
      "拍照核验（阿里云 APP）",
      "等待审核（7-20 天）",
      "备案成功"
    ];
    steps.forEach((st, i) => {
      const y = 2.0 + i * 0.4;
      // 圆点编号
      s.addShape("ellipse", {
        x: 5.2, y: y, w: 0.3, h: 0.3,
        fill: { color: C.accent }, line: { color: C.accent }
      });
      s.addText(String(i + 1), {
        x: 5.2, y: y, w: 0.3, h: 0.3,
        fontSize: 11, color: C.deep, fontFace: FH, bold: true, align: "center", valign: "middle", margin: 0
      });
      s.addText(st, {
        x: 5.6, y: y, w: 4.0, h: 0.3,
        fontSize: 11, color: C.white, fontFace: FB, valign: "middle", margin: 0
      });
    });
    drawFooter(s, 14, TOTAL);
  }

  // ============ Slide 15: 域名解析记录类型 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "域名解析记录类型", "DNS Record Types", "10 · DNS");
    const records = [
      { code: "A", name: "地址记录", desc: "域名 → IP 地址\n最常用", color: C.primary, example: "@ → 1.2.3.4" },
      { code: "CNAME", name: "别名记录", desc: "域名 → 另一个域名\n适合 CDN", color: C.secondary, example: "www → site.framer.app" },
      { code: "MX", name: "邮件记录", desc: "域名 → 邮件服务器\n配企业邮箱用", color: C.accent, example: "@ → mail.xxx.com" }
    ];
    records.forEach((r, i) => {
      const x = 0.4 + i * 3.15;
      s.addShape("rect", {
        x: x, y: 1.3, w: 3.0, h: 3.5,
        fill: { color: C.white }, line: { color: C.border }
      });
      s.addShape("rect", {
        x: x, y: 1.3, w: 3.0, h: 0.6,
        fill: { color: r.color }, line: { color: r.color }
      });
      s.addText(r.code, {
        x: x, y: 1.3, w: 3.0, h: 0.6,
        fontSize: 22, color: C.white, fontFace: "Consolas", bold: true, align: "center", valign: "middle", margin: 0
      });
      s.addText(r.name, {
        x: x + 0.2, y: 2.05, w: 2.6, h: 0.4,
        fontSize: 14, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      s.addText(r.desc, {
        x: x + 0.2, y: 2.5, w: 2.6, h: 1.0,
        fontSize: 11, color: C.textMuted, fontFace: FB, margin: 0
      });
      s.addShape("rect", {
        x: x + 0.2, y: 3.6, w: 2.6, h: 0.65,
        fill: { color: "0F172A" }, line: { color: "0F172A" }
      });
      s.addText(r.example, {
        x: x + 0.3, y: 3.6, w: 2.4, h: 0.65,
        fontSize: 11, color: C.accent, fontFace: "Consolas", bold: true, valign: "middle", margin: 0
      });
    });
    drawFooter(s, 15, TOTAL);
  }

  // ============ Slide 16: 5 大避坑 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "5 大避坑陷阱", "5 Pitfalls to Dodge", "11 · 避坑指南");
    const traps = [
      { num: "1", title: "在 GoDaddy 注册域名", bad: "首年便宜，续费贵 (.com $20+/年)", good: "用 Cloudflare，成本价" },
      { num: "2", title: "选最便宜的主机", bad: "50 元/年，随时宕机丢数据", good: "选靠谱服务商，多花 100 元/年" },
      { num: "3", title: "不设自动续费", bad: "忘记续费，域名被抢注", good: "开自动续费 + 到期提醒" },
      { num: "4", title: "备案选错接入商", bad: "A 备案，B 主机，备案注销", good: "备案和主机用同一家" },
      { num: "5", title: "DNS 改完不验证", bad: "以为万事大吉", good: "用 dig / nslookup 验证" }
    ];
    traps.forEach((t, i) => {
      const y = 1.3+ i * 0.788
      // 编号圆
      s.addShape("ellipse", {
        x: 0.4, y: y, w: 0.6, h: 0.6,
        fill: { color: C.danger }, line: { color: C.danger }
      });
      s.addText(t.num, {
        x: 0.4, y: y, w: 0.6, h: 0.6,
        fontSize: 20, color: C.white, fontFace: FH, bold: true, align: "center", valign: "middle", margin: 0
      });
      // 标题
      s.addText(t.title, {
        x: 1.1, y: y, w: 4, h: 0.3,
        fontSize: 14, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      // ❌
      s.addImage({ data: icons.crossD, x: 5.2, y: y + 0.05, w: 0.25, h: 0.25 });
      s.addText(t.bad, {
        x: 5.5, y: y, w: 2.3, h: 0.3,
        fontSize: 11, color: C.danger, fontFace: FB, margin: 0
      });
      // ✅
      s.addImage({ data: icons.checkS, x: 7.85, y: y + 0.05, w: 0.25, h: 0.25 });
      s.addText(t.good, {
        x: 8.15, y: y, w: 2.0, h: 0.3,
        fontSize: 11, color: C.success, fontFace: FB, margin: 0
      });
    });
    drawFooter(s, 16, TOTAL);
  }

  // ============ Slide 17: 本讲作业 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.bg };
    drawHeader(s, "本讲作业", "Homework", "12 · 作业");
    const homeworks = [
      { num: "1", title: "注册域名", steps: "1. 用 AI 生成 10 个域名建议\n2. 在 Cloudflare 或阿里云注册\n3. 记录实际花费", icon: icons.searchA, color: C.primary },
      { num: "2", title: "选择主机方案", steps: "☑ 免主机（Notion / Framer）\n☑ 共享主机（SiteGround / 阿里云）\n☑ 云服务器", icon: icons.serverP, color: C.secondary },
      { num: "3", title: "完成域名解析", steps: "按照教程，把域名指向你的主机\n（如果适用的话）", icon: icons.routeA, color: C.accent }
    ];
    homeworks.forEach((hw, i) => {
      const x = 0.4 + i * 3.15;
      s.addShape("rect", {
        x: x, y: 1.3, w: 3.0, h: 3.5,
        fill: { color: C.white }, line: { color: C.border },
        shadow: { type: "outer", color: "000000", blur: 6, offset: 2, angle: 135, opacity: 0.08 }
      });
      s.addShape("rect", {
        x: x, y: 1.3, w: 3.0, h: 0.6,
        fill: { color: hw.color }, line: { color: hw.color }
      });
      s.addImage({ data: hw.icon, x: x + 0.2, y: 1.4, w: 0.4, h: 0.4 });
      s.addText("作业 " + hw.num, {
        x: x + 0.7, y: 1.45, w: 2.2, h: 0.3,
        fontSize: 12, color: C.white, fontFace: FH, bold: true, margin: 0
      });
      s.addText(hw.title, {
        x: x + 0.2, y: 2.1, w: 2.6, h: 0.5,
        fontSize: 18, color: C.text, fontFace: FH, bold: true, margin: 0
      });
      s.addText(hw.steps, {
        x: x + 0.2, y: 2.75, w: 2.6, h: 2.0,
        fontSize: 12, color: C.text, fontFace: FB, margin: 0
      });
    });
    // 底部 CTA
    s.addShape("rect", {
      x: 0.4, y: 4.85, w: 9.2, h: 0.45,
      fill: { color: C.deep }, line: { color: C.deep }
    });
    s.addImage({ data: icons.gradA, x: 0.6, y: 4.92, w: 0.3, h: 0.3 });
    s.addText("完成作业的同学，评论区告诉我你的域名，下期挑几个点评", {
      x: 1.0, y: 4.9, w: 8.5, h: 0.4,
      fontSize: 12, color: C.white, fontFace: FH, bold: true, valign: "middle", margin: 0
    });
    drawFooter(s, 17, TOTAL);
  }

  // ============ Slide 18: 收尾 ============
  {
    const s = pres.addSlide();
    s.background = { color: C.deep };
    // 左侧装饰
    s.addShape("rect", { x: 0, y: 0, w: 0.3, h: 5.625, fill: { color: C.accent }, line: { color: C.accent } });
    // 大图标
    s.addImage({ data: icons.rocketA, x: 0.8, y: 1.0, w: 1.5, h: 1.5 });
    s.addImage({ data: icons.checkW, x: 0.8, y: 2.6, w: 1.0, h: 1.0 });

    // 标题
    s.addText("本讲小结", {
      x: 3.0, y: 0.8, w: 6.5, h: 0.5,
      fontSize: 14, color: C.accent, fontFace: FH, bold: true, charSpacing: 4, margin: 0
    });
    s.addText("选对域名 + 主机，网站就成功一半", {
      x: 3.0, y: 1.3, w: 6.5, h: 0.9,
      fontSize: 30, color: C.white, fontFace: FH, bold: true, margin: 0
    });
    s.addShape("line", {
      x: 3.0, y: 2.3, w: 1.0, h: 0,
      line: { color: C.accent, width: 3 }
    });
    // 三个要点
    const points = [
      "用 AI 取名 · 选 .com",
      "主机 + 域名同一家",
      "HTTPS 必须开"
    ];
    points.forEach((p, i) => {
      const y = 2.6 + i * 0.55;
      s.addImage({ data: icons.checkW, x: 3.0, y: y, w: 0.3, h: 0.3 });
      s.addText(p, {
        x: 3.4, y: y - 0.05, w: 5, h: 0.4,
        fontSize: 16, color: C.white, fontFace: FH, bold: true, valign: "middle", margin: 0
      });
    });
    // 底部 CTA
    s.addShape("rect", {
      x: 3.0, y: 4.0, w: 6.5, h: 0.75,
      fill: { color: C.accent }, line: { color: C.accent }
    });
    s.addText("扫码加入训练营，免费试看前 3 讲", {
      x: 3.0, y: 4.0, w: 6.5, h: 0.75,
      fontSize: 16, color: C.deep, fontFace: FH, bold: true, align: "center", valign: "middle", margin: 0
    });
    s.addText("程序员晚枫 · 公众号：CoderWanFeng", {
      x: 3.0, y: 4.95, w: 6.5, h: 0.3,
      fontSize: 11, color: "94A3B8", fontFace: FB, align: "center", margin: 0
    });
  }

  await pres.writeFile({ fileName: "第4讲-域名与主机选择.pptx" });
  console.log("✅ PPT 生成成功");
}

build().catch(e => { console.error(e); process.exit(1); });