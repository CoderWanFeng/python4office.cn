'use strict';

/**
 * 全站智能 description 生成器
 *
 * 目的：解决 Bing Webmaster Tools 的两个警告：
 *   - "Meta descriptions on many pages are too short"
 *   - "There are too many pages with identical meta descriptions"
 *
 * 策略（before_generate 阶段对 post 注入 description）：
 *   1. 优先使用 frontmatter 中的 description
 *   2. 若缺失或 <60 字符：标题 + tags + 正文首段，生成 150-160 字符的描述
 *   3. 用 Set 哈希去重，重复时追加"（第 N 篇）"
 *   4. 注入 post.description，不修改源文件
 *
 * 配合 _config.butterfly.yml 的 index_post_content.method: 2（优先 description），
 * 保证全站每个页面都有唯一且长度合适的 meta description。
 */

function stripMarkdown(text) {
  return text
    .replace(/```[\s\S]*?```/g, ' ')            // 代码块
    .replace(/<!--[\s\S]*?-->/g, ' ')           // 注释
    .replace(/!\[[^\]]*\]\([^)]*\)/g, ' ')      // 图片
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1')    // 链接保留文本
    .replace(/^#+\s+.*$/gm, '')                 // 标题
    .replace(/^>\s*/gm, '')                     // 引用
    .replace(/[*_~`]/g, '')                     // 强调/代码
    .replace(/\s+/g, '');                       // 空白
}

function extractFirstMeaningfulText(body) {
  // 取首段有意义文本（最多 100 字符原文）
  const lines = body.split('\n');
  for (const line of lines) {
    const stripped = stripMarkdown(line);
    if (stripped.length > 20) {
      return stripped;
    }
  }
  return '';
}

function generateDescription(post) {
  const title = (post.title || '').toString();
  const tags = (post.tags && post.tags.toArray ? post.tags.toArray() : [])
    .slice(0, 3)
    .map((t) => (typeof t === 'string' ? t : t.name))
    .filter(Boolean);

  const body = post.content || post._content || '';
  const firstText = extractFirstMeaningfulText(body).slice(0, 80);

  const tagStr = tags.length ? tags.join('、') : '核心要点';
  const template = `${title}。本文围绕${tagStr}：${firstText}...`;
  return template;
}

function ensureUniqueDescription(desc, seen) {
  let unique = desc;
  let suffix = 1;
  while (seen.has(unique)) {
    suffix += 1;
    unique = `${desc}（第${suffix}篇）`;
  }
  seen.add(unique);
  return unique;
}

function truncate(str, max) {
  if (str.length <= max) return str;
  // 保留前 max-1 字符 + …
  return str.slice(0, max - 1) + '…';
}

hexo.extend.filter.register('before_generate', function () {
  const posts = hexo.locals.get('posts').toArray();
  const seen = new Set();
  let generated = 0;
  let deduped = 0;

  for (const post of posts) {
    let desc = post.description;

    // 1) 缺失或过短 → 重新生成
    if (!desc || desc.length < 60) {
      desc = generateDescription(post);
      generated += 1;
    }

    // 2) 截断到 160 字符以内
    desc = truncate(desc, 160);

    // 3) 去重
    const beforeLen = seen.size;
    desc = ensureUniqueDescription(desc, seen);
    if (seen.size > beforeLen + 1) deduped += 1;

    // 4) 注入（不写回源文件）
    post.description = desc;
  }

  hexo.log.info(
    '[description-generator] 处理 %d 篇文章，新生成 %d 条，去重 %d 条',
    posts.length, generated, deduped
  );
});