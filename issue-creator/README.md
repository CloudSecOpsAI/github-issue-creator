# 🚀 GitHub Issue Creator

A powerful and flexible Python tool to automatically create GitHub issues from text files using configurable JSON templates. Perfect for bulk issue creation, project planning, standardized workflows, and team collaboration.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

---

## ✨ Features

- 📝 **Template-Based Creation**: Use JSON configuration files to define custom issue templates
- 🔄 **Bulk Issue Creation**: Create multiple issues from simple text files
- 🏷️ **Labels & Assignees**: Automatically assign labels, assignees, and milestones
- 🔍 **Duplicate Prevention**: Smart checking to avoid creating duplicate issues
- 🧪 **Dry Run Mode**: Test your configuration safely before creating actual issues
- ⚙️ **Highly Configurable**: Easy-to-modify JSON templates for any workflow
- 🎯 **Template Variables**: Use `{item}` placeholder for dynamic content

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- GitHub Personal Access Token
- Required packages: `requests`, `python-dotenv`

### Installation
```bash
git clone <your-repo-url>
cd github-issue-creator
pip install -r requirements.txt
```

### Setup
1. Get a GitHub Personal Access Token with `repo` scope
2. Copy the environment template:
```bash
cp env.example .env
```
3. Edit `.env` and add your token:
```bash
GITHUB_TOKEN=your_token_here
```

### Basic Usage
```bash
# Test with dry run (safe, no issues created)
python github-issue-creator.py --config config-examples/basic-config.json --file examples/sample-items.txt

# Actually create issues
python github-issue-creator.py --config config-examples/basic-config.json --file examples/sample-items.txt --no-dry-run
```

---

## 📋 Configuration Examples

### Basic Feature Requests (`config-examples/basic-config.json`)
```json
{
  "repository": {
    "owner": "myorg",
    "name": "myrepo"
  },
  "issue_template": {
    "title_format": "Add {item} support",
    "body_template": "**Objective**\nImplement {item} functionality..."
  },
  "labels": ["enhancement", "feature"],
  "assignees": ["developer"],
  "input_file": "features-list.txt"
}
```

### Feature Requests (`config-examples/feature-requests.json`)
Perfect for product planning and user story creation.

### Compliance Tracking (`config-examples/compliance-tracking.json`)
Ideal for security standards and audit requirements.

---

## 📝 Input Files

Create a simple text file with one item per line:

**Example (`examples/sample-items.txt`):**
```
User Authentication
Dashboard Analytics
Email Notifications
Mobile App
API Documentation
```

Each line becomes an `{item}` in your template!

---

## 🔧 Command Options

| Option | Description | Example |
|--------|-------------|---------|
| `--config` | Path to JSON configuration file | `--config my-config.json` |
| `--file` | Path to input text file (overrides config) | `--file items.txt` |
| `--dry-run` | Test mode - no issues created (default) | `--dry-run` |
| `--no-dry-run` | Actually create issues | `--no-dry-run` |

---

## 📊 Example Workflows

### 1. Product Feature Planning
```bash
# Create feature request issues
python github-issue-creator.py \
  --config config-examples/feature-requests.json \
  --file product-features.txt \
  --no-dry-run
```

### 2. Security Compliance Tracking
```bash
# Create compliance tracking issues
python github-issue-creator.py \
  --config config-examples/compliance-tracking.json \
  --file security-standards.txt \
  --no-dry-run
```

### 3. Sprint Planning
```bash
# Test configuration first
python github-issue-creator.py --config sprint-config.json --dry-run

# Create sprint issues
python github-issue-creator.py --config sprint-config.json --no-dry-run
```

---

## 🎯 Use Cases

### **Project Management**
- Sprint planning and task creation
- Feature roadmap tracking
- Bug fix initiatives

### **Compliance & Security**
- Security audit requirements
- Compliance standard tracking
- Risk assessment tasks

### **Development Workflows**
- API endpoint implementation
- Library integrations
- Testing requirements

### **Team Collaboration**
- Onboarding checklists
- Documentation tasks
- Code review processes

---

## 📁 File Structure

```
github-issue-creator/
├── github-issue-creator.py           # Main script
├── requirements.txt                  # Dependencies
├── README.md                        # This documentation
├── LICENSE                          # MIT License
├── .gitignore                       # Git ignore patterns
├── env.example                      # Environment template
├── config-examples/                 # Configuration templates
│   ├── basic-config.json           # Basic feature requests
│   ├── feature-requests.json       # Product planning
│   └── compliance-tracking.json    # Security/compliance
└── examples/                        # Usage examples
    ├── sample-items.txt            # Example input file
    └── create-issues.sh            # Demo script
```

---

## 🔍 Safety Features

### **Duplicate Prevention**
- Automatically checks existing open issues
- Compares issue titles to avoid duplicates
- Skips creation if issue already exists

### **Dry Run Mode (Default)**
- Test your templates safely
- See exactly what would be created
- Default behavior prevents accidents

### **Input Validation**
- Validates JSON configuration files
- Checks for required fields
- Verifies file paths and permissions

---

## 📈 Sample Output

### Dry Run Output
```
Dry run is set to: True (default is True; set to False to actually create issues)

Summary of inputs:
  Config: config-examples/basic-config.json
  Owner: myorg
  Repo: myrepo
  Input File: examples/sample-items.txt
  Labels: enhancement, feature
  Assignees: developer

🔍 Would post to: https://api.github.com/repos/myorg/myrepo/issues
    Title: Add User Authentication support
    Labels: enhancement, feature
    Assignees: developer
[DRY RUN] Issue not actually created.

⚠️ Skipped (already exists): Add Dashboard Analytics support
```

### Actual Creation
```
✅ Created: Add User Authentication support
⚠️ Skipped (already exists): Add Dashboard Analytics support
✅ Created: Add Email Notifications support
```

---

## 🛠️ Creating Custom Configurations

### 1. Copy a Template
```bash
cp config-examples/basic-config.json my-config.json
```

### 2. Customize Your Template
```json
{
  "repository": {
    "owner": "your-org",
    "name": "your-repo"
  },
  "issue_template": {
    "title_format": "Implement {item}",
    "body_template": "## Objective\nImplement {item} in our system...\n\n## Tasks\n- [ ] Research {item}\n- [ ] Design solution\n- [ ] Implement {item}"
  },
  "labels": ["enhancement"],
  "assignees": ["team-lead"]
}
```

### 3. Create Input File
```bash
echo -e "Payment Gateway\nUser Dashboard\nEmail System" > my-items.txt
```

### 4. Test and Deploy
```bash
# Test first
python github-issue-creator.py --config my-config.json --file my-items.txt

# Create issues
python github-issue-creator.py --config my-config.json --file my-items.txt --no-dry-run
```

---

## 🐛 Troubleshooting

### Common Issues

**Authentication Error**
```
❌ Missing GitHub token
```
**Solution**: Set `GITHUB_TOKEN` in `.env` file

**Configuration File Error**
```
❌ Config file not found: my-config.json
```
**Solution**: Check file path and ensure file exists

**Invalid JSON**
```
❌ Invalid JSON in config file
```
**Solution**: Validate JSON syntax using online JSON validator

**Input File Error**
```
❌ Invalid input file: items.txt
```
**Solution**: Ensure file exists and has `.txt` extension

---

## 🤝 Best Practices

1. **Always Test First**: Use dry-run mode before creating actual issues
2. **Descriptive Titles**: Make issue titles clear and searchable
3. **Consistent Templates**: Use standardized templates across projects
4. **Version Control**: Keep configuration files in source control
5. **Regular Cleanup**: Archive or close completed configuration files
6. **Team Standards**: Establish labeling and assignment conventions

---

## 📚 Examples Gallery

### Development Tasks
```json
{
  "issue_template": {
    "title_format": "Implement {item} API endpoint",
    "body_template": "## API Endpoint: {item}\n\n### Requirements\n- [ ] Design {item} endpoint\n- [ ] Implement business logic\n- [ ] Add validation\n- [ ] Write tests\n- [ ] Update documentation"
  }
}
```

### Bug Fixes
```json
{
  "issue_template": {
    "title_format": "Fix: {item} issue",
    "body_template": "## Bug Report: {item}\n\n### Description\nResolve {item} related issues.\n\n### Steps\n- [ ] Investigate {item} problem\n- [ ] Identify root cause\n- [ ] Implement fix\n- [ ] Test solution"
  }
}
```

### Documentation
```json
{
  "issue_template": {
    "title_format": "Document {item}",
    "body_template": "## Documentation Task: {item}\n\n### Objective\nCreate comprehensive documentation for {item}.\n\n### Deliverables\n- [ ] User guide for {item}\n- [ ] Technical specifications\n- [ ] Examples and tutorials"
  }
}
```

---

## 🔄 Integration Ideas

### **CI/CD Pipelines**
- Automatically create issues from deployment failures
- Generate release tracking issues

### **Project Management Tools**
- Export configurations for different project types
- Sync with existing project templates

### **Team Workflows**
- Onboarding task creation
- Regular maintenance issue generation

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you find this tool helpful:
- ⭐ Star the repository
- 🐛 Report issues
- 💡 Suggest features
- 🤝 Contribute improvements

---

**Transform your GitHub issue creation workflow! 🚀**
