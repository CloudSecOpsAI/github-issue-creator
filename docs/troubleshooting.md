# 🔧 Troubleshooting Guide

Common issues and solutions for GitHub Utilities toolkit.

## 🚨 Quick Diagnostics

Run this diagnostic script to identify common issues:

```bash
# Navigate to your github-utilities directory
cd github-utilities

# Run diagnostic checks
echo "🔍 GitHub Utilities Diagnostics"
echo "==============================="

# Check Python version
echo "Python: $(python3 --version 2>/dev/null || echo 'Not found')"

# Check dependencies
echo "Dependencies:"
pip list | grep -E "(requests|python-dotenv)" || echo "Missing dependencies"

# Check environment
echo "Environment:"
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('GITHUB_TOKEN')
print(f'  GITHUB_TOKEN: {\"Set\" if token else \"Not set\"} ({len(token) if token else 0} chars)')
"

# Check Git config
echo "Git config:"
echo "  Name: $(git config --global user.name || echo 'Not set')"
echo "  Email: $(git config --global user.email || echo 'Not set')"
```

---

## 🐛 Common Issues

### **Authentication Problems**

#### ❌ "Bad credentials" Error
```bash
Error: 401 Client Error: Unauthorized for url: https://api.github.com/repos/...
```

**Solutions:**
1. **Check token validity:**
   ```bash
   curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
   ```

2. **Verify .env file:**
   ```bash
   cat .env | grep GITHUB_TOKEN
   # Should show: GITHUB_TOKEN=your_token_here
   ```

3. **Regenerate token:**
   - Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
   - Delete old token, create new one with `repo` scope

#### ❌ "Token not set" Error
```bash
❌ GITHUB_TOKEN not set. Please set it in .env file or environment variable.
```

**Solutions:**
1. **Create .env file:**
   ```bash
   echo "GITHUB_TOKEN=your_token_here" > .env
   ```

2. **Check file location:**
   ```bash
   # .env should be in the same directory as the script
   ls -la .env
   ```

3. **Export manually:**
   ```bash
   export GITHUB_TOKEN="your_token_here"
   ```

### **Repository Access Issues**

#### ❌ "Repository not found" Error
```bash
Error: 404 Client Error: Not Found for url: https://api.github.com/repos/owner/repo
```

**Solutions:**
1. **Verify repository details:**
   ```bash
   # Check if repository exists and is accessible
   curl -H "Authorization: token YOUR_TOKEN" \
     https://api.github.com/repos/OWNER/REPO
   ```

2. **Check repository name:**
   - Ensure correct spelling: `owner/repository-name`
   - Check if repository is private (requires appropriate token scopes)

3. **Verify token scopes:**
   - Token needs `repo` scope for private repositories
   - Token needs `public_repo` scope for public repositories

#### ❌ "Resource not accessible" Error
```bash
Error: 403 Client Error: Forbidden - Resource not accessible by personal access token
```

**Solutions:**
1. **Add required scopes to token:**
   - Go to [GitHub Settings → Tokens](https://github.com/settings/tokens)
   - Edit token and add `repo` scope

2. **Check organization restrictions:**
   - Some organizations require token approval
   - Contact organization admin if needed

### **Python and Dependencies**

#### ❌ "Module not found" Error
```bash
ModuleNotFoundError: No module named 'requests'
```

**Solutions:**
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Check Python environment:**
   ```bash
   # Make sure you're using the right Python
   which python3
   python3 -m pip install requests python-dotenv
   ```

3. **Use virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

#### ❌ "Permission denied" Error
```bash
PermissionError: [Errno 13] Permission denied
```

**Solutions:**
1. **Use user installation:**
   ```bash
   pip install --user -r requirements.txt
   ```

2. **Fix file permissions:**
   ```bash
   chmod +x scripts/setup.sh
   ```

3. **Use virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### **Configuration Issues**

#### ❌ "Invalid JSON configuration" Error
```bash
JSONDecodeError: Expecting ',' delimiter: line 5 column 1
```

**Solutions:**
1. **Validate JSON syntax:**
   ```bash
   python3 -m json.tool config-examples/basic-config.json
   ```

2. **Common JSON fixes:**
   - Remove trailing commas
   - Use double quotes, not single quotes
   - Escape special characters properly

3. **Use provided examples:**
   ```bash
   cp config-examples/basic-config.json my-config.json
   # Edit my-config.json carefully
   ```

#### ❌ "File not found" Error
```bash
FileNotFoundError: [Errno 2] No such file or directory: 'items.txt'
```

**Solutions:**
1. **Check file path:**
   ```bash
   ls -la items.txt
   # Use absolute path if needed
   python3 github-issue-creator.py --file /full/path/to/items.txt
   ```

2. **Verify working directory:**
   ```bash
   pwd
   # Should be in the correct tool directory
   ```

### **Rate Limiting**

#### ❌ "API rate limit exceeded" Error
```bash
Error: 403 Client Error: Forbidden - API rate limit exceeded
```

**Solutions:**
1. **Check rate limit status:**
   ```bash
   curl -H "Authorization: token YOUR_TOKEN" \
     https://api.github.com/rate_limit
   ```

2. **Wait for reset:**
   - Authenticated: 5000 requests/hour
   - Unauthenticated: 60 requests/hour
   - Wait for `X-RateLimit-Reset` time

3. **Use smaller batches:**
   ```bash
   # Process items in smaller batches
   python3 github-issue-creator.py --file small-batch.txt
   ```

### **Git and GitHub CLI Issues**

#### ❌ "Git not configured" Warning
```bash
⚠️ Git not fully configured
```

**Solutions:**
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

#### ❌ "GitHub CLI not authenticated"
```bash
To get started with GitHub CLI, please run: gh auth login
```

**Solutions:**
```bash
gh auth login
# Follow the prompts to authenticate
```

---

## 🔍 Advanced Debugging

### **Enable Debug Mode**
```bash
# Add to your script for verbose output
export DEBUG=1
python3 github-issue-creator.py --config config.json --file items.txt
```

### **Test API Connection**
```bash
# Basic API test
curl -H "Authorization: token YOUR_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user

# Test repository access
curl -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/repos/OWNER/REPO
```

### **Check Network Connectivity**
```bash
# Test GitHub connectivity
ping github.com

# Test API endpoint
curl -I https://api.github.com
```

---

## 📋 Environment Checklist

Before reporting issues, verify:

- [ ] **Python 3.7+** installed
- [ ] **Dependencies** installed (`pip install -r requirements.txt`)
- [ ] **GitHub token** created with correct scopes
- [ ] **Environment variable** set (`GITHUB_TOKEN`)
- [ ] **Repository** exists and is accessible
- [ ] **Network** connection to github.com
- [ ] **Git** configured (name and email)
- [ ] **JSON configuration** files are valid

---

## 🆘 Getting Help

### **Before Asking for Help**
1. Run the diagnostic script above
2. Check this troubleshooting guide
3. Search existing [GitHub Issues](https://github.com/CloudSecOpsAI/github-utilities/issues)

### **When Reporting Issues**
Include this information:
```bash
# System information
echo "OS: $(uname -s)"
echo "Python: $(python3 --version)"
echo "Tool: $(basename $PWD)"

# Error details
echo "Error message: [paste full error]"
echo "Command run: [paste exact command]"
echo "Expected: [describe expected behavior]"
echo "Actual: [describe what happened]"
```

### **Support Channels**
- **[GitHub Issues](https://github.com/CloudSecOpsAI/github-utilities/issues)** - Bug reports and feature requests
- **[GitHub Discussions](https://github.com/CloudSecOpsAI/github-utilities/discussions)** - Questions and community help
- **[Documentation](README.md)** - Complete usage guides

---

## 📚 Additional Resources

- **[GitHub API Documentation](https://docs.github.com/en/rest)**
- **[Personal Access Token Guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)**
- **[Python Requests Documentation](https://docs.python-requests.org/)**
- **[JSON Syntax Guide](https://www.json.org/)**

---

**🛠️ Most issues are resolved by checking authentication and dependencies!**
