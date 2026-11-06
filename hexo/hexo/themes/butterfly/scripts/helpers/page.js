/**
 * Butterfly
 * @example
 *  page_description()
 *  cloudTags(source, minfontsize, maxfontsize, limit)
 */

'use strict'

const { stripHTML, escapeHTML, unescapeHTML, prettyUrls } = require('hexo-util')
const crypto = require('crypto')

hexo.extend.helper.register('page_description', function () {
  const { config, page } = this
  let description = page.description || page.content || page.title || config.description

  if (description) {
    description = escapeHTML(stripHTML(description).substring(0, 200)
      .trim()
    ).replace(/\n/g, ' ')
    return description
  }
})

hexo.extend.helper.register('cloudTags', function (options = {}) {
  const env = this
  let source = options.source
  const minfontsize = options.minfontsize
  const maxfontsize = options.maxfontsize
  const limit = options.limit
  const unit = options.unit || 'px'

  let result = ''
  if (limit > 0) {
    source = source.limit(limit)
  }

  const sizes = []
  source.sort('length').forEach(tag => {
    const { length } = tag
    if (sizes.includes(length)) return
    sizes.push(length)
  })

  const length = sizes.length - 1
  source.forEach(tag => {
    const ratio = length ? sizes.indexOf(tag.length) / length : 0
    const size = minfontsize + ((maxfontsize - minfontsize) * ratio)
    let style = `font-size: ${parseFloat(size.toFixed(2))}${unit};`
    const color = 'rgb(' + Math.floor(Math.random() * 201) + ', ' + Math.floor(Math.random() * 201) + ', ' + Math.floor(Math.random() * 201) + ')' // 0,0,0 -> 200,200,200
    style += ` color: ${color}`
    result += `<a href="${env.url_for(tag.path)}" style="${style}">${tag.name}</a>`
  })
  return result
})

hexo.extend.helper.register('urlNoIndex', function () {
  return prettyUrls(this.url, { trailing_index: false, trailing_html: false })
})

// 仅输出文章实际元信息，地址复用现有 canonical，不推导或改写 slug。
hexo.extend.helper.register('page_structured_data', function () {
  const { page, config } = this
  if (!page.__post) return ''
  const canonical = this.urlNoIndex()
  const headline = String(page.title || this._p('no_title'))
  const configuredAuthor = page.author || config.author
  const authorName = typeof configuredAuthor === 'string'
    ? configuredAuthor : (configuredAuthor && configuredAuthor.name) || config.author
  const article = {
    '@type': 'BlogPosting',
    '@id': canonical + '#article',
    url: canonical,
    mainEntityOfPage: { '@type': 'WebPage', '@id': canonical },
    headline,
    description: unescapeHTML(this.page_description() || ''),
    author: { '@type': 'Person', name: String(authorName || '') }
  }
  for (const [field, date] of [['datePublished', page.date], ['dateModified', page.updated]]) {
    if (date && typeof date.toISOString === 'function' && !isNaN(date.valueOf())) {
      article[field] = date.toISOString()
    }
  }
  if (typeof page.cover === 'string' && page.cover.trim()) {
    article.image = this.full_url_for(page.cover)
  }
  // 仅使用已有首页和当前文章，避免为目录虚构页面。
  const breadcrumb = {
    '@type': 'BreadcrumbList',
    '@id': canonical + '#breadcrumb',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: String(config.title), item: this.full_url_for('/') },
      { '@type': 'ListItem', position: 2, name: headline, item: canonical }
    ]
  }
  return JSON.stringify({ '@context': 'https://schema.org', '@graph': [article, breadcrumb] })
    .replace(/</g, '\\u003c').replace(/>/g, '\\u003e').replace(/&/g, '\\u0026')
    .replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029')
})

hexo.extend.helper.register('md5', function (path) {
  return crypto.createHash('md5').update(decodeURI(this.url_for(path))).digest('hex')
})

hexo.extend.helper.register('injectHtml', function (data) {
  let result = ''
  if (!data) return ''
  for (let i = 0; i < data.length; i++) {
    result += data[i]
  }
  return result
})
