// 阅读进度条功能
function initReadingProgress() {
    // 创建进度条元素
    const progressBar = document.createElement('div');
    progressBar.id = 'reading-progress';
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        z-index: 9999;
        width: 0%;
        transition: width 0.2s ease;
    `;
    document.body.appendChild(progressBar);

    // 监听滚动事件
    window.addEventListener('scroll', updateReadingProgress);

    function updateReadingProgress() {
        const totalHeight = document.body.scrollHeight - window.innerHeight;
        const progress = (window.pageYOffset / totalHeight) * 100;
        progressBar.style.width = `${progress}%`;
    }
}

export default {
    init: initReadingProgress
};