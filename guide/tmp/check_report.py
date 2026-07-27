import re
p='/Users/wanfeng/晚枫工作室/内容更新/个人网站/python4office.cn/guide/千问办公QwenWork产品深度研究.md'
t=open(p,encoding='utf-8').read()
lines=t.count('\n')+1
print('总行数:',lines)
print('二级标题(##):',t.count('\n## '))
print('三级标题(###):',t.count('\n### '))
tbl=sum(1 for l in t.split('\n') if l.strip().startswith('|'))
print('表格行数:',tbl)
print('代码块数(```):',t.count('```'))
bad=re.findall(r'(保证收益|稳赚|第一|最强)',t)
print('敏感/夸大词(除引用):',bad if bad else '无')
print('非官方声明出现次数:',t.count('非官方'))
print('章节数(一~十):',len(re.findall(r'\n## 一、|\n## 二、|\n## 三、|\n## 四、|\n## 五、|\n## 六、|\n## 七、|\n## 八、|\n## 九、|\n## 十、',t)))
