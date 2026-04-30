---
title: sqlalchemy常用语法
date: "2022-02-10 14:17:07"
tags: sqlalchemy
cover: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1200&auto=format&fit=crop"
---


<!-- more -->

![sqlalchemy常用语法](https://images.pexels.com/photos/1181263/pexels-photo-1181263.jpeg?auto=compress&cs=tinysrgb&w=800)
![sqlalchemy常用语法](https://images.unsplash.com/photo-151707730?w=800&h=400&fit=crop)

```python
# 查询代码如下：
0.like:模糊查询
result0 = db.session.query(Protocols.protocolName).filter(Protocols.protocolName.like("%" + "cp" + "%")).all()
1.notlike：模糊查询，不在查询范围内
result1 = db.session.query(Protocols.protocolName).filter(Protocols.protocolName.notlike("%" + "cp" + "%")).all()
2.in_:在某个范围内，参数为元组或者列表类型的数据
result2 = db.session.query(Protocols.protocolName).filter(Protocols.id.in_((1, 2))).all()
3.notin_：和in_相反
result3 = db.session.query(Protocols.protocolName).filter(Protocols.id.notin_((1, 2))).all()
4.is_:是否为null的比较
result4 = db.session.query(Protocols.protocolName).filter(Protocols.protocolName.is_(None)).all()
5.isnot:不为null
result5 = db.session.query(Protocols.protocolName).filter(Protocols.protocolName.isnot(None)).all()
6.startswith：以某个数据开头
result6 = db.session.query(Protocols.protocolName).filter(Protocols.protocolName.startswith("t")).all()
7.endswith：以某数据结尾
result7 = db.session.query(Protocols.protocolName).filter(Protocols.protocolName.endswith("t")).all()
8.contains：数据中包含，和like功能差不多
result8 = db.session.query(Protocols.protocolName).filter(Protocols.protocolName.contains("cp")).all()
9.desc：对查询出来的数据进行降序排序
result9 = db.session.query(Protocols.protocolName).order_by(Protocols.id.desc()).all()
10.asc：对查询出来的数据进行升序排序
result10 = db.session.query(Protocols.protocolName).order_by(Protocols.id.asc()).all()
11.between：某个字段的参数在某个范围内
result11 = db.session.query(Protocols.protocolName).filter(Protocols.id.between(1, 3)).all()
12.distinct：对查询出来的数据进行去重
result12 = db.session.query(Protocols.parent_protocol).distinct().all()

```

## 相关阅读

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)


## 🎓 AI 编程实战课程

程序员晚枫专注AI编程培训，通过 **[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/8p2eviFUmYa1V0pswmDRmw)**，让小白也能用AI做出实际项目。帮你从零上手！

- 👉 **课程报名**：[点击这里报名，前3讲免费试听](https://r7up9.xetslk.com/s/1uP5YW)
- 👉 **免费试看**：[B站免费试看前3讲，先看看适不适合自己](https://www.bilibili.com/cheese/play/ss982042944)

