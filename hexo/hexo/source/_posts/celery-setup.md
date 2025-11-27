---
title: Celery讲解和入门案例
date: 2022-01-26 20:26:44
tags: [Linux,Celery]
---



<p align="center" id='进群-banner-AI'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/h0MExYJag6hLnQg26yx98w'>
    <img src="https://raw.gitcode.com/user-images/assets/5027920/87fc1ca4-1a6c-47b8-b234-3e323a1aa827/aiq.jpg" width="100%"/>
    </a>   
</p>

<p align="center">
	👉 <a target="_blank" href="https://www.python-office.com/">项目官网：https://www.python-office.com/</a> 👈
</p>
<p align="center">
	👉 <a target="_blank" href="http://www.python4office.cn/wechat-group/">本开源项目的交流群</a> 👈
</p>




<p align="center" name="gitcode">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
		<img src='https://gitcode.com/CoderWanFeng1/python-office/star/badge.svg?theme=dark' alt='gitcode star'/>
	</a>	
	<a target="_blank" href='https://gitcode.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/o98F_h_m6g4u5haPkbBtGg">
  <img src="https://img.shields.io/badge/学习-AI编程-red" alt="AI编程">
</a>
    	<a href="https://mp.weixin.qq.com/s/h0MExYJag6hLnQg26yx98w">
  <img src="https://img.shields.io/badge/加入-AI交流群-brightgreen" alt="AI交流群">
</a>

</p>




## Celery介绍

<!-- more -->


- 应用场景1：Web应用

  > 用户发送一个需要较长时间 处理的请求；
  > 传统思想会等待请求的结果（即常见到的转圈圈）；
  > 为了避免用户一直等待响应结果，在服务端可以通过异步的方式处理需要花费较长时间请求（例如调用外部服务API类似叮叮通知，邮件系统等）；
  > 服务后端创建相应的任务（创建任务是很快速的过程，执行具体任务才是真正耗时的操作），并将任务ID返回（响应）给用户；
  > 在前端看来，此次请求已经成功了，但是具体邮件是不是发成功了，没有直接给出结果，如果想看状态或结果，只需要拿到返回的任务ID再发送请求即可；
  > 用户可主动通过ID查看任务的执行进度，或通过前端轮询查看任务处理进度，常见的进度条就可以通过轮询实现；
  > 如果用户不关心邮件发送的结果，就直接该干嘛干嘛去了，不用再关心；
  > 如果需要动态监控任务状态及结果，从后台服务端看，任务结束后需要调用回调函数，将任务处理后的结果及数据进行转存或推送。

- 应用场景2：定时任务

  > 有一些业务场景可能需 要做定时任务，如定时发送邮件等

- 工作原理

![](/images/celery-setup/celery.png)

## Demo代码

#### 异步任务

```python
# celery_app_task.py：启动celery
import celery
import time

broker='redis://127.0.0.1:6379/11' #不加密码
backend = 'redis://127.0.0.1:6379/12'
# backend = 'redis://:Hx$hfcmsrx3@127.0.0.1:6379/11'
# broker = 'redis://:Hx$hfcmsrx3@127.0.0.1:6379/12'
cel = celery.Celery('tasks', backend=backend, broker=broker)


@cel.task
def add(x, y):
    return x + y
```

```python
# add_task.py：把任务加入celery
from celery_app_task import add
result = add.delay(9,5)
print(result.id)
```

```python
# query_result.py：查询任务的执行结果
from celery.result import AsyncResult
from celery_app_task import cel

async_run = AsyncResult(id="9ef26f34-a30e-433b-964a-348b7e2e4ab8", app=cel)

if async_run.successful():
    result = async_run.get()
    print(result)
    # result.forget() # 将结果删除
elif async_run.failed():
    print('执行失败')
elif async_run.status == 'PENDING':
    print('任务等待中被执行')
elif async_run.status == 'RETRY':
    print('任务异常后正在重试')
elif async_run.status == 'STARTED':
    print('任务已经开始被执行')
```

#### 定时任务


## Tips

启动命令：Linux和Win不一样，Celery对Win的支持不好

- Linux上的启动命令

    ```python
    celery -A celery_app_task worker  -l info
    ```



- Win上的启动命令

  ```python
  celery -A celery_app_task worker  -l info -P eventlet
  ```

Flower

启动命令
celery -A celery_app_task flower --address=127.0.0.1 --port=5566


## 参考链接

- [Celery - 简书 (jianshu.com)](https://www.jianshu.com/p/620052aadbff)
- [celery开发中踩的坑 - -零 - 博客园 (cnblogs.com)](https://www.cnblogs.com/-wenli/p/10960241.html)
- [ Celery入门与Flower监控](https://blog.csdn.net/u010784605/article/details/119042393?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~aggregatepage~first_rank_ecpm_v1~rank_v31_ecpm-2-119042393.pc_agg_new_rank&utm_term=celery+flower+启动&spm=1000.2123.3001.4430)
