#!/usr/bin/env node

/**
 * 快速构建脚本 - 用于开发环境
 * 跳过压缩等耗时操作，加快构建速度
 */

const fs = require('fs');
const path = require('path');

// 配置文件路径
const configFile = path.join(__dirname, '_config.yml');

// 备份配置
function backupConfig() {
    const content = fs.readFileSync(configFile, 'utf8');
    fs.writeFileSync(configFile + '.backup', content);
    return content;
}

// 恢复配置
function restoreConfig() {
    const backupFile = configFile + '.backup';
    if (fs.existsSync(backupFile)) {
        const content = fs.readFileSync(backupFile, 'utf8');
        fs.writeFileSync(configFile, content);
        fs.unlinkSync(backupFile);
    }
}

// 创建快速配置
function createFastConfig(originalContent) {
    return originalContent
        .replace(/html_minifier:\s*enable:\s*true/g, 'html_minifier:\n  enable: false')
        .replace(/clean_css:\s*enable:\s*true/g, 'clean_css:\n  enable: false')
        .replace(/uglify:\s*enable:\s*true/g, 'uglify:\n  enable: false')
        .replace(/sitemap:/g, '# sitemap:')
        .replace(/baidusitemap:/g, '# baidusitemap:')
        .replace(/jsonContent:/g, '# jsonContent:');
}

// 主函数
async function main() {
    console.log('🚀 快速构建模式（跳过压缩）');
    console.log('----------------------------------------');

    try {
        // 备份并修改配置
        const originalContent = backupConfig();
        const fastConfig = createFastConfig(originalContent);
        fs.writeFileSync(configFile, fastConfig);
        console.log('✓ 配置已切换为快速模式');

        // 执行构建
        console.log('🔨 开始构建...');
        const { spawn } = require('child_process');
        await new Promise((resolve, reject) => {
            const build = spawn('npm', ['run', 'build'], {
                stdio: 'inherit',
                cwd: __dirname
            });

            build.on('close', (code) => {
                if (code === 0) {
                    resolve();
                } else {
                    reject(new Error(`构建失败，退出码: ${code}`));
                }
            });
        });

        console.log('✓ 构建完成');
        console.log('----------------------------------------');
        console.log('⚠️  警告：当前为快速构建模式，文件未压缩');
        console.log('💡 部署到生产环境前请使用完整构建: npm run build');
    } catch (error) {
        console.error('❌ 构建失败:', error.message);
        process.exit(1);
    } finally {
        // 恢复配置
        restoreConfig();
        console.log('✓ 配置已恢复');
    }
}

main();
