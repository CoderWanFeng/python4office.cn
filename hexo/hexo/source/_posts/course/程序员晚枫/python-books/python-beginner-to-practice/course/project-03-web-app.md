---
title: 项目三 Web应用程序（学习笔记）
date: 2026-04-28 23:54:00
tags: [python,入门,课程,项目实战,Django]
cover: https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1200&auto=format&fit=crop
---


<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://www.python4office.cn/wechat-group/'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<!-- more -->
<p align="center">
    <img src="https://raw.atomgit.com/user-images/assets/5027920/a8bdeb7d-f6a8-4ad5-8020-e206055dd039/Python编程：从入门到实践_第3版__.png" alt="Python编程：从入门到实践（第3版）" width="400"/>
</p>
> 📖 **一起读书吧！** 加入《Python编程：从入门到实践》共读营 👉 [点击参加](https://mp.weixin.qq.com/s/ehe2vMrfAFscRLqbM9TF-g)



## 项目介绍

用 **Django** 开发一个完整的学习笔记网站——"Learning Log"！用户可以注册账号、创建学习主题、记录学习条目。

## 你将学会

- ✅ Django项目搭建 + App创建
- ✅ Topic 和 Entry 数据模型
- ✅ 用户注册、登录、登出（**第2版新增**）
- ✅ 创建、编辑、删除条目
- ✅ Bootstrap样式（**第2版更新到Bootstrap 5**）
- ✅ 部署上线（**第2版更新部署方式**）

**原书对应章节：第18-20章**

---

## 第1步：安装Django

```bash
pip install django
python -m django --version
```

## 第2步：创建项目和App

```bash
# 创建项目
django-admin startproject learning_log .

# 创建App
python manage.py startapp learning_logs
```

## 第3步：模型定义

```python
# learning_logs/models.py
from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """学习主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Entry(models.Model):
    """学习条目"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
```

运行迁移：

```bash
python manage.py makemigrations learning_logs
python manage.py migrate
```

## 第4步：Django管理后台

```python
# learning_logs/admin.py
from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
```

创建超级用户：

```bash
python manage.py createsuperuser
```

访问 `http://127.0.0.1:8000/admin/` 管理数据。

## 第5步：视图函数

```python
# learning_logs/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry

def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
```

## 第6步：用户认证（第2版新增）

```python
# users/views.py
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    context = {'form': form}
    return render(request, 'users/register.html', context)
```

## 第7步：URL配置

```python
# learning_log/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),
]
```

## 第8步：模板

```html
<!-- base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Learning Log</title>
    <!-- Bootstrap 5 -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
          rel="stylesheet">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="{% url 'learning_logs:index' %}">Learning Log</a>
        {% if user.is_authenticated %}
            <span class="navbar-text">Hello, {{ user.username }}</span>
        {% endif %}
    </nav>
    <div class="container mt-4">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

## 第9步：部署（Render/ Railway/ Fly.io）

第2版改用现代部署平台（如 Render）：

```bash
# requirements.txt
Django>=4.2
psycopg2-binary

# 构建命令
pip install -r requirements.txt
python manage.py collectstatic
```

> Django官方部署文档：[https://docs.djangoproject.com/en/stable/howto/deployment/](https://docs.djangoproject.com/en/stable/howto/deployment/)

---

## 项目文件结构

```
learning_log/
├── manage.py
├── requirements.txt
├── learning_log/          # 项目配置
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── learning_logs/         # 笔记App
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── users/                 # 用户App（第2版新增）
│   ├── __init__.py
│   ├── views.py
│   └── urls.py
└── templates/
    ├── base.html
    └── learning_logs/
        ├── index.html
        ├── topics.html
        └── topic.html
```

---

## 📚 官方文档参考

- [Django 官方文档](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) — 官方入门教程
- [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/) — 模型定义
- [Django Authentication](https://docs.djangoproject.com/en/stable/topics/auth/) — 用户认证系统
- [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/) — 模板系统

---

## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲](https://www.bilibili.com/cheese/play/ss982042944)