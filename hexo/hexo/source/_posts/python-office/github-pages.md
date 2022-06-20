---
title: github-pages是如何搭建的？
date: 2022-05-31 18:54:16
tags: 
---

<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>python-office</title>
    <meta name="generator" content="VuePress 1.9.7">
    
    <meta name="description" content="python-office自动化办公">
    
    <link rel="preload" href="./assets/css/0.styles.1306b68e.css" as="style"><link rel="preload" href="./assets/js/app.fa7e33e2.js" as="script"><link rel="preload" href="./assets/js/2.a1d55f4d.js" as="script"><link rel="preload" href="./assets/js/7.9bf69f72.js" as="script"><link rel="prefetch" href="./assets/js/10.1d308212.js"><link rel="prefetch" href="./assets/js/11.9673df9c.js"><link rel="prefetch" href="./assets/js/12.1b7b91fd.js"><link rel="prefetch" href="./assets/js/13.633f88fa.js"><link rel="prefetch" href="./assets/js/14.2697ab47.js"><link rel="prefetch" href="./assets/js/15.14996e55.js"><link rel="prefetch" href="./assets/js/16.a6af27f4.js"><link rel="prefetch" href="./assets/js/17.d4666eae.js"><link rel="prefetch" href="./assets/js/18.0c525901.js"><link rel="prefetch" href="./assets/js/19.76d292a7.js"><link rel="prefetch" href="./assets/js/20.25794adc.js"><link rel="prefetch" href="./assets/js/21.1d358792.js"><link rel="prefetch" href="./assets/js/22.22a1e7a4.js"><link rel="prefetch" href="./assets/js/23.b3205f27.js"><link rel="prefetch" href="./assets/js/24.2998f611.js"><link rel="prefetch" href="./assets/js/3.0c893207.js"><link rel="prefetch" href="./assets/js/4.2e5a36eb.js"><link rel="prefetch" href="./assets/js/5.06e1c49b.js"><link rel="prefetch" href="./assets/js/6.5ec218b2.js"><link rel="prefetch" href="./assets/js/8.bcfd2372.js"><link rel="prefetch" href="./assets/js/9.f93ddc75.js">
    <link rel="stylesheet" href="./assets/css/0.styles.1306b68e.css">
  </head>
  <body>
    <div id="app" data-server-rendered="true"><div class="theme-container no-sidebar"><header class="navbar"><div class="sidebar-button"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" viewBox="0 0 448 512" class="icon"><path fill="currentColor" d="M436 124H12c-6.627 0-12-5.373-12-12V80c0-6.627 5.373-12 12-12h424c6.627 0 12 5.373 12 12v32c0 6.627-5.373 12-12 12zm0 160H12c-6.627 0-12-5.373-12-12v-32c0-6.627 5.373-12 12-12h424c6.627 0 12 5.373 12 12v32c0 6.627-5.373 12-12 12zm0 160H12c-6.627 0-12-5.373-12-12v-32c0-6.627 5.373-12 12-12h424c6.627 0 12 5.373 12 12v32c0 6.627-5.373 12-12 12z"></path></svg></div> <a href="/./" aria-current="page" class="home-link router-link-exact-active router-link-active"><!----> <span class="site-name">python-office</span></a> <div class="links"><div class="search-box"><input aria-label="Search" autocomplete="off" spellcheck="false" value=""> <!----></div> <nav class="nav-links can-hide"><div class="nav-item"><a href="/./" aria-current="page" class="nav-link router-link-exact-active router-link-active">
  主页
</a></div><div class="nav-item"><a href="http://www.python4office.cn/wechat-group/" target="_blank" rel="noopener noreferrer" class="nav-link external">
  交流群
  <span><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" x="0px" y="0px" viewBox="0 0 100 100" width="15" height="15" class="icon outbound"><path fill="currentColor" d="M18.8,85.1h56l0,0c2.2,0,4-1.8,4-4v-32h-8v28h-48v-48h28v-8h-32l0,0c-2.2,0-4,1.8-4,4v56C14.8,83.3,16.6,85.1,18.8,85.1z"></path> <polygon fill="currentColor" points="45.7,48.7 51.3,54.3 77.2,28.5 77.2,37.2 85.2,37.2 85.2,14.9 62.8,14.9 62.8,22.9 71.5,22.9"></polygon></svg> <span class="sr-only">(opens new window)</span></span></a></div><div class="nav-item"><a href="https://www.bilibili.com/video/BV1pT4y1k7FH" target="_blank" rel="noopener noreferrer" class="nav-link external">
  视频教程
  <span><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" x="0px" y="0px" viewBox="0 0 100 100" width="15" height="15" class="icon outbound"><path fill="currentColor" d="M18.8,85.1h56l0,0c2.2,0,4-1.8,4-4v-32h-8v28h-48v-48h28v-8h-32l0,0c-2.2,0-4,1.8-4,4v56C14.8,83.3,16.6,85.1,18.8,85.1z"></path> <polygon fill="currentColor" points="45.7,48.7 51.3,54.3 77.2,28.5 77.2,37.2 85.2,37.2 85.2,14.9 62.8,14.9 62.8,22.9 71.5,22.9"></polygon></svg> <span class="sr-only">(opens new window)</span></span></a></div><div class="nav-item"><a href="https://github.com/CoderWanFeng/python-office" target="_blank" rel="noopener noreferrer" class="nav-link external">
  GitHub
  <span><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" x="0px" y="0px" viewBox="0 0 100 100" width="15" height="15" class="icon outbound"><path fill="currentColor" d="M18.8,85.1h56l0,0c2.2,0,4-1.8,4-4v-32h-8v28h-48v-48h28v-8h-32l0,0c-2.2,0-4,1.8-4,4v56C14.8,83.3,16.6,85.1,18.8,85.1z"></path> <polygon fill="currentColor" points="45.7,48.7 51.3,54.3 77.2,28.5 77.2,37.2 85.2,37.2 85.2,14.9 62.8,14.9 62.8,22.9 71.5,22.9"></polygon></svg> <span class="sr-only">(opens new window)</span></span></a></div> <!----></nav></div></header> <div class="sidebar-mask"></div> <aside class="sidebar"><nav class="nav-links"><div class="nav-item"><a href="/./" aria-current="page" class="nav-link router-link-exact-active router-link-active">
  主页
</a></div><div class="nav-item"><a href="http://www.python4office.cn/wechat-group/" target="_blank" rel="noopener noreferrer" class="nav-link external">
  交流群
  <span><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" x="0px" y="0px" viewBox="0 0 100 100" width="15" height="15" class="icon outbound"><path fill="currentColor" d="M18.8,85.1h56l0,0c2.2,0,4-1.8,4-4v-32h-8v28h-48v-48h28v-8h-32l0,0c-2.2,0-4,1.8-4,4v56C14.8,83.3,16.6,85.1,18.8,85.1z"></path> <polygon fill="currentColor" points="45.7,48.7 51.3,54.3 77.2,28.5 77.2,37.2 85.2,37.2 85.2,14.9 62.8,14.9 62.8,22.9 71.5,22.9"></polygon></svg> <span class="sr-only">(opens new window)</span></span></a></div><div class="nav-item"><a href="https://www.bilibili.com/video/BV1pT4y1k7FH" target="_blank" rel="noopener noreferrer" class="nav-link external">
  视频教程
  <span><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" x="0px" y="0px" viewBox="0 0 100 100" width="15" height="15" class="icon outbound"><path fill="currentColor" d="M18.8,85.1h56l0,0c2.2,0,4-1.8,4-4v-32h-8v28h-48v-48h28v-8h-32l0,0c-2.2,0-4,1.8-4,4v56C14.8,83.3,16.6,85.1,18.8,85.1z"></path> <polygon fill="currentColor" points="45.7,48.7 51.3,54.3 77.2,28.5 77.2,37.2 85.2,37.2 85.2,14.9 62.8,14.9 62.8,22.9 71.5,22.9"></polygon></svg> <span class="sr-only">(opens new window)</span></span></a></div><div class="nav-item"><a href="https://github.com/CoderWanFeng/python-office" target="_blank" rel="noopener noreferrer" class="nav-link external">
  GitHub
  <span><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" x="0px" y="0px" viewBox="0 0 100 100" width="15" height="15" class="icon outbound"><path fill="currentColor" d="M18.8,85.1h56l0,0c2.2,0,4-1.8,4-4v-32h-8v28h-48v-48h28v-8h-32l0,0c-2.2,0-4,1.8-4,4v56C14.8,83.3,16.6,85.1,18.8,85.1z"></path> <polygon fill="currentColor" points="45.7,48.7 51.3,54.3 77.2,28.5 77.2,37.2 85.2,37.2 85.2,14.9 62.8,14.9 62.8,22.9 71.5,22.9"></polygon></svg> <span class="sr-only">(opens new window)</span></span></a></div> <!----></nav>  <ul class="sidebar-links"><li><a href="/./" aria-current="page" class="active sidebar-link">Home</a></li><li><section class="sidebar-group collapsable depth-0"><p class="sidebar-heading"><span>入门指南</span> <span class="arrow right"></span></p> <!----></section></li><li><section class="sidebar-group collapsable depth-0"><p class="sidebar-heading"><span>核心功能</span> <span class="arrow right"></span></p> <!----></section></li><li><section class="sidebar-group collapsable depth-0"><p class="sidebar-heading"><span>相关文档</span> <span class="arrow right"></span></p> <!----></section></li><li><section class="sidebar-group collapsable depth-0"><p class="sidebar-heading"><span>常见问题</span> <span class="arrow right"></span></p> <!----></section></li></ul> </aside> <main aria-labelledby="main-title" class="home"><header class="hero"><img src="http://python4office.cn/images/github-nav.jpg" alt="hero"> <h1 id="main-title">
      Welcome to python-office
    </h1> <p class="description">
      为自动化办公而生
    </p> <p class="action"><a href="/./guide/introduction.html" class="nav-link action-button">
  开始使用 →
</a></p></header> <div class="features"><div class="feature"><h2>专注一个领域</h2> <p>Python-office 是一个 Python 自动化办公第三方库，能解决大部分自动化办公的问题。</p></div><div class="feature"><h2>降低学习门槛</h2> <p>不用学习Python编程知识，会电脑操作就行</p></div><div class="feature"><h2>一行代码</h2> <p>实现自动化办公，做到开箱即用</p></div></div> <div class="theme-default-content custom content__default"></div> <div class="footer">
    Hep Licensed | Copyright © 2022-present 程序员晚枫
  </div></main></div><div class="global-ui"><!----></div></div>
    <script src="./assets/js/app.fa7e33e2.js" defer></script><script src="./assets/js/2.a1d55f4d.js" defer></script><script src="./assets/js/7.9bf69f72.js" defer></script>
  </body>
</html>
