---
title: Python绘制冬奥吉祥物“冰墩墩”，源代码给你，复制粘贴就可以运行！(3D款)
date: 2022-02-10 10:45:09
tags: JavaScript
---

### 你好呀，我是[程序员晚枫](https://mp.weixin.qq.com/s/9hGurnWoFOaNwZKFoK_Vlw)
- 🐧 编程知识博主
- 👨‍💻 我的经历，点击查看👉[法学院毕业后转行Python程序员，现定居重庆，就职于某上市航空公司](https://www.bilibili.com/video/BV1uT4y1i7J8)
- 💬 我的微信，点击添加👉[CoderWanFeng](https://mp.weixin.qq.com/s/5eFJcon_yA0zdqjnxbSR1w)
- 💪 社区交流群👉[Python自动化办公社区 · 交流群](/wechat-group)

### 冰墩墩进阶款代码

> 👀 在线预览：[冰墩墩3D效果](https://dragonir.github.io/3d/#/olympic) （部署在 GitHub，加载速度可能会有点慢 😓）
>之前我们给大家分享过，如何部署自己的个人网站？👉[从0开始，搭建个人网站](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg3MDU3OTgxMg==&action=getalbum&album_id=2157699521936457730&scene=173&from_msgid=2247490481&from_itemidx=1&count=3&nolastread=1#wechat_redirect)

冰墩墩进阶款代码，主要通过JavaScript中的React框架来实现，
> 如需深入学习的同学，可以学习视频课程：[React 实战进阶 45 讲 - 掌握大厂热门的前端利器](http://gk.link/a/118LK)
> JavaScript通常搭配Python中的Django框架来使用：[Django快速开发实战 - 从开发到部署，掌握项目开发全流程](http://gk.link/a/10Wl1)

`实现代码如下`

```javascript
import React from 'react';
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { TWEEN } from "three/examples/jsm/libs/tween.module.min.js";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader";
import bingdundunModel from './models/bingdundun.glb';

<div>
  <div id="container"></div>
  {this.state.loadingProcess === 100 ? '' : (
    <div className="olympic_loading">
      <div className="box">{this.state.loadingProcess} %</div>
    </div>
  )}
</div>

container = document.getElementById('container');
renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
container.appendChild(renderer.domElement);
scene = new THREE.Scene();
scene.background = new THREE.TextureLoader().load(skyTexture);
camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 30, 100);
camera.lookAt(new THREE.Vector3(0, 0, 0));

// 直射光
const light = new THREE.DirectionalLight(0xffffff, 1);
light.intensity = 1;
light.position.set(16, 16, 8);
light.castShadow = true;
light.shadow.mapSize.width = 512 * 12;
light.shadow.mapSize.height = 512 * 12;
light.shadow.camera.top = 40;
light.shadow.camera.bottom = -40;
light.shadow.camera.left = -40;
light.shadow.camera.right = 40;
scene.add(light);
// 环境光
const ambientLight = new THREE.AmbientLight(0xcfffff);
ambientLight.intensity = 1;
scene.add(ambientLight);

const manager = new THREE.LoadingManager();
manager.onStart = (url, loaded, total) => {};
manager.onLoad = () => { console.log('Loading complete!')};
manager.onProgress = (url, loaded, total) => {
  if (Math.floor(loaded / total * 100) === 100) {
    this.setState({ loadingProcess: Math.floor(loaded / total * 100) });
    // 镜头补间动画
    Animations.animateCamera(camera, controls, { x: 0, y: -1, z: 20 }, { x: 0, y: 0, z: 0 }, 3600, () => {});
  } else {
    this.setState({ loadingProcess: Math.floor(loaded / total * 100) });
  }
};

var loader = new THREE.GLTFLoader(manager);
loader.load(landModel, function (mesh) {
  mesh.scene.traverse(function (child) {
    if (child.isMesh) {
      child.material.metalness = .1;
      child.material.roughness = .8;
      // 地面
      if (child.name === 'Mesh_2') {
        child.material.metalness = .5;
        child.receiveShadow = true;
      }
  });
  mesh.scene.rotation.y = Math.PI / 4;
  mesh.scene.position.set(15, -20, 0);
  mesh.scene.scale.set(.9, .9, .9);
  land = mesh.scene;
  scene.add(land);
});

loader.load(bingdundunModel, mesh => {
  mesh.scene.traverse(child => {
    if (child.isMesh) {
      // 内部
      if (child.name === 'oldtiger001') {
        child.material.metalness = .5
        child.material.roughness = .8
      }
      // 半透明外壳
      if (child.name === 'oldtiger002') {
        child.material.transparent = true;
        child.material.opacity = .5
        child.material.metalness = .2
        child.material.roughness = 0
        child.material.refractionRatio = 1
        child.castShadow = true;
      }
    }
  });
  mesh.scene.rotation.y = Math.PI / 24;
  mesh.scene.position.set(-8, -12, 0);
  mesh.scene.scale.set(24, 24, 24);
  scene.add(mesh.scene);
});
//绘制奥运五环
const fiveCycles = [
  { key: 'cycle_0', color: 0x0885c2, position: { x: -250, y: 0, z: 0 }},
  { key: 'cycle_1', color: 0x000000, position: { x: -10, y: 0, z: 5 }},
  { key: 'cycle_2', color: 0xed334e, position: { x: 230, y: 0, z: 0 }},
  { key: 'cycle_3', color: 0xfbb132, position: { x: -125, y: -100, z: -5 }},
  { key: 'cycle_4', color: 0x1c8b3c, position: { x: 115, y: -100, z: 10 }}
];
fiveCycles.map(item => {
  let cycleMesh = new THREE.Mesh(new THREE.TorusGeometry(100, 10, 10, 50), new THREE.MeshLambertMaterial({
    color: new THREE.Color(item.color),
    side: THREE.DoubleSide
  }));
  cycleMesh.castShadow = true;
  cycleMesh.position.set(item.position.x, item.position.y, item.position.z);
  meshes.push(cycleMesh);
  fiveCyclesGroup.add(cycleMesh);
});
fiveCyclesGroup.scale.set(.036, .036, .036);
fiveCyclesGroup.position.set(0, 10, -8);
scene.add(fiveCyclesGroup);
```

![](/images/拉勾/10大模板.jpg)