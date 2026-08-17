[English](README.md) | [简体中文](README.zh-CN.md)

# 🚀 Codex Plugin Generator

Generate production-ready Codex plugins in seconds with best practices built-in.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

## ✨ Features

- 🎨 **Multiple Templates** - MCP servers, Skills, Full plugins
- 📝 **Auto-generated Documentation** - README, CONTRIBUTING, examples
- ✅ **Testing Setup** - pytest configuration included
- 🔄 **CI/CD Ready** - GitHub Actions workflows
- 📦 **Package Configuration** - pyproject.toml with all dependencies
- 🎯 **Best Practices** - Following official Codex guidelines

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/codex-plugin-generator.git
cd codex-plugin-generator

# Install locally
pip install -e .
```

> **Note**: Package will be published to PyPI soon. For now, use local installation.

### Usage

#### Interactive Mode (Recommended)

```bash
codex-plugin-generator generate
```

Answer a few questions and get your plugin scaffolded!

#### Command Line

```bash
# Generate an MCP server plugin
codex-plugin-generator generate --type mcp --name my-mcp-server

# Generate a Skill
codex-plugin-generator generate --type skill --name my-skill

# Generate a full plugin with multiple components
codex-plugin-generator generate --type full --name my-awesome-plugin
```

## 📖 What Gets Generated

### MCP Server Plugin

```
my-mcp-server/
├── src/
│   └── my_mcp_server/
│       ├── __init__.py
│       └── server.py         # MCP server implementation
├── tests/
│   ├── __init__.py
│   └── test_server.py
├── examples/
├── README.md
├── pyproject.toml
├── .gitignore
├── LICENSE
└── .github/workflows/
    └── test.yml
```

### Skill Plugin

```
my-skill/
├── SKILL.md                  # Main skill documentation
├── examples/
│   └── example.md
├── plugin.json
├── README.md
├── .gitignore
└── LICENSE
```

### Full Plugin

```
my-awesome-plugin/
├── src/
│   └── my_awesome_plugin/
│       ├── __init__.py
│       └── server.py
├── skills/
│   └── main-skill/
│       └── SKILL.md
├── tests/
├── docs/
├── examples/
├── README.md
├── CONTRIBUTING.md
├── pyproject.toml
├── .gitignore
└── LICENSE
```

## 🎯 Examples

### Generate an MCP Server for Database Access

```bash
codex-plugin-generator generate \
  --type mcp \
  --name database-connector \
  --description "Connect Codex to PostgreSQL databases" \
  --author "Your Name"
```

### Generate a Skill for Code Review

```bash
codex-plugin-generator generate \
  --type skill \
  --name code-review-helper \
  --description "AI-powered code review assistance" \
  --author "Your Name"
```

## 📚 Templates

### Available Templates

1. **MCP Server** - Full Model Context Protocol server
   - Tool definitions with proper async handlers
   - Testing suite with pytest
   - CI/CD configuration
   - Complete documentation

2. **Skill** - Codex skill with SKILL.md
   - Structured skill documentation
   - Usage examples
   - Best practices guide

3. **Full Plugin** - Complete plugin package
   - MCP server + Skills
   - Comprehensive documentation
   - Testing and CI/CD
   - Contribution guidelines

## 🛠️ Configuration

Create a `.plugin-generator.json` in your home directory to set defaults:

```json
{
  "author": "Your Name",
  "email": "your.email@example.com",
  "github": "yourusername",
  "license": "MIT",
  "include_tests": true,
  "include_ci": true
}
```

Initialize config interactively:

```bash
codex-plugin-generator init-config
```

## 🧪 Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov

# Run code quality checks
black . && ruff check . && mypy .
```

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) (once available).

### Development Setup

```bash
# Clone repository
git clone https://github.com/yourusername/codex-plugin-generator.git
cd codex-plugin-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## 📖 Documentation

- [MCP Protocol Documentation](https://modelcontextprotocol.io)
- [Codex Plugin Development](https://platform.openai.com/docs)
- [Template Customization Guide](docs/templates.md) (coming soon)

## 🌟 Generated Examples

See the `examples/` directory for complete working examples of generated plugins:
- Coming soon: Example MCP server
- Coming soon: Example Skill
- Coming soon: Example Full plugin

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- OpenAI Codex Team for the platform
- MCP Community for the protocol
- All contributors and users

## 📮 Support

- Create an [Issue](../../issues) for bug reports
- Start a [Discussion](../../discussions) for questions
- Star ⭐ this repo if you find it useful!

---

**Made with ❤️ for the Codex community**

> ⚠️ **Status**: Beta - Plugin generation works, but templates are being refined based on community feedback.
