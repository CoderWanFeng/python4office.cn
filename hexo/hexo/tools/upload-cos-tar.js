'use strict'

process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'

const COS = require('cos-nodejs-sdk-v5')
const fs = require('fs')
const path = require('path')

const cos = new COS({
  SecretId: process.env.SecretId,
  SecretKey: process.env.SecretKey
})

const publicDir = path.join(__dirname, '..', 'public')
const tarPath = '/tmp/public.tar.gz'
const bucket = 'python4office-cn-1300615378'
const region = 'ap-shanghai'

const startTime = Date.now()

console.log('[COS] 上传 tar 包...')

const fileSize = fs.statSync(tarPath).size
console.log(`[COS] 文件大小: ${(fileSize / 1024 / 1024).toFixed(1)} MB`)

const fileStream = fs.createReadStream(tarPath)

cos.putObject({
  Bucket: bucket,
  Region: region,
  Key: 'public.tar.gz',
  Body: fileStream,
  ContentLength: fileSize
}, (err, data) => {
  const total = ((Date.now() - startTime) / 1000).toFixed(1)
  if (err) {
    console.error(`[COS] 上传失败: ${err.message}`)
    process.exit(1)
  }
  console.log(`[COS] 上传完成！耗时 ${total}s`)
  console.log('[COS] 需要在远程解压到 public/ 目录')
  process.exit(0)
})