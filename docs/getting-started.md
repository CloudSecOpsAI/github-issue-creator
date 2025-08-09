# 🚀 Getting Started with GitHub Utilities

This guide will help you set up and start using the GitHub Utilities toolkit.

## 📋 Prerequisites

- **Python 3.7+** installed on your system
- **Git** configured with your GitHub account
- **GitHub account** with appropriate repository access
- **GitHub Personal Access Token** (we'll help you create one)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/CloudSecOpsAI/github-utilities.git
cd github-utilities
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment
```bash
cp issue-creator/env.example .env
```

## 🔑 Authentication Setup

### Create GitHub Personal Access Token

1. Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
2. Click **"Generate new token (classic)"**
3. Give it a descriptive name (e.g., "GitHub Utilities")
4. Select these scopes:
   - ✅ **repo** (full control of private repositories)
   - ✅ **read:org** (read organization data)
   - ✅ **workflow** (update GitHub Actions workflows)
5. Click **"Generate token"**
6. **Copy the token immediately** (you won't see it again)

### Configure Environment
Edit your `.env` file:
```bash
GITHUB_TOKEN=your_token_here
```

## 🧪 Test Your Setup

### Test Issue Creator
```bash
cd issue-creator/
python github-issue-creator.py --help
```

### Test Issue Analyzer
```bash
cd issue-analyzer/
python github-issues-analyzer.py --help
```

## 🎯 Your First Automation

### Create Your First Issues
```bash
cd issue-creator/
python github-issue-creator.py \
  --config config-examples/basic-config.json \
  --file examples/sample-items.txt \
  --dry-run
```

### Generate Your First Report
```bash
cd issue-analyzer/
python github-issues-analyzer.py \
  --owner microsoft \
  --repo vscode \
  --days 7
```

## 📚 Next Steps

- **[Issue Creator Guide](../issue-creator/README.md)** - Learn bulk issue creation
- **[Issue Analyzer Guide](../issue-analyzer/README.md)** - Master reporting and analytics
- **[Authentication Guide](authentication.md)** - Advanced auth setup
- **[Troubleshooting](troubleshooting.md)** - Common issues and solutions

## 💡 Pro Tips

1. **Start with dry-run mode** to test configurations safely
2. **Use descriptive commit messages** when contributing
3. **Keep your token secure** - never commit it to git
4. **Test with public repositories** first to validate setup
5. **Read tool-specific documentation** for advanced features

**Ready to automate your GitHub workflows! 🚀**