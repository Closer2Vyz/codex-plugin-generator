# Codex Plugin Generator

[English](README.md) | 简体中文

> 🚀 **几秒钟内生成生产级 OpenAI Codex 插件**  
> 内置最佳实践，零样板代码，最大化生产力

[![GitHub stars](https://img.shields.io/github/stars/Closer2Vyz/codex-plugin-generator?style=social)](https://github.com/Closer2Vyz/codex-plugin-generator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/badge/pypi-v0.1.0-orange.svg)](https://pypi.org/)

## ✨ 特性

- 🎯 **3种插件类型** - Skill、MCP、Full (完整功能)
- 🚀 **10秒创建** - 从零到生产级插件
- 📦 **14个模板** - 涵盖所有必需文件
- 🧪 **自动测试** - 内置pytest配置
- 🔄 **CI/CD就绪** - GitHub Actions工作流
- 📖 **完整文档** - README、API文档、贡献指南
- ⚡ **交互式CLI** - 美观的命令行界面
- 🎨 **自定义模板** - 轻松扩展和修改

## 🚀 快速开始

### 安装

```bash
# 从源码安装 (推荐)
git clone https://github.com/Closer2Vyz/codex-plugin-generator.git
cd codex-plugin-generator
pip install -e .

# 或从PyPI安装 (即将推出)
pip install codex-plugin-generator
```

### 基础用法

```bash
# 交互式模式 (推荐新手)
codex-plugin-generator generate

# 命令行模式 (快速使用)
codex-plugin-generator generate \
  --type skill \
  --name my-plugin \
  --description "我的第一个Codex插件" \
  --author "你的名字"
```

## 📦 插件类型

### 1. Skill插件 (最简单)
适合：简单的提示词和工作流

```bash
codex-plugin-generator generate --type skill --name my-skill
```

**生成的文件**:
```
my-skill/
├── SKILL.md           # 技能定义和说明
├── README.md          # 项目文档
├── plugin.json        # 插件元数据
├── LICENSE            # MIT许可证
├── .gitignore         # Git忽略规则
└── examples/
    └── example.md     # 使用示例
```

### 2. MCP插件 (中等)
适合：需要工具调用的功能

```bash
codex-plugin-generator generate --type mcp --name my-mcp
```

**生成的文件**:
```
my-mcp/
├── README.md
├── pyproject.toml     # Python项目配置
├── LICENSE
├── .gitignore
├── src/
│   └── my_mcp/
│       ├── __init__.py
│       └── server.py  # MCP服务器实现
├── tests/
│   ├── __init__.py
│   └── test_server.py # 单元测试
└── .github/
    └── workflows/
        └── test.yml   # CI/CD配置
```

### 3. Full插件 (高级)
适合：完整的生产级插件

```bash
codex-plugin-generator generate --type full --name my-full-plugin
```

**生成的文件**:
```
my-full-plugin/
├── README.md
├── pyproject.toml
├── CONTRIBUTING.md    # 贡献指南
├── LICENSE
├── .gitignore
├── src/
│   └── my_full_plugin/
│       ├── __init__.py
│       └── server.py
├── tests/
│   ├── __init__.py
│   └── test_server.py
├── skills/
│   └── main-skill/
│       └── SKILL.md   # 集成的技能
├── docs/              # 文档目录
└── .github/
    └── workflows/
        └── test.yml
```

## 🎯 CLI命令

### generate
生成新的Codex插件

```bash
codex-plugin-generator generate [OPTIONS]

选项:
  -t, --type [mcp|skill|full]  插件类型
  -n, --name TEXT              插件名称 (kebab-case)
  -d, --description TEXT       插件描述
  -a, --author TEXT            作者名称
  -o, --output TEXT            输出目录
  --no-tests                   跳过测试生成
  --no-ci                      跳过CI/CD配置
```

### list-templates
列出可用的模板

```bash
codex-plugin-generator list-templates
```

### init-config
初始化配置文件

```bash
codex-plugin-generator init-config
```

## 📖 使用示例

### 示例1: 创建天气查询Skill

```bash
codex-plugin-generator generate \
  --type skill \
  --name weather-lookup \
  --description "查询城市天气信息" \
  --author "张三"
```

**生成后**:
1. 编辑 `SKILL.md` 添加你的提示词
2. 添加使用示例到 `examples/`
3. 推送到GitHub

### 示例2: 创建数据库查询MCP插件

```bash
codex-plugin-generator generate \
  --type mcp \
  --name database-query \
  --description "执行SQL查询的MCP服务器"
```

**生成后**:
1. 实现 `src/database_query/server.py` 中的工具
2. 运行 `pytest` 确保测试通过
3. 发布到PyPI

### 示例3: 创建完整的文档生成器

```bash
codex-plugin-generator generate \
  --type full \
  --name doc-generator \
  --description "自动化文档生成工具"
```

**生成后**:
1. 开发MCP服务器功能
2. 添加Skill定义
3. 编写完整文档
4. 设置CI/CD
5. 发布插件

## 🏗️ 项目结构

```
codex-plugin-generator/
├── src/
│   └── codex_plugin_generator/
│       ├── __init__.py
│       ├── cli.py          # CLI入口
│       ├── generator.py    # 核心生成逻辑
│       └── templates/      # Jinja2模板
│           ├── common/     # 通用模板
│           ├── skill/      # Skill模板
│           ├── mcp/        # MCP模板
│           └── full/       # Full模板
├── tests/                  # 单元测试
├── examples/               # 示例插件
├── README.md
├── README.zh-CN.md
└── pyproject.toml
```

## 🎨 模板系统

### 可用变量

所有模板都可以使用这些Jinja2变量:

```jinja2
{{ name }}              # 插件名称 (kebab-case)
{{ title }}             # 插件标题 (Title Case)
{{ snake_name }}        # Python包名 (snake_case)
{{ description }}       # 插件描述
{{ author }}            # 作者名称
{{ year }}              # 当前年份
{{ include_tests }}     # 是否包含测试
{{ include_ci }}        # 是否包含CI配置
```

### 自定义模板

1. 复制现有模板目录
2. 修改 `.j2` 文件
3. 在 `generator.py` 中注册新模板

## 🧪 测试

```bash
# 运行所有测试
pytest

# 带覆盖率报告
pytest --cov=codex_plugin_generator

# 详细输出
pytest -v

# 测试特定文件
pytest tests/test_generator.py
```

**测试覆盖**:
- ✅ Skill插件生成
- ✅ MCP插件生成
- ✅ Full插件生成
- ✅ 辅助函数 (kebab_to_title, kebab_to_snake)
- ✅ 模板渲染

## 📊 生成的代码质量

每个生成的插件都遵循最佳实践：

### MCP服务器
- ✅ 使用 `server = Server()` (正确的MCP API)
- ✅ Async/await异步编程
- ✅ 正确的装饰器 (`@server.list_tools()`)
- ✅ 类型提示
- ✅ 错误处理
- ✅ 单元测试

### 项目配置
- ✅ `pyproject.toml` (现代Python打包)
- ✅ `.gitignore` (忽略常见文件)
- ✅ GitHub Actions CI/CD
- ✅ MIT许可证
- ✅ 完整文档

### 代码风格
- ✅ PEP 8兼容
- ✅ 类型注解
- ✅ Docstrings文档
- ✅ 一致的命名约定

## 🌟 为什么选择本工具？

### 与手动创建对比

| 特性 | 手动创建 | Codex Plugin Generator |
|------|---------|----------------------|
| 设置时间 | 2-4小时 | **10秒** |
| 最佳实践 | 需自己研究 | **内置** |
| 测试配置 | 手动设置 | **自动生成** |
| CI/CD | 需要配置 | **一键生成** |
| 文档 | 自己编写 | **完整模板** |
| 错误风险 | 高 | **零** |

## 🛠️ 技术栈

- **Python 3.8+** - 现代Python
- **Click** - 优雅的CLI框架
- **Jinja2** - 强大的模板引擎
- **Pytest** - 测试框架
- **Rich** - 美观的终端输出
- **Pydantic** - 数据验证

## 📚 相关资源

- [Codex Prompt Library](https://github.com/Closer2Vyz/codex-prompt-library) - 精选Codex提示词库
- [OpenAI Codex 文档](https://platform.openai.com/docs/guides/code)
- [MCP协议文档](https://modelcontextprotocol.io/)
- [Jinja2文档](https://jinja.palletsprojects.com/)

## 🤝 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 贡献方式

- 🐛 报告bug
- 💡 建议新功能
- 📝 改进文档
- 🎨 添加新模板
- 🧪 添加测试

## 📜 许可证

本项目采用 [MIT许可证](LICENSE)。

## 🙏 致谢

- OpenAI Codex团队
- 所有开源贡献者
- Python社区

## 📞 获取帮助

- 🐛 [提交Issue](https://github.com/Closer2Vyz/codex-plugin-generator/issues)
- 💬 [讨论区](https://github.com/Closer2Vyz/codex-plugin-generator/discussions)
- 🌟 觉得有用？给个Star！

---

**用Codex Plugin Generator，10秒创建专业级插件！** 🚀
