'use strict';

/**
 * 只在文章渲染上下文补充缺失的 description，不修改源文件或正文。
 * 人工摘要不受长度、重复检查影响；自动摘要从渲染后的正文提取，
 * 排除广告、徽章、代码块和问候语，不用编号制造唯一性。
 */
const cheerio = require('cheerio');

function cleanText(text) {
  return String(text || '')
    .replace(/https?:\/\/[^\s<>]+/gi, ' ')
    .replace(/[\u200B\uFEFF]/g, '')
    .replace(/\s+/g, ' ').trim()
    .replace(/^(?:大家好|各位好|你好)[，,！!\s]*(?:我是[^。！!]*[。！!]\s*)?/, '')
    .trim();
}

function extractFirstMeaningfulText(body) {
  const $ = cheerio.load(String(body || ''));
  $('script,style,noscript,iframe,svg,img,picture,video,audio,pre,figure,nav,header,footer,form,h1,h2,h3,h4,h5,h6').remove();
  $('[class],[id]').each((_, node) => {
    const marker = `${$(node).attr('class') || ''} ${$(node).attr('id') || ''}`;
    if (/(?:^|\s)(?:promo(?:-[\w-]+)?|ad(?:s|vertisement)?|badge|toc)(?:\s|$)/i.test(marker)) $(node).remove();
  });
  $('br').replaceWith(' ');
  const blocks = $('p,li').toArray().filter(node => !$(node).find('p,li').length);
  const texts = [];
  for (const node of blocks) {
    const text = cleanText($(node).text());
    const links = cleanText($(node).find('a').text());
    if (!text || text === links || /(?:扫码|扫描二维码|添加.{0,8}微信|加入.{0,8}群|领取.{0,8}资料|关注.{0,8}公众号)/.test(text)) continue;
    texts.push(text);
    if (Array.from(texts.join(' ')).length >= 160) break;
  }
  // 无段落标签的纯文本仍可使用；仅图片或推广内容回退到文章标题。
  if (!blocks.length) return cleanText($.root().text());
  return texts.join(' ');
}

function generateDescription(post) {
  const text = extractFirstMeaningfulText(post.content);
  return truncate(text || String(post.title || ''), 160);
}

function truncate(str, max) {
  const chars = Array.from(str);
  if (chars.length <= max) return str;
  return chars.slice(0, max - 1).join('').trimEnd() + '…';
}

hexo.extend.filter.register('template_locals', function (locals) {
  const page = locals.page;
  if (page && page.__post && !String(page.description || '').trim()) {
    page.description = generateDescription(page);
  }
  return locals;
});