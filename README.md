# 🛠️ GitHub Utilities

A comprehensive collection of GitHub automation tools for developers, DevOps teams, and project managers. Streamline your GitHub workflows with powerful utilities for issue management, automation, and reporting.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

---

## 🚀 Available Tools

### **📝 Issue Creator**
Automate GitHub issue creation with configurable templates and bulk operations.

- **Bulk Issue Creation**: Create multiple issues from text files
- **Template-Based**: Use JSON configuration files for consistent formatting
- **Smart Features**: Duplicate prevention, dry-run mode, label management
- **Use Cases**: Project planning, feature requests, compliance tracking

**Quick Start:**
```bash
cd issue-creator/
python github-issue-creator.py --config config-examples/basic-config.json --file examples/sample-items.txt
```

### **📊 Issue Analyzer**
Generate detailed reports and analytics from closed GitHub issues.

- **Advanced Filtering**: Filter by labels, date ranges, assignees
- **Multiple Exports**: CSV, JSON, and console outputs
- **Comprehensive Analytics**: Trends, statistics, resolution times
- **Use Cases**: Team performance, sprint retrospectives, reporting

**Quick Start:**
```bash
cd issue-analyzer/
python github-issues-analyzer.py --owner myorg --repo myrepo --format csv
```

---

## 🛠️ Coming Soon

### **🔄 PR Automation** (Planned)
- Automated pull request creation and management
- Template-based PR descriptions
- Bulk PR operations

### **🏛️ Repository Management** (Planned)
- Repository setup and configuration automation
- Bulk repository operations
- Settings synchronization

### **🔒 Branch Protection Utilities** (Planned)
- Automated branch protection rule setup
- Policy management across repositories
- Compliance enforcement

### **⚡ GitHub Actions Helpers** (Planned)
- Workflow template generation
- Action configuration utilities
- CI/CD automation tools

---

## 📋 Quick Setup

### **Prerequisites**
- Python 3.7+
- GitHub Personal Access Token
- Git configured with your GitHub account

### **Installation**
```bash
# Clone the repository
git clone https://github.com/CloudSecOpsAI/github-utilities.git
cd github-utilities

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp issue-creator/env.example .env
# Edit .env with your GitHub token
```

### **Authentication Setup**
1. Create a [GitHub Personal Access Token](https://github.com/settings/tokens)
2. Add token to your `.env` file:
```bash
GITHUB_TOKEN=your_token_here
```

---

## 📁 Repository Structure

```
github-utilities/
├── README.md                          # This overview
├── LICENSE                            # MIT License
├── requirements.txt                   # Shared dependencies
├── .gitignore                         # Global ignore patterns
├── issue-creator/                     # Issue creation tools
│   ├── README.md                     # Issue creator documentation
│   ├── github-issue-creator.py       # Main script
│   ├── config-examples/              # Template configurations
│   └── examples/                     # Usage examples
├── issue-analyzer/                    # Issue analysis tools
│   ├── README.md                     # Issue analyzer documentation
│   ├── github-issues-analyzer.py     # Main script
│   └── examples/                     # Usage examples
├── docs/                             # Shared documentation
│   ├── getting-started.md           # Setup guide
│   ├── authentication.md            # Auth setup
│   └── troubleshooting.md           # Common issues
└── scripts/                          # Utility scripts
    ├── setup.sh                     # Environment setup
    └── test-all.sh                  # Test all tools
```

---

## 🎯 Use Cases

### **Project Management**
- **Sprint Planning**: Bulk create sprint tasks and user stories
- **Feature Tracking**: Generate issues for roadmap items
- **Bug Triage**: Analyze bug resolution patterns

### **DevOps Workflows**
- **Release Planning**: Create release tracking issues
- **Compliance**: Generate compliance requirement issues
- **Reporting**: Monthly team performance reports

### **Team Collaboration**
- **Onboarding**: Create standardized onboarding tasks
- **Documentation**: Track documentation requirements
- **Code Review**: Analyze review patterns and performance

---

## 🔧 Configuration Examples

### **Issue Creator Templates**
```json
{
  "repository": {
    "owner": "myorg",
    "name": "myrepo"
  },
  "issue_template": {
    "title_format": "Feature: {item}",
    "body_template": "## Objective\nImplement {item} functionality..."
  },
  "labels": ["enhancement", "feature"],
  "assignees": ["team-lead"]
}
```

### **Issue Analyzer Filtering**
```bash
# Team performance report
python github-issues-analyzer.py --owner myorg --repo myrepo --days 30 --format csv

# Bug analysis
python github-issues-analyzer.py --owner myorg --repo myrepo --labels "bug" --format json

# Sprint retrospective
python github-issues-analyzer.py --owner myorg --repo myrepo --since 2024-01-01 --until 2024-01-14
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🐛 Report Issues**: Found a bug? [Create an issue](https://github.com/CloudSecOpsAI/github-utilities/issues)
2. **💡 Suggest Features**: Have an idea? [Start a discussion](https://github.com/CloudSecOpsAI/github-utilities/discussions)
3. **🔧 Submit PRs**: Want to contribute code? Fork and submit a pull request
4. **📚 Improve Docs**: Help make our documentation better

### **Development Setup**
```bash
# Fork and clone your fork
git clone https://github.com/your-username/github-utilities.git
cd github-utilities

# Create feature branch
git checkout -b feature/your-feature

# Make changes and test
# Submit pull request
```

---

## 📚 Documentation

- **[Getting Started](docs/getting-started.md)** - Complete setup guide
- **[Authentication](docs/authentication.md)** - GitHub token setup
- **[Issue Creator Guide](issue-creator/README.md)** - Detailed usage
- **[Issue Analyzer Guide](issue-analyzer/README.md)** - Analytics and reporting
- **[Troubleshooting](docs/troubleshooting.md)** - Common issues and solutions

---

## 🔗 Related Projects

- **[GitHub CLI](https://cli.github.com/)** - Official GitHub command line tool
- **[Hub](https://hub.github.com/)** - Command-line wrapper for git
- **[Octokit](https://octokit.github.io/)** - Official GitHub API libraries

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you find these tools helpful:
- ⭐ **Star this repository**
- 🐛 **Report issues** you encounter
- 💡 **Suggest new features**
- 🤝 **Contribute** to the project
- 📢 **Share** with your team

---

## 📈 Roadmap

### **2024 Q4**
- ✅ Issue Creator
- ✅ Issue Analyzer
- 🔄 Documentation improvements
- 🔄 Enhanced examples

### **2025 Q1**
- 🚀 PR Automation tools
- 🚀 Repository management utilities
- 🚀 Enhanced configuration options

### **2025 Q2**
- 🚀 Branch protection utilities
- 🚀 GitHub Actions helpers
- 🚀 Advanced automation workflows

---

**Transform your GitHub workflow with powerful automation tools! 🚀**