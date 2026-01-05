---
title: git-high-version
date: 2022-06-02 10:17:33
tags: git
---

centos安装高版本git

yum默认安装1.8.1，版本太低了，vscode的插件会报版本过低

```shell
yum install http://opensource.wandisco.com/centos/6/git/x86_64/wandisco-git-release-6-1.noarch.rpm
yum -y install git
git --version
```