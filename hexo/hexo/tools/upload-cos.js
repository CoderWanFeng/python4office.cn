'use strict'

process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'

const COS = require('cos-nodejs-sdk-v5')
const fs = require('fs')
const path = require('path')

const cos = new COS({
  SecretId: process.env.SecretId,
  SecretKey: process.env.SecretKey,
  parallel: 10,
  filesFileParallel: 20,
  multipartParallel: 20
})

const publicDir = path.join(__dirname, '..', 'public')
const bucket = 'python4office-cn-1300615378'
const region = 'ap-shanghai'

const files = []

function walkDir(dir) {
  if (!fs.existsSync(dir)) return
  fs.readdirSync(dir, { withFileTypes: true }).forEach(entry => {
    const full = path.join(dir, entry.name)
    if (entry.isDirectory()) {
      walkDir(full)
    } else {
      files.push(full)
    }
  })
}

walkDir(publicDir)

let uploaded = 0
let failed = 0
let count = 0
let lastLog = 0
const startTime = Date.now()

function uploadFile(filePath) {
  return new Promise((resolve) => {
    const key = path.relative(publicDir, filePath).replace(/\\/g, '/')
    cos.putObject({
      Bucket: bucket,
      Region: region,
      Key: key,
      Body: fs.createReadStream(filePath)
    }, (err) => {
      count++
      if (!err) uploaded++
      else failed++
      if (count - lastLog >= 1000) {
        lastLog = count
        const elapsed = ((Date.now() - startTime) / 1000).toFixed(1)
        console.log(`[${elapsed}s] ${count}/${files.length} | 上传 ${uploaded} | 失败 ${failed}`)
      }
      resolve()
    })
  })
}

async function run() {
  console.log(`[COS] 上传 ${files.length} 个文件...`)
  const promises = files.map(f => uploadFile(f))
  await Promise.all(promises)
  const total = ((Date.now() - startTime) / 1000).toFixed(1)
  console.log(`\n[COS] 完成！总耗时 ${total}s | 上传 ${uploaded} | 失败 ${failed}`)
  process.exit(failed > 0 ? 1 : 0)
}

run()