# 📊 GitHub Issues Analyzer

A comprehensive Python tool to analyze and generate detailed reports from closed GitHub issues. Perfect for tracking team performance, analyzing issue resolution patterns, and generating insights for project management.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

---

## ✨ Features

- 🔍 **Advanced Filtering**: Filter by labels, date ranges, assignees, and more
- 📊 **Multiple Export Formats**: Console display, CSV, and JSON exports
- 📈 **Comprehensive Analytics**:
  - Issues by labels, assignees, and authors
  - Time-based trends (monthly, weekly)
  - Average resolution times
  - Label combination analysis
- ⚡ **Efficient Processing**: Smart pagination and API optimization
- 🔄 **Flexible Date Ranges**: Last N days, custom periods, or specific dates

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- GitHub Personal Access Token
- Required packages: `requests`, `python-dotenv`

### Installation
```bash
git clone <your-repo-url>
cd github-issues-analyzer
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
# Console report for last 30 days
python github-issues-analyzer.py --owner myorg --repo myrepo

# Export to CSV with specific labels
python github-issues-analyzer.py --owner myorg --repo myrepo --labels "bug,enhancement" --format csv

# Custom date range with JSON export
python github-issues-analyzer.py --owner myorg --repo myrepo --since 2024-01-01 --until 2024-03-31 --format json
```

---

## 📋 Command Options

| Option | Required | Description | Example |
|--------|----------|-------------|---------|
| `--owner` | ✅ | Repository owner/organization | `--owner microsoft` |
| `--repo` | ✅ | Repository name | `--repo vscode` |
| `--labels` | ❌ | Comma-separated labels | `--labels "bug,enhancement"` |
| `--days` | ❌ | Days to look back (default: 30) | `--days 90` |
| `--since` | ❌ | Start date (YYYY-MM-DD) | `--since 2024-01-01` |
| `--until` | ❌ | End date (YYYY-MM-DD) | `--until 2024-03-31` |
| `--format` | ❌ | Output: console/csv/json | `--format csv` |
| `--token` | ❌ | GitHub token (or use .env) | `--token ghp_xxx` |

---

## 📊 Sample Output

### Console Report
```
📊 GITHUB ISSUES ANALYSIS REPORT
📁 Repository: microsoft/vscode
📅 Generated: 2024-08-07 19:18:38

📈 SUMMARY STATISTICS
   Total Closed Issues: 156
   Average Days to Close: 12.3 days

🏷️ ISSUES BY LABEL
   bug: 89 (57.1%)
   enhancement: 34 (21.8%)
   documentation: 18 (11.5%)
   good-first-issue: 15 (9.6%)

👥 ISSUES BY ASSIGNEE
   contributor1: 45 (28.8%)
   contributor2: 32 (20.5%)
   contributor3: 28 (17.9%)

🔗 TOP LABEL COMBINATIONS
   [bug]: 56 (35.9%)
   [enhancement]: 23 (14.7%)
   [bug, high-priority]: 12 (7.7%)
```

### CSV Export
Generated files include detailed issue data:
- Issue number, title, author
- Assignees and labels
- Creation and closure dates
- Time to resolution
- Direct GitHub URLs

### JSON Export
Structured data perfect for:
- Dashboard integration
- Automated reporting
- API consumption
- Data analysis pipelines

---

## 🎯 Use Cases

### 1. Team Performance Analysis
```bash
# Monthly team report
python github-issues-analyzer.py --owner myorg --repo myrepo --days 30 --format csv
```

### 2. Bug Tracking
```bash
# Analyze bug resolution patterns
python github-issues-analyzer.py --owner myorg --repo myrepo --labels "bug" --days 90
```

### 3. Sprint Retrospectives
```bash
# Specific sprint period
python github-issues-analyzer.py --owner myorg --repo myrepo --since 2024-07-01 --until 2024-07-14
```

### 4. Label-Specific Analysis
```bash
# High-priority issues
python github-issues-analyzer.py --owner myorg --repo myrepo --labels "priority-high,critical"
```

### 5. Long-term Trends
```bash
# Quarterly analysis with JSON export
python github-issues-analyzer.py --owner myorg --repo myrepo --days 90 --format json
```

---

## 📁 Examples

Check the `examples/` directory for ready-to-run scripts:

```bash
# Basic report example
./examples/basic-report.sh

# CSV export example
./examples/csv-export.sh

# Advanced analysis example
./examples/advanced-analysis.sh
```

---

## 🔧 Advanced Usage

### Environment Variables
```bash
# Set token via environment
export GITHUB_TOKEN=your_token_here

# Or use .env file (recommended)
echo "GITHUB_TOKEN=your_token_here" > .env
```

### Label Filtering Tips
```bash
# Multiple labels (issues with ANY of these labels)
--labels "bug,enhancement,documentation"

# Labels with special characters (use quotes)
--labels "good-first-issue,help-wanted"

# Complex label names
--labels "customer:enterprise,priority:high"
```

### Date Range Examples
```bash
# Last week
--days 7

# Last quarter
--days 90

# Specific month
--since 2024-07-01 --until 2024-07-31

# Year-to-date
--since 2024-01-01
```

---

## 🐛 Troubleshooting

### Common Issues

**Authentication Error**
```
❌ Missing GitHub token
```
**Solution**: Set `GITHUB_TOKEN` in `.env` file or environment

**No Issues Found**
```
ℹ️ No issues found matching the criteria
```
**Solutions**:
- Check repository name and owner
- Verify label names (case-sensitive)
- Try longer time period
- Remove label filters to see all issues

**Rate Limit**
```
❌ Failed to fetch issues: 403
```
**Solution**: Wait for rate limit reset or use narrower date range

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you find this tool helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Suggesting features
- 🤝 Contributing code

---

**Made with ❤️ for the GitHub community**
