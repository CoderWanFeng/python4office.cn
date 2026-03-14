// 样式
import '../css/main.scss'
// 上报
import './report'
// 图片查看器
import Viewer from './viewer'
// 分享
import Share from './share'
// 边缘
import Aside from './aside'
// 阅读进度条
import Progress from './progress'

import {addLoadEvent} from './util'
import util from './util'

// 平滑滚动功能
function initSmoothScroll() {
    // 为所有内部链接添加平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = this.getAttribute('href');
            util.smoothScroll(target);
        });
    });
}

addLoadEvent(function() {
    Share.init()
    Viewer.init()
    Aside.init()
    initSmoothScroll()
    Progress.init()
})
