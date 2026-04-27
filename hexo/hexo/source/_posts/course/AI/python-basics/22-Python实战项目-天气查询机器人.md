---
title: Python实战项目：我做了个天气查询机器人，每天自动推送天气提醒
date: 2026-02-28 21:11:00
tags: [Python实战, API, 天气, 自动化]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw'>
    <img src="https://raw.atomgit.com/user-images/assets/5027920/9f01d0e8-11e1-4a88-9528-b3d3dd354bc3/TuLing.jpg" />
    </a>   
</p>

<p align="center" name="atomgit">
    <a target="_blank" href='https://github.com/CoderWanFeng/python-office'>
    <img src="https://img.shields.io/github/stars/CoderWanFeng/python-office.svg?style=social" alt="github star"/>
    </a>
    	<a target="_blank" href='https://gitee.com/CoderWanFeng//python-office/'>
		<img src='https://gitee.com/CoderWanFeng//python-office/badge/star.svg?theme=dark' alt='gitee star'/>
	</a>
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
		<img src='https://atomgit.com/CoderWanFeng1/python-office/star/2025top.svg?theme=dark' alt='atomgit star'/>
	</a>	
	<a target="_blank" href='https://atomgit.com/CoderWanFeng1/python-office'>
<img src="https://static.pepy.tech/badge/python-office" alt="PyPI Downloads">
</a>
<a href="https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

你有没有这样的经历？早上急匆匆出门，到了公司才发现——今天降温了没带外套、下雨了没带伞、紫外线很强没涂防晒……如果能有人每天早上提醒你该穿什么、带什么，该多好。

> 💡 **场景**：每天出门前都要查天气，与其手动打开APP看，不如让Python自动查！查完还能给你穿衣建议——"今天有雨，记得带伞！""降温8度，穿厚点！"

这个项目是我给自己写的第一个实用Python项目，用了2年多了，每天早上7:30准时推送，一次都没断过。今天把代码分享给你。

这个项目会教你：
- 如何调用第三方API
- 如何处理JSON数据
- 如何根据天气给出智能建议
- 如何集成到微信/钉钉机器人

---

## 项目功能

- 查询指定城市的实时天气
- 获取未来3天预报
- 根据天气给出穿衣、出行建议
- 空气质量提醒
- 可集成到微信/钉钉机器人

---

## 准备工作

需要注册一个天气API。推荐选择：

| API | 特点 | 免费额度 | 推荐指数 |
|-----|------|---------|---------|
| [和风天气](https://www.qweather.com/) | 国内数据准，文档好 | 1000次/天 | ⭐⭐⭐⭐⭐ |
| [心知天气](https://www.seniverse.com/) | 简单易用 | 300次/天 | ⭐⭐⭐⭐ |
| [OpenWeatherMap](https://openweathermap.org/) | 国际通用 | 1000次/天 | ⭐⭐⭐ |

> 💡 **注册流程**：注册 → 获取API Key → 开始调用。以和风天气为例，注册后在控制台就能看到你的Key。

### requests库安装

```bash
pip install requests
```

---

## 完整代码（以和风天气为例）

```python
import requests
import json
from datetime import datetime

class WeatherBot:
    def __init__(self, api_key):
        self.api_key = api_key
        # 和风天气API
        self.url_current = "https://devapi.qweather.com/v7/weather/now"
        self.url_forecast = "https://devapi.qweather.com/v7/weather/3d"
        self.url_air = "https://devapi.qweather.com/v7/air/now"
        # 城市ID缓存（避免重复查询）
        self.city_cache = {}
    
    def get_city_id(self, city_name):
        """根据城市名获取城市ID（和风天气需要城市ID）"""
        if city_name in self.city_cache:
            return self.city_cache[city_name]
        
        # 常用城市ID映射
        city_map = {
            "北京": "101010100",
            "上海": "101020100",
            "广州": "101280101",
            "深圳": "101280601",
            "重庆": "101040100",
            "成都": "101270101",
            "杭州": "101210101",
            "武汉": "101200101",
            "南京": "101190101",
            "西安": "101110101",
        }
        
        if city_name in city_map:
            self.city_cache[city_name] = city_map[city_name]
            return city_map[city_name]
        
        # 查询城市ID
        url = "https://geoapi.qweather.com/v2/city/lookup"
        params = {'location': city_name, 'key': self.api_key}
        try:
            resp = requests.get(url, params=params, timeout=5)
            data = resp.json()
            if data.get('code') == '200' and data.get('location'):
                city_id = data['location'][0]['id']
                self.city_cache[city_name] = city_id
                return city_id
        except Exception as e:
            print(f"查询城市ID失败：{e}")
        
        # 直接用城市名作为location（和风天气也支持）
        return city_name
    
    def get_weather(self, city):
        """获取当前天气"""
        city_id = self.get_city_id(city)
        params = {
            'location': city_id,
            'key': self.api_key,
            'unit': 'm'  # 摄氏度
        }
        
        try:
            resp = requests.get(self.url_current, params=params, timeout=5)
            data = resp.json()
            
            if data.get('code') == '200':
                return self._format_current(data, city)
            else:
                return f"查询失败：错误码 {data.get('code')}"
        except requests.Timeout:
            return "❌ 请求超时，请检查网络"
        except requests.ConnectionError:
            return "❌ 网络连接失败"
        except Exception as e:
            return f"❌ 查询出错：{e}"
    
    def get_forecast(self, city):
        """获取天气预报"""
        city_id = self.get_city_id(city)
        params = {
            'location': city_id,
            'key': self.api_key
        }
        
        try:
            resp = requests.get(self.url_forecast, params=params, timeout=5)
            data = resp.json()
            
            if data.get('code') == '200':
                return self._format_forecast(data, city)
            else:
                return f"查询失败：错误码 {data.get('code')}"
        except Exception as e:
            return f"❌ 查询出错：{e}"
    
    def get_air_quality(self, city):
        """获取空气质量"""
        city_id = self.get_city_id(city)
        params = {
            'location': city_id,
            'key': self.api_key
        }
        
        try:
            resp = requests.get(self.url_air, params=params, timeout=5)
            data = resp.json()
            
            if data.get('code') == '200':
                return self._format_air(data, city)
            else:
                return None
        except:
            return None
    
    def _format_current(self, data, city):
        """格式化当前天气"""
        now = data['now']
        temp = now['temp']          # 温度
        feels = now['feelsLike']    # 体感温度
        hum = now['humidity']       # 湿度
        wind = now['windSpeed']     # 风速
        wind_dir = now['windDir']   # 风向
        weather = now['text']       # 天气状况
        vis = now['vis']            # 能见度
        
        # 温度预警
        temp_diff = int(feels) - int(temp)
        temp_notice = ""
        if temp_diff <= -3:
            temp_notice = f"（体感比实际低{abs(temp_diff)}度，注意保暖！）"
        elif temp_diff >= 3:
            temp_notice = f"（体感比实际高{temp_diff}度）"
        
        report = f"""
🌍 {city} 当前天气
━━━━━━━━━━━━━━━━━━
🌡️ 温度: {temp}°C (体感{feels}°C){temp_notice}
☁️ 天气: {weather}
💧 湿度: {hum}%
💨 风速: {wind}km/h {wind_dir}
👁️ 能见度: {vis}km

💡 {self._get_advice(temp, weather, hum)}
"""
        return report
    
    def _format_forecast(self, data, city):
        """格式化预报"""
        daily = data['daily']
        
        result = f"\n🌍 {city} 未来3天预报\n━━━━━━━━━━━━━━━━━━\n"
        
        for day in daily:
            date = day['fxDate']
            temp_max = day['tempMax']
            temp_min = day['tempMin']
            weather_day = day['textDay']
            weather_night = day['textNight']
            
            # 温差提醒
            temp_range = int(temp_max) - int(temp_min)
            range_notice = " ⚠️温差大" if temp_range >= 15 else ""
            
            result += f"📅 {date}: {temp_min}°C ~ {temp_max}°C, {weather_day}/{weather_night}{range_notice}\n"
        
        return result
    
    def _format_air(self, data, city):
        """格式化空气质量"""
        now = data['now']
        aqi = now.get('aqi', 'N/A')
        category = now.get('category', 'N/A')
        pm25 = now.get('pm2p5', 'N/A')
        
        # 空气质量建议
        advice = ""
        aqi_val = int(aqi) if aqi.isdigit() else 999
        if aqi_val <= 50:
            advice = "✅ 空气优，适合户外运动"
        elif aqi_val <= 100:
            advice = "👍 空气良，可正常户外活动"
        elif aqi_val <= 150:
            advice = "⚠️ 轻度污染，减少户外运动"
        elif aqi_val <= 200:
            advice = "❌ 中度污染，建议室内活动"
        else:
            advice = "🚫 重度污染，避免外出"
        
        return f"\n🌫️ {city} 空气质量: AQI {aqi} ({category}) PM2.5: {pm25}\n   {advice}"
    
    def _get_advice(self, temp, weather, hum):
        """根据天气给出建议"""
        advice = []
        temp = int(temp)
        hum = int(hum)
        
        # 温度建议
        if temp < 0:
            advice.append("🥶 严寒，请穿羽绒服、戴帽子手套")
        elif temp < 5:
            advice.append("❄️ 天气寒冷，请穿羽绒服")
        elif temp < 10:
            advice.append("🧥 天冷，穿厚外套+毛衣")
        elif temp < 15:
            advice.append("🧣 天气较凉，建议穿外套")
        elif temp < 20:
            advice.append("👔 温度适中，可以穿长袖+薄外套")
        elif temp < 25:
            advice.append("👕 温度适宜，穿长袖即可")
        elif temp < 30:
            advice.append("🩳 天气偏热，穿短袖")
        elif temp < 35:
            advice.append("☀️ 天气炎热，注意防暑降温")
        else:
            advice.append("🔥 高温预警，尽量待在室内！")
        
        # 天气状况建议
        if '暴雨' in weather:
            advice.append("🌊 暴雨预警，非必要不出门！")
        elif '大雨' in weather:
            advice.append("🌧️ 大雨，出门一定带伞")
        elif '雨' in weather:
            advice.append("☂️ 有雨，记得带伞")
        if '雪' in weather:
            advice.append("⛸️ 有雪，注意防滑")
        if '雷' in weather:
            advice.append("⚡ 雷电预警，避免户外活动")
        if '雾' in weather or '霾' in weather:
            advice.append("😷 能见度低，开车注意安全")
        if '晴' in weather and temp > 20:
            advice.append("🏃 天气晴朗，适合户外活动")
        
        # 湿度建议
        if hum > 80:
            advice.append("💧 湿度高，体感闷热")
        elif hum < 30:
            advice.append("🏜️ 空气干燥，多喝水保湿")
        
        return " | ".join(advice) if advice else "祝你今天愉快！😊"
    
    def daily_report(self, city):
        """生成每日天气报告（整合所有信息）"""
        report = ""
        report += self.get_weather(city)
        report += self.get_forecast(city)
        
        air = self.get_air_quality(city)
        if air:
            report += air
        
        return report


# 使用示例
if __name__ == "__main__":
    # ⚠️ 请替换为你的API Key
    API_KEY = "你的API_Key"
    
    bot = WeatherBot(API_KEY)
    
    # 查询完整天气报告
    print(bot.daily_report("重庆"))
```

---

## 运行效果

> ⚠️ 需要先替换代码中的 `API_KEY` 为你的真实API Key

**查询完整报告：**

```bash
python weather_bot.py
```

**输出结果：**

```
🌍 重庆 当前天气
━━━━━━━━━━━━━━━━━━
🌡️ 温度: 18°C (体感16°C)（体感比实际低2度，注意保暖！）
☁️ 天气: 多云
💧 湿度: 65%
💨 风速: 12km/h 西北风
👁️ 能见度: 15km

💡 👔 温度适中，可以穿长袖+薄外套 | ☂️ 有雨，记得带伞 | 💧 湿度高，体感闷热

🌍 重庆 未来3天预报
━━━━━━━━━━━━━━━━━━
📅 2026-04-17: 15°C ~ 25°C, 多云/小雨
📅 2026-04-18: 18°C ~ 28°C, 晴/晴
📅 2026-04-19: 16°C ~ 22°C, 小雨/阴 ⚠️温差大

🌫️ 重庆 空气质量: AQI 65 (良) PM2.5: 35
   👍 空气良，可正常户外活动
```

---

## 代码关键点

### 1. requests 库 - HTTP请求

```python
import requests

# GET请求（最常用）
response = requests.get(url, params=params, timeout=5)

# 解析JSON响应
data = response.json()

# POST请求
response = requests.post(url, json=payload)

# 带请求头
headers = {'Authorization': 'Bearer xxx'}
response = requests.get(url, headers=headers)
```

### 2. API调用流程

```
1. 构造URL和参数
   ↓
2. 发送GET请求（设置timeout）
   ↓
3. 检查响应状态 (code == '200')
   ↓
4. 解析JSON数据
   ↓
5. 格式化输出
```

### 3. 城市ID缓存

```python
# 和风天气需要城市ID，但每次查询都调API太浪费
# 用字典缓存城市ID，查过一次就不用再查了
self.city_cache = {}

def get_city_id(self, city_name):
    if city_name in self.city_cache:
        return self.city_cache[city_name]  # 命中缓存
    # ... 查询API
    self.city_cache[city_name] = city_id   # 存入缓存
    return city_id
```

### 4. 智能建议逻辑

```python
def _get_advice(self, temp, weather, hum):
    advice = []
    
    # 温度分级建议（从冷到热）
    if temp < 0:
        advice.append("🥶 严寒")
    elif temp < 10:
        advice.append("❄️ 天冷")
    # ...
    
    # 天气状况建议（雨、雪、雷、雾）
    if '雨' in weather:
        advice.append("☂️ 带伞")
    
    # 湿度建议
    if hum > 80:
        advice.append("💧 湿度高")
    
    return " | ".join(advice)
```

---

## 进阶：集成到微信/钉钉

### 方式1：企业微信机器人

```python
def send_to_wechat(message, webhook_key):
    """发送天气提醒到企业微信群"""
    webhook = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={webhook_key}"
    
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": message
        }
    }
    
    try:
        resp = requests.post(webhook, json=data, timeout=5)
        result = resp.json()
        if result.get('errcode') == 0:
            print("✅ 微信推送成功")
        else:
            print(f"❌ 微信推送失败：{result}")
    except Exception as e:
        print(f"❌ 推送出错：{e}")

# 使用
message = bot.daily_report("重庆")
send_to_wechat(message, "你的webhook_key")
```

### 方式2：Server酱（推送到微信个人）

```python
def send_to_serverchan(message, sendkey):
    """通过Server酱推送到微信"""
    url = f"https://sctapi.ftqq.com/{sendkey}.send"
    data = {
        "title": "今日天气提醒",
        "desp": message
    }
    try:
        resp = requests.post(url, data=data, timeout=5)
        print("✅ Server酱推送成功")
    except Exception as e:
        print(f"❌ 推送出错：{e}")
```

### 方式3：钉钉机器人

```python
def send_to_dingtalk(message, webhook_token):
    """发送到钉钉群"""
    import hmac
    import hashlib
    import base64
    import time
    import urllib.parse
    
    timestamp = str(round(time.time() * 1000))
    secret = '你的签名密钥'
    string_to_sign = f'{timestamp}\n{secret}'
    hmac_code = hmac.new(secret.encode(), string_to_sign.encode(), digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    
    url = f"https://oapi.dingtalk.com/robot/send?access_token={webhook_token}&timestamp={timestamp}&sign={sign}"
    data = {
        "msgtype": "text",
        "text": {"content": message}
    }
    requests.post(url, json=data, timeout=5)
```

---

## 避坑指南

### 1. API Key泄露

```python
# ❌ 危险：API Key硬编码在代码里
API_KEY = "abc123def456"  # 推到GitHub就完了

# ✅ 正确：用环境变量
import os
API_KEY = os.environ.get('QWEATHER_API_KEY')

# ✅ 更好：用配置文件（加入.gitignore）
import json
with open('config.json', 'r') as f:
    config = json.load(f)
API_KEY = config['api_key']
```

### 2. API调用频率限制

```python
import time

def rate_limit_call(calls_per_second=1):
    """简单的限流装饰器"""
    min_interval = 1.0 / calls_per_second
    last_called = [0.0]
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

@rate_limit_call(calls_per_second=0.5)  # 每秒最多0.5次（2秒1次）
def get_weather(self, city):
    # ...
```

### 3. 网络超时处理

```python
# ❌ 危险：不设timeout，可能一直卡住
resp = requests.get(url, params=params)

# ✅ 正确：设置timeout
resp = requests.get(url, params=params, timeout=5)

# ✅ 更好：加重试机制
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount('https://', HTTPAdapter(max_retries=retries))

resp = session.get(url, params=params, timeout=5)
```

### 4. 城市名不匹配

```python
# ❌ 问题：用户输入"北京"，API可能不认识
# ✅ 解决：建一个常用城市映射表
city_map = {
    "北京": "101010100",
    "上海": "101020100",
    # ... 或用模糊匹配
}

# 模糊匹配
def fuzzy_match_city(input_name, city_map):
    for name in city_map.keys():
        if input_name in name or name in input_name:
            return city_map[name]
    return None
```

---

## 🔥 完整定时推送方案

```python
import schedule
import time
import os
from datetime import datetime

def daily_weather_push():
    """每日天气推送"""
    api_key = os.environ.get('QWEATHER_API_KEY')
    bot = WeatherBot(api_key)
    
    # 查询多个城市
    cities = ["重庆", "北京"]
    for city in cities:
        report = bot.daily_report(city)
        
        # 推送到微信
        send_to_serverchan(report, os.environ.get('SERVERCHAN_KEY'))
        
        # 或者发邮件
        # send_report(sender, password, [recipient])
    
    print(f"✅ {datetime.now().strftime('%Y-%m-%d %H:%M')} 天气推送完成")

# 每天早上7:30自动推送
schedule.every().day.at("07:30").do(daily_weather_push)

print("🤖 天气推送服务已启动")
while True:
    schedule.run_pending()
    time.sleep(60)
```

---


---

## 📚 推荐：Python 零基础实战营

**系统学习Python，推荐这个免费入门课程 👇**

| 特点 | 说明 |
|-----|------|
| 🎯 专为0基础设计 | 门槛低，上手快 |
| 📹 配套视频讲解 | 配合文章学习效果更好 |
| 💬 专属答疑群 | 遇到问题有人带 |
| 🎁 实体书赠送 | 优秀学员送《Python编程从入门到实践》 |

👉 **[点击免费领取 Python 零基础实战营](https://appycyfaqcq1951.pc.xiaoe-tech.com/p/t_pc/goods_pc_detail/goods_detail/course_38vSeD9XU0XdsWnT6jLTaDeRxjT?channel_id=1515397)**


## 本讲小结

用到的知识：

| 知识 | 用途 |
|-----|------|
| `requests` | 发送HTTP请求 |
| API调用 | 获取第三方数据 |
| JSON解析 | 处理返回的数据 |
| 类封装 | 把功能打包成工具 |
| 条件判断 | 根据天气给建议 |
| 字典缓存 | 优化API调用频率 |
| `schedule` | 定时任务调度 |

---

## 下节预告

实战项目做完了，下一篇是**学习路线图**——帮你规划从入门到实战的学习路径！

👉 **[继续阅读：Python学习路线图](./23-Python学习路线图.md)**

---

## 课程导航

**上一篇：** [Python实战项目-自动发送邮件报告](./21-Python实战项目-自动发送邮件报告.md)

**下一篇：** [Python学习路线图-从入门到精通的完整指南](./23-Python学习路线图.md)

---

*PS：API调用是现代编程的核心技能。学会这个，你可以接入任何互联网服务！*


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


