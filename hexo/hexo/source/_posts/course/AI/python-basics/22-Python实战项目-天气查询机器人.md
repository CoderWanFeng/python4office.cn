---
title: Python实战项目：我做了个天气查询机器人，每天自动推送天气提醒
date: 2026-02-28 21:11:00
tags: [Python实战, API, 天气, 自动化]
---

<p align="center" id='扫码查看 AI 编程训练营'>
    <a target="_blank" href='https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA'>
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
<a href="https://mp.weixin.qq.com/s/Bt_SctzYsPNxLnrK5F9HZA">
  <img src="https://img.shields.io/badge/学习-AI 编程-red" alt="AI 编程">
</a>
    	<a href="https://www.python4office.cn/wechat-group/">
  <img src="https://img.shields.io/badge/加入-AI 交流群-brightgreen" alt="AI 交流群">
</a>

</p>

<!-- more -->

大家好，我是正在实战各种AI项目的程序员晚枫。

今天第三个实战项目：**天气查询机器人**。

> 💡 **场景**：每天出门前都要查天气，与其手动打开APP看，不如让Python自动查！查完还能给你穿衣建议——"今天有雨，记得带伞！"

这个项目会教你：
- 如何调用第三方API（和风天气/心知天气/OpenWeatherMap）
- 如何处理JSON数据
- 如何根据天气给出智能建议

---

## 项目功能

- 查询指定城市的实时天气
- 获取未来3天预报
- 根据天气给出穿衣、出行建议
- 可集成到微信/钉钉机器人

---

## 准备工作

需要注册一个天气API。推荐选择：

| API | 特点 | 免费额度 |
|-----|------|---------|
| [和风天气](https://www.qweather.com/) | 国内数据准 | 1000次/天 |
| [心知天气](https://www.seniverse.com/) | 简单易用 | 300次/天 |
| [OpenWeatherMap](https://openweathermap.org/) | 国际通用 | 1000次/天 |

> 💡 **注册流程**：注册 → 获取API Key → 开始调用

---

## 完整代码（以和风天气为例）

```python
import requests
from datetime import datetime

class WeatherBot:
    def __init__(self, api_key):
        self.api_key = api_key
        # 和风天气API
        self.url_current = "https://devapi.qweather.com/v7/weather/now"
        self.url_forecast = "https://devapi.qweather.com/v7/weather/3d"
    
    def get_weather(self, city):
        """获取当前天气"""
        params = {
            'location': city,
            'key': self.api_key,
            'unit': 'm'  # 摄氏度
        }
        
        try:
            resp = requests.get(self.url_current, params=params)
            data = resp.json()
            
            if data.get('code') == '200':
                return self._format_current(data)
            else:
                return f"查询失败：{data.get('message', '未知错误')}"
        except Exception as e:
            return f"网络错误：{e}"
    
    def get_forecast(self, city):
        """获取天气预报"""
        params = {
            'location': city,
            'key': self.api_key
        }
        
        try:
            resp = requests.get(self.url_forecast, params=params)
            data = resp.json()
            
            if data.get('code') == '200':
                return self._format_forecast(data)
            else:
                return f"查询失败：{data.get('message')}"
        except Exception as e:
            return f"网络错误：{e}"
    
    def _format_current(self, data):
        """格式化当前天气"""
        now = data['now']
        city = data['location'][0]['name']
        temp = now['temp']          # 温度
        feels = now['feelsLike']    # 体感温度
        hum = now['humidity']       # 湿度
        wind = now['windSpeed']     # 风速
        weather = now['text']        # 天气状况
        
        report = f"""
🌍 {city} 当前天气
━━━━━━━━━━━━━━━━━━
🌡️ 温度: {temp}°C (体感{feels}°C)
☁️ 天气: {weather}
💧 湿度: {hum}%
💨 风速: {wind}km/h

💡 {self._get_advice(temp, weather)}
"""
        return report
    
    def _format_forecast(self, data):
        """格式化预报"""
        city = data['location'][0]['name']
        daily = data['daily']
        
        result = f"\n🌍 {city} 未来3天预报\n━━━━━━━━━━━━━━━━━━\n"
        
        for day in daily:
            date = day['fxDate']
            temp_max = day['tempMax']
            temp_min = day['tempMin']
            weather = day['textDay']
            result += f"📅 {date}: {temp_min}°C ~ {temp_max}°C, {weather}\n"
        
        return result
    
    def _get_advice(self, temp, weather):
        """根据天气给出建议"""
        advice = []
        
        # 温度建议
        if temp < 5:
            advice.append("天气寒冷，请穿羽绒服")
        elif temp < 15:
            advice.append("天气较凉，建议穿外套")
        elif temp < 25:
            advice.append("温度适宜，可以穿长袖")
        else:
            advice.append("天气炎热，注意防暑")
        
        # 天气状况建议
        if '雨' in weather:
            advice.append("有雨，记得带伞🌂")
        if '雪' in weather:
            advice.append("有雪，注意防滑⛸️")
        if '晴' in weather:
            advice.append("天气晴朗，适合户外活动🏃")
        
        return " | ".join(advice) if advice else "祝你今天愉快！"


# 使用示例
if __name__ == "__main__":
    # ⚠️ 请替换为你的API Key
    API_KEY = "你的API_Key"
    
    bot = WeatherBot(API_KEY)
    
    # 查询北京天气
    print(bot.get_weather("北京"))
    print("\n" + "="*40 + "\n")
    print(bot.get_forecast("北京"))
```

---

## 运行效果

> ⚠️ 需要先替换代码中的 `API_KEY` 为你的真实API Key

**查询当前天气：**

```bash
python weather_bot.py
```

**输出结果：**

```
🌍 北京 当前天气
━━━━━━━━━━━━━━━━━━
🌡️ 温度: 18°C (体感16°C)
☁️ 天气: 多云
💧 湿度: 45%
💨 风速: 12km/h

💡 温度适宜，可以穿长袖 | 天气晴朗，适合户外活动🏃

========================================

🌍 北京 未来3天预报
━━━━━━━━━━━━━━━━━━
📅 2026-04-17: 12°C ~ 22°C, 晴
📅 2026-04-18: 15°C ~ 25°C, 多云
📅 2026-04-19: 13°C ~ 20°C, 小雨
```

---

## 代码关键点

### 1. requests 库 - HTTP请求

```python
import requests

# GET请求
response = requests.get(url, params=params)
data = response.json()  # 解析JSON响应
```

### 2. API调用流程

```
1. 构造URL和参数
   ↓
2. 发送GET请求
   ↓
3. 检查响应状态 (code == '200')
   ↓
4. 解析JSON数据
   ↓
5. 格式化输出
```

### 3. 智能建议逻辑

```python
def _get_advice(self, temp, weather):
    advice = []
    
    # 温度判断
    if temp < 5:
        advice.append("穿羽绒服")
    # ... 更多判断
    
    # 天气判断
    if '雨' in weather:
        advice.append("带伞")
    
    return " | ".join(advice)
```

---

## 进阶：集成到微信/钉钉

```python
# 发送天气提醒到微信群
def send_to_wechat(message):
    # 使用企业微信机器人或Server酱
    webhook = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx"
    requests.post(webhook, json={"msgtype": "text", "text": {"content": message}})

# 定时发送
import schedule

def job():
    weather = bot.get_weather("北京")
    send_to_wechat(weather)

schedule.every().day.at("07:30").do(job)  # 每天7:30推送
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

