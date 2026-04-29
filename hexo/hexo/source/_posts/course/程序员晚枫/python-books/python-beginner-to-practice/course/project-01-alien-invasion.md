---
title: 项目一 外星人入侵（游戏开发）
date: 2026-04-28 23:54:00
tags: [python,入门,课程,项目实战,Pygame]
cover: https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=1200&auto=format&fit=crop
---

<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<!-- more -->

## 项目介绍

用 Python 的 **Pygame** 库，开发一款完整的2D射击游戏——"外星人入侵"！第3版使用 **VS Code** 作为编辑器。

## 你将学会

- ✅ 安装Pygame + 创建游戏窗口
- ✅ 加载和绘制可移动的飞船
- ✅ 发射子弹
- ✅ 从屏幕上方涌来的外星人
- ✅ 碰撞检测（子弹击中外星人）
- ✅ 记分系统 + 游戏结束与重玩

**原书对应章节：第12-14章**

---

## 第1步：安装Pygame

```bash
pip install pygame
```

> Pygame官网：[https://www.pygame.org/](https://www.pygame.org/) — 封装了SDL，专注2D游戏开发。

## 第2步：创建游戏窗口

```python
# alien_invasion.py
import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("外星人入侵")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()

run_game()
```

## 第3步：用Settings类管理配置

```python
# settings.py
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 3
        self.bullet_speed = 5
        self.alien_speed = 1
```

## 第4步：飞船类

```python
# ship.py
import pygame

class Ship:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
```

## 第5步：子弹类

```python
# bullet.py
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.color = ai_settings.bullet_color
        self.speed = ai_settings.bullet_speed

    def update(self):
        self.rect.y -= self.speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
```

## 第6步：外星人类 + 碰撞检测

```python
# alien.py
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

# 碰撞检测（用pygame.sprite.Group）
from pygame.sprite import Group

bullets = Group()
aliens = Group()

collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
```

## 项目文件结构

```
alien_invasion/
├── alien_invasion.py   # 主程序
├── settings.py         # 游戏设置
├── ship.py             # 飞船
├── bullet.py           # 子弹
├── alien.py            # 外星人
├── game_stats.py       # 游戏统计（分数）
├── button.py           # Play按钮
└── images/             # 资源图片
    ├── ship.bmp
    └── alien.bmp
```

> 💡 VS Code中，`images/` 目录放在项目根目录下，与 `.py` 文件平级。

---

## 📚 官方文档参考

- [pygame 官方文档](https://www.pygame.org/docs/)
- [pygame.sprite — Sprite base class](https://www.pygame.org/docs/ref/sprite.html) — 碰撞检测核心
- [pygame.event — Event handling](https://www.pygame.org/docs/ref/event.html) — 键盘事件
- [pygame.display — Display Surface](https://www.pygame.org/docs/ref/display.html) — 窗口管理
- [9. Classes](https://docs.python.org/3/tutorial/classes.html) — 本项目大量使用类

---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲](https://www.bilibili.com/cheese/play/ss982042944)