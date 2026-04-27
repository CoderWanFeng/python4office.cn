# 文件命名规范文档

## 目的

为了防止Git在不同操作系统（Windows、Mac、Linux）之间出现文件大小写冲突问题，特制定本命名规范。

## 背景

Git默认区分文件名大小写，但不同操作系统的文件系统对大小写的处理方式不同：
- **Windows**：不区分大小写（NTFS）
- **Mac**：默认不区分大小写（APFS）
- **Linux**：区分大小写（ext4等）

这会导致在跨平台协作时出现文件冲突，例如：
```
fatal: will not add file alias 'hexo/hexo/public/tags/C语言/index.html' 
('hexo/hexo/public/tags/c语言/index.html' already exists in index)
```

## 命名规范

### 1. 标签（Tags）

**规则**：所有标签必须使用小写字母

**示例**：
- ✅ 正确：`tags: [wwp, c语言, python, javascript]`
- ❌ 错误：`tags: [wwp, C语言, Python, JavaScript]`

### 2. 分类（Categories）

**规则**：所有分类必须使用小写字母

**示例**：
- ✅ 正确：`categories: [教程, 编程]`
- ❌ 错误：`categories: [教程, 编程]`

### 3. 文件路径

**规则**：所有文件路径必须使用小写字母

**示例**：
- ✅ 正确：`/hexo/hexo/source/_posts/wwp/array.md`
- ❌ 错误：`/hexo/hexo/source/_posts/wwp/Array.md`

### 4. 文件名

**规则**：文件名使用小写字母，单词之间用连字符（-）分隔

**示例**：
- ✅ 正确：`my-first-post.md`, `python-tutorial.md`
- ❌ 错误：`MyFirstPost.md`, `PythonTutorial.md`

## Git配置

### 必需配置

在项目根目录执行以下命令，确保Git正确处理大小写：

```bash
git config core.ignorecase false
```

### 验证配置

```bash
git config core.ignorecase
# 应该输出：false
```

## 检查清单

在提交代码前，请检查以下内容：

- [ ] 所有标签使用小写字母
- [ ] 所有分类使用小写字母
- [ ] 文件路径使用小写字母
- [ ] 文件名使用小写字母和连字符
- [ ] Git配置 `core.ignorecase` 设置为 `false`

## 常见问题

### Q: 如果已经存在大小写冲突怎么办？

A: 执行以下步骤清理冲突：

```bash
# 1. 从Git缓存中删除冲突的文件
git rm -rf --cached <冲突文件路径>

# 2. 统一文件名格式为小写

# 3. 重新添加文件
git add -A

# 4. 提交更改
git commit -m "fix: 统一文件名为小写格式"
```

### Q: 为什么不能使用大写字母？

A: 虽然大写字母在某些操作系统上可以正常工作，但在跨平台协作时会导致问题。统一使用小写字母可以避免所有潜在的冲突。

### Q: 中文标签需要遵循这个规范吗？

A: 是的。虽然中文没有大小写之分，但为了保持一致性，建议所有标签和分类都使用统一格式。

## 参考资料

- [Git - git-config Documentation](https://git-scm.com/docs/git-config)
- [Git Case Sensitivity](https://git.wiki.kernel.org/index.php/GitFaq#Git_has_case_insensitive_filenames.3F)

## 更新历史

- 2026-03-09: 初始版本，解决C语言标签大小写冲突问题
