![TASK_TRANSLATE.md - 配图1](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)
![TASK_TRANSLATE.md - 配图2](https://images.unsplash.com/photo-151707730?w=800&h=400&fit=crop)
# 批量翻译任务说明

## 目标
将当前目录下的中文 Markdown 文件批量翻译为英文，生成 `-en.md` 后缀的英文版本。

## 目录路径
```
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads
```

## 文件统计
- 总计 308 个中文 Markdown 文件需要翻译
- 已完成：143 个（截至 2026-04-23）
- 剩余：165 个

## 最新进度
- 2026-04-23：完成 `atomgit` 目录下全部 8 个中文文件的翻译，新增 8 个英文版本
- 2026-04-23：完成 `deepseek` 目录下全部 8 个中文文件的翻译，新增 8 个英文版本
- 2026-04-23：完成 `xunfei` 目录下全部 6 个中文文件的翻译，新增 6 个英文版本
- 2026-04-23：完成 `ai` 目录下全部 7 个中文文件的翻译，新增 7 个英文版本
- 2026-04-23：完成 `ai-agent` 目录下全部 3 个中文文件的翻译，新增 3 个英文版本
- 2026-04-23：完成 `aliyun` 目录下全部 10 个中文文件的翻译，新增 10 个英文版本
- 2026-04-23：完成 `tencent` 目录下全部 10 个中文文件的翻译，新增 10 个英文版本

## 翻译方案
- 使用 **MyMemory API**（免费，https://mymemory.translated.net）
- 调用命令：
  ```bash
  python3 batch_translate.py "/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads" 0.3
  ```
- 进程 PID：8739
- 日志文件：`/Users/wanfeng/code/opc-website/python4office.cn/translate.log`

## 输出文件命名规则
- 原文：`xxx.md`
- 译文：`xxx-en.md`

## 监控命令
```bash
# 查看已翻译数量
ls /Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/**/*-en.md 2>/dev/null | wc -l

# 查看日志
tail -20 /Users/wanfeng/code/opc-website/python4office.cn/translate.log

# 停止翻译
pkill -f batch_translate.py
```

## 待翻译文件列表
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/TASK_TRANSLATE.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/ali/openclaw/20260408-aliyun-coding-plan-who-should-use.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/20250725-字节海外.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/250726-coze开源.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/250903-剪映小助手.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/arkclaw/20260412-arkclaw-40-yuan-not-enough.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/arkclaw/20260412-arkclaw-7x24-real-task.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/arkclaw/20260412-arkclaw-invite-code-guide.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/arkclaw/20260412-arkclaw-what-is-it.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/0-提示词.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/1-智能简史.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/10-第一性原理.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/11-黑客与画家.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/12-从零构建大模型.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/13-大模型技术30讲.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/14-贫穷的本质.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/18-机器学习漫画小抄.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/2-从新手到高手.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/20-英伟达之道.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/22-无人机diy.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/23-超智能与未来.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/24-AI辅助编程实战.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/4-我看见的世界.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/5-图解DeepSeek.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/8-芯片通识课.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/9-算法面试328题.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/公众号文章/2万的培训班.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/1-Python编程从入门到实践/1-从入门到实践.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/1-Python编程从入门到实践/2-从入门到实践.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/1-Python编程从入门到实践/3-从入门到实践.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/1-Python编程从入门到实践/4.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/1-Python编程从入门到实践/5.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/2-图解大模型/1-图解大模型.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/2-图解大模型/2.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/2-图解大模型/3.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/2-图解大模型/4-图解ds.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/2-图解大模型/5-大模型.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/2-图解大模型/6.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/2-图解大模型/7.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/2-图解大模型/8.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/2-图解大模型/9.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/3-金融人工智能/1-金融人工智能.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/3-金融人工智能/2.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/3-金融人工智能/3.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/3-金融人工智能/4.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/3-金融人工智能/5.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/3-金融人工智能/6.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/3-金融人工智能/7.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/4-数据科学手册/19-Python数据科学手册.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/4-数据科学手册/2.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/4-数据科学手册/3.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/5-程序员数学/1-程序员数学.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/5-程序员数学/2.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/5-程序员数学/3.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/5-程序员数学/4.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/5-程序员数学/5.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/5-程序员数学/6.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/5-程序员数学/7.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/5-程序员数学/8.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/6-流畅的Python/21-流畅的python-2.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/6-流畅的Python/3.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/6-流畅的Python/4.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/6-流畅的Python/5.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/6-流畅的Python/6-流畅的Python.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/7-怎么样系列/1-计算机怎样跑起来的.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/7-怎么样系列/2.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/7-怎么样系列/3-网络连接.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/7-怎么样系列/4-程序怎么跑起来.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/7-怎么样系列/5.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/7-怎么样系列/6.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/7-怎么样系列/7.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/7-怎么样系列/8.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/卖出去的书/7-怎么样系列/9.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/书单号/模板.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/工作流/20250822-自动发文章.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/coze/工作流/下载链接/公众号.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260408-ark-coding-plan-model-review.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260408-ark-coding-plan-save-money.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260408-ark-coding-plan-tutorial.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260408-ark-coding-plan-vs-copilot.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260408-ark-coding-plan-who-should-use.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260408-ark-coding-plan.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-api-usage.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-cursor-guide.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-detailed-guide.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-faq-detailed.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-faq.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-prompt-skills.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-python-dev.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-quick-compare.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-student-guide.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-team-use.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-vs-code.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-why-choose.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260410-ark-coding-plan-workflow.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260413-ark-coding-plan-1day-1000lines.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260413-ark-coding-plan-after-claude-copilot.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260413-ark-coding-plan-ai-tool-price-rise.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260413-ark-coding-plan-copilot-hard-to-use.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260413-ark-coding-plan-price-increase-reason.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260413-ark-coding-plan-price-rise-all.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260413-ark-coding-plan-promotion-income.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260413-ark-coding-plan-vs-copilot-price-rise.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260416-claude-code-cheaper.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260416-claude-code-free.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/bytedance/huoshan/20260416-claude-code-huoshan-model.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260422-tencent-cloud-coding-plan-intro.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260422-tencent-cloud-coding-plan-tutorial.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260422-tencent-cloud-coding-plan-who-should-use.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-cloud-coding-plan-api.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-cloud-coding-plan-faq.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-cloud-coding-plan-open.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-cloud-coding-plan-price.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-cloud-coding-plan-save-money.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-cloud-coding-plan-student.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-cloud-coding-plan-update.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-cloud-coding-plan-who.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-vs-aliyun.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/20260423-tencent-vs-huoshuanfangzhou.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/CodeBuddy/20251028-popdf-gui.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/CodeBuddy/20251031-cli.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/CodeBuddy/20251104-hexo-build.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/CodeBuddy/20251107-CodeBuddy-GLM4.6.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/CodeBuddy/260311-cbc-ai.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/Workuddy/20230407-opc.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/Workuddy/260319-ocr.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/Workuddy/articles/20260407-lobster-class-zhengzhou.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/Workuddy/articles/20260407-qclaw-vs-workbuddy.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/Workuddy/how-to-opc.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/Workuddy/郑州/0410-ppt.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/20260408-tencent-openclaw-business-case.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/20260408-tencent-openclaw-deploy-guide.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/20260408-tencent-openclaw-deploy.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/20260408-tencent-openclaw-vs-others.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/20260408-tencent-openclaw-zhengzhou.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/260310-实战.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/260313-重庆养虾大会.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/260314-重庆养虾大会-2.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/260325-重庆装虾.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/openclaw/260328-重庆龙虾公开课.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260410-cloud-price-rise-ai-coding.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260410-tencent-tokenplan-complete-guide.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260410-tencent-tokenplan-faq.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260410-tencent-tokenplan-vs-codingplan.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260411-ai-nav-launch.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260411-mbti-ai-coding-1-intro.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260411-mbti-ai-coding-2-tutorial.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260411-mbti-ai-coding-3-business.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260411-mbti-ai-coding-4-comparison.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260411-mbti-ai-coding-5-faq.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260416-claude-code-tokenplan-cheaper.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260416-claude-code-tokenplan-free.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260416-claude-code-tokenplan-model.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260422-aliyun-vs-tencent-tokenplan.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260422-coding-plan-upgrade-notice.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260422-tokenplan-for-student.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260422-tokenplan-vs-volcano.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/tencent/tokenplan/20260422-why-switch-domestic.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/unitree/20250727-3.99万的机器人-en.99万的机器人.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/unitree/20250727-3.99万的机器人.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/优质教程/20240613-ai-code.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/优质教程/哈佛/20250803-cs50p.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/卖书/python入门.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/卖书/xi/4-6.md
/Users/wanfeng/code/opc-website/python4office.cn/hexo/hexo/source/_posts/ads/卖书/xi/7-11.md


## 🎓 AI 编程实战课程

想系统学习 AI 编程？程序员晚枫的 **AI 编程实战课** 帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)


