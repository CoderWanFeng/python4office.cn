---
title: Python绘制冬奥吉祥物“冰墩墩”，源代码给你，复制粘贴就可以运行！
date: 2022-02-09 17:06:19
tags: Turtle
---

### 你好呀，我是[程序员晚枫](http://www.python4office.cn/wechat-qrcode/)
- 🐧 编程知识博主
- 👨‍💻 我的B站，点击查看👉[千万别来重庆工作，别问为什么](https://www.bilibili.com/video/BV1aD4y1N7ai)
- 💬 我的微信，点击添加👉[python-office](http://www.python4office.cn/wechat-qrcode/)
- 💪 社区交流群👉[Python自动化办公社区 · 交流群](/wechat-group)
- 看到这里的朋友，记得加我哟，免费送你1套付费课程📕
### 冰墩墩基础款代码

> 温馨提示：本代码的运行，需要在电脑上，安装Python运行环境
还没安装的同学，可以查看：[详解 | Python&PyCharm的软件下载和安装](https://mp.weixin.qq.com/s/a0zoCo9DacvdpIoz1LEN3Q)

> 运行完代码，想继续学习Python的朋友，可以查看教程：[0基础学Python](http://gk.link/a/110jO)

```python
# coding=gbk
"""
公众号：Python图书馆
@时间  : 2022/2/8 14:28
免费 · Python学习群：http://www.python4office.cn/wechat-group/
     · Python学习资源：http://t.cn/A6ij6iXf
"""
import turtle as t

# 设置速度
t.speed(10000)  # 速度
t.delay(1)  # 延迟

t.title('冰墩墩')
# t.bgcolor('red')
# 双耳
# 左耳
t.penup()
t.goto(-150, 200)
t.setheading(160)
t.begin_fill()
t.pendown()
t.circle(-30, 230)
t.setheading(180)
t.circle(37, 90)
t.end_fill()
# 右耳
t.penup()
t.goto(60, 200)
t.setheading(20)
t.begin_fill()
t.pendown()
t.circle(30, 230)
t.setheading(0)
t.circle(-37, 90)
t.end_fill()
# 头
t.pensize(5)
t.penup()
t.goto(-113, 237)
t.setheading(30)
t.pendown()
t.circle(-134, 60)

t.penup()
t.goto(-150, 200)
t.setheading(-120)
t.pendown()
t.circle(200, 80)

t.penup()
t.goto(60, 200)
t.setheading(-60)
t.pendown()
t.circle(-200, 80)

t.penup()
t.setheading(210)
t.pendown()
t.circle(-120, 60)
# 双眼
# 左眼
# 眼圈
t.speed(10000)
t.penup()
t.goto(-140, 100)
t.setheading(-45)
t.begin_fill()
t.pendown()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.speed(10000)
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.1
        t.speed(10000)
        t.lt(3)
        t.fd(a)
t.end_fill()
# 眼白
t.fillcolor("white")
t.penup()
t.goto(-103, 125)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(14, 360)
t.end_fill()
# 眼珠
# t.fillcolor("sienna")
# t.pencolor("sienna")
t.penup()
t.goto(-102, 133)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(6, 360)
t.end_fill()
# 右眼
# 眼圈
# 办公神器：https://mp.weixin.qq.com/s/FMLw4RhStTvjgX0pXaDUNw
t.penup()
t.goto(50, 100)
t.setheading(45)
t.fillcolor("black")
t.pencolor("black")
t.begin_fill()
t.pendown()
a = 0.2
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.1
        t.speed(10000)
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.1
        t.speed(10000)
        t.lt(3)
        t.fd(a)
t.end_fill()
# 眼白
t.fillcolor("white")
t.penup()
t.goto(13, 125)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(14, 360)
t.end_fill()
# 眼珠
# 文件管理：https://mp.weixin.qq.com/s/IoTcorxmioGBZcXBRFXJwQ
# t.fillcolor("sienna")
# t.pencolor("sienna")
t.penup()
t.goto(12, 133)
t.setheading(0)
t.begin_fill()
t.pendown()
t.circle(6, 360)
t.end_fill()
# 鼻子
t.pencolor("black")
t.fillcolor("black")
t.penup()
t.goto(-55, 133)
t.begin_fill()
t.pendown()
t.fd(20)
t.seth(-120)
t.fd(20)
t.seth(120)
t.fd(20)
t.end_fill()
# 嘴
t.penup()
t.goto(-70, 110)
t.setheading(-30)
t.fillcolor("red")
t.begin_fill()
t.pendown()
t.circle(50, 60)
t.setheading(-120)
t.circle(-100, 15)
t.circle(-15, 90)
t.circle(-100, 15)
t.end_fill()
# 四肢
# 左臂
t.penup()
t.goto(-175, 100)
t.fillcolor("black")
t.begin_fill()
t.setheading(-120)
t.pendown()
t.fd(100)
t.setheading(-110)
t.circle(20, 180)
t.fd(30)
t.circle(-5, 160)
t.end_fill()
# 右臂
t.penup()
t.goto(85, 100)
t.setheading(60)
t.begin_fill()
t.pendown()
t.fd(100)
t.setheading(70)
t.circle(20, 180)
t.fd(30)
t.circle(-5, 160)
t.end_fill()
# 小红心
t.penup()
t.pencolor("red")
t.fillcolor('red')
t.goto(105, 200)
t.begin_fill()
t.pendown()
t.circle(-5, 180)
t.setheading(90)
t.circle(-5, 180)
t.setheading(-120)
t.fd(17)
t.penup()
t.goto(105, 200)
t.pendown()
t.setheading(-60)
t.fd(17)
t.end_fill()
t.pencolor("black")
t.fillcolor("black")
# 左腿
t.penup()
t.goto(-120, -45)
t.begin_fill()
t.pendown()
t.setheading(-90)
t.circle(-140, 20)
t.circle(5, 109)
t.fd(30)
t.circle(10, 120)
t.setheading(90)
t.circle(-140, 10)
t.end_fill()
# 右腿
t.penup()
t.goto(30, -45)
t.begin_fill()
t.pendown()
t.setheading(-90)
t.circle(140, 20)
t.circle(-5, 109)
t.fd(30)
t.circle(-10, 120)
t.setheading(90)
t.circle(140, 10)
t.end_fill()
# 冰糖外壳
t.pensize(3)
t.penup()
t.goto(-160, 195)
t.setheading(160)
t.pendown()
t.circle(-40, 230)
t.setheading(30)
t.circle(-134, 58)
t.setheading(60)
t.circle(-40, 215)
t.setheading(-60)
t.fd(15)
t.circle(2, 200)
t.setheading(65)
t.fd(30)
t.circle(-25, 180)
t.fd(100)
t.circle(2, 25)
t.circle(-200, 47)
t.circle(2, 60)
t.circle(140, 23)
t.circle(-2, 90)
t.setheading(180)
t.fd(70)
t.circle(-2, 90)
t.fd(30)
t.setheading(-160)
t.circle(-100, 35)
t.setheading(-90)
t.fd(30)
t.circle(-2, 90)
t.fd(70)
t.circle(-2, 90)
t.setheading(60)
t.circle(140, 30)
t.circle(2, 45)
t.circle(-200, 19)
t.circle(2, 130)
t.fd(30)
t.circle(-25, 180)
t.fd(100)
t.setheading(90)
t.circle(-200, 30)
# 冰糖面罩
t.pensize(3)
t.penup()
t.goto(65, 120)
t.setheading(90)
t.pendown()
t.pencolor("red")
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:  # 控制a的变化
        a = a + 0.25
        t.lt(3)  # 向左转3度
        t.fd(a)  # 向前走a的步长
    else:
        a = a - 0.25
        t.lt(3)
        t.fd(a)
t.pencolor("orange")
t.penup()
t.goto(66, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.255
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.255
        t.lt(3)
        t.fd(a)
t.pencolor("green")
t.penup()
t.goto(67, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.2555
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.2555
        t.lt(3)
        t.fd(a)
t.pencolor("deep sky blue")
t.penup()
t.goto(68, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.25955
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.25955
        t.lt(3)
        t.fd(a)
t.pencolor("pink")
t.penup()
t.goto(71, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.26
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.26
        t.lt(3)
        t.fd(a)
t.pencolor("purple")
t.penup()
t.goto(72, 120)
t.pendown()
a = 1
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.269
        t.lt(3)
        t.fd(a)
    else:
        a = a - 0.269
        t.lt(3)
        t.fd(a)

# 五环
t.penup()
t.goto(-55, -10)
t.pendown()
t.pencolor("blue")
t.circle(10)
t.penup()
t.goto(-40, -10)
t.pendown()
t.pencolor("black")
t.circle(10)
t.penup()
t.goto(-25, -10)
t.pendown()
t.pencolor("red")
t.circle(10)
t.penup()
t.goto(-50, -20)
t.pendown()
t.pencolor("yellow")
t.circle(10)
t.penup()
t.goto(-30, -20)
t.pendown()
t.pencolor("green")
t.circle(10)

# 输出文字
printer = t.Turtle()
printer.hideturtle()
printer.penup()
printer.goto(-350,-50)
printer.write("程\n\n",move = True, align="left", font=('宋体',40,'normal'))
printer.goto(-350,-100)
printer.write("序\n\n",move = True, align="left", font=('宋体',40,'normal'))
printer.goto(-350,-150)
printer.write("员\n\n",move = True, align="left", font=('宋体',40,'normal'))
printer.goto(-350,-200)
printer.write("晚\n\n",move = True, align="left", font=('宋体',40,'normal'))
printer.goto(-350,-250)
printer.write("枫\n\n",move = True, align="left", font=('宋体',40,'normal'))
t.hideturtle()
t.done()

```

### 答疑与交流
![python-office](https://cos.python-office.com/wechat/qr-code.jpg)

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/j8C-AsOGGM43vA0hXoCawg)就能上手做AI项目。