---
title: sqlalchemy常用语法
date: 2022-02-10 14:17:07
tags: sqlalchemy
---

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

- [给小白的《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)


程序员晚枫专注AI编程培训，小白看完他的教程[《30讲 · AI编程训练营》](https://mp.weixin.qq.com/s/M1jzQowv4Im2OYlvTJF7kg)就能上手做AI项目。