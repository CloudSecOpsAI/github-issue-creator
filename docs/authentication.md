# 🔑 Authentication Guide

Complete guide to setting up GitHub authentication for the GitHub Utilities toolkit.

## 🎯 Overview

GitHub Utilities uses **GitHub Personal Access Tokens (PAT)** for authentication. This guide covers:
- Creating and configuring tokens
- Setting up environment variables
- Security best practices
- Troubleshooting authentication issues

## 🛠️ Creating a Personal Access Token

### Method 1: GitHub Web Interface (Recommended)

1. **Navigate to GitHub Settings**
   - Go to [GitHub.com](https://github.com)
   - Click your profile picture → **Settings**
   - Scroll down to **Developer settings**
   - Click **Personal access tokens** → **Tokens (classic)**

2. **Generate New Token**
   - Click **"Generate new token (classic)"**
   - Give it a descriptive name: `GitHub Utilities - [Your Machine]`
   - Set expiration (recommended: 90 days for security)

3. **Select Required Scopes**
   ```
   ✅ repo                    # Full control of private repositories
   ✅ read:org               # Read organization membership
   ✅ workflow               # Update GitHub Action workflows (future use)
   ✅ read:user              # Read user profile data
   ✅ user:email             # Access user email addresses
   ```

4. **Generate and Copy Token**
   - Click **"Generate token"**
   - **⚠️ IMPORTANT**: Copy the token immediately - you won't see it again!

### Method 2: GitHub CLI (Advanced)
```bash
# Install GitHub CLI first: https://cli.github.com/
gh auth login --scopes repo,read:org,workflow,read:user,user:email
```

## 🔧 Environment Setup

### Option 1: .env File (Recommended)
```bash
# In your project root
cp issue-creator/env.example .env

# Edit .env file
echo "GITHUB_TOKEN=your_token_here" > .env
```

### Option 2: System Environment Variables
```bash
# Linux/macOS
export GITHUB_TOKEN="your_token_here"
echo 'export GITHUB_TOKEN="your_token_here"' >> ~/.bashrc

# Windows PowerShell
$env:GITHUB_TOKEN="your_token_here"
[Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "your_token_here", "User")
```

### Option 3: Command Line Arguments
```bash
# Pass token directly (less secure)
python github-issue-creator.py --token your_token_here --config config.json
```

## 🔒 Security Best Practices

### ✅ Do's
- **Use descriptive token names** with machine/purpose info
- **Set reasonable expiration dates** (30-90 days)
- **Use minimum required scopes** for your use case
- **Store tokens in .env files** (not in code)
- **Add .env to .gitignore** to prevent accidental commits
- **Rotate tokens regularly**
- **Use different tokens** for different projects/machines

### ❌ Don'ts
- **Never commit tokens to git repositories**
- **Don't share tokens** in chat, email, or documentation
- **Avoid tokens with unnecessary scopes**
- **Don't use tokens in CI/CD logs**
- **Don't store tokens in plain text files** in shared locations

## 🧪 Testing Your Authentication

### Quick Test Script
```bash
# Test environment loading
cd github-utilities
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('GITHUB_TOKEN')
print('✅ Token found' if token else '❌ Token not found')
print(f'Token length: {len(token) if token else 0}')
"
```

### Test API Access
```bash
# Test with issue analyzer
cd issue-analyzer/
python github-issues-analyzer.py --owner microsoft --repo vscode --days 1

# Test with issue creator (dry run)
cd ../issue-creator/
python github-issue-creator.py --config config-examples/basic-config.json --dry-run
```

## 🔍 Scope Explanations

| Scope | Purpose | Required For |
|-------|---------|--------------|
| `repo` | Full repository access | Creating/reading issues, accessing private repos |
| `read:org` | Read organization data | Organization-owned repositories |
| `workflow` | GitHub Actions access | Future automation features |
| `read:user` | Read user profile | User information in reports |
| `user:email` | Access email addresses | Assignee/author email lookup |

## 🚨 Troubleshooting

### Token Not Working
```bash
# Check if token is loaded
python -c "import os; print('GITHUB_TOKEN' in os.environ)"

# Test token validity
curl -H "Authorization: token YOUR_TOKEN" https://api.github.com/user
```

### Common Error Messages

**"Bad credentials"**
- Token is invalid or expired
- Token not properly set in environment
- Solution: Generate new token, check .env file

**"Not Found" for public repositories**
- Token lacks required scopes
- Repository name/owner incorrect
- Solution: Add `repo` scope, verify repository details

**"API rate limit exceeded"**
- Too many requests in short time
- Solution: Wait for rate limit reset, use authenticated requests

**"Resource not accessible by personal access token"**
- Token lacks required scope for operation
- Solution: Add necessary scopes to token

## 🔄 Token Rotation

### When to Rotate
- **Scheduled rotation**: Every 90 days
- **Security incident**: Immediately if token may be compromised
- **Scope changes**: When you need different permissions
- **Team changes**: When team members leave

### Rotation Process
1. Generate new token with same scopes
2. Test new token in development environment
3. Update .env file with new token
4. Revoke old token in GitHub settings
5. Update any external services using the token

## 📱 Organization Tokens (Advanced)

For organization-wide automation:
1. Use **GitHub Apps** instead of personal tokens
2. Request organization owner to create **organizational tokens**
3. Use **service accounts** with dedicated tokens

## 🌐 Enterprise Considerations

### GitHub Enterprise Server
```bash
# Set custom API endpoint
export GITHUB_API_URL="https://github.yourdomain.com/api/v3"
```

### SAML/SSO Organizations
- Enable **SSO for your token** in organization settings
- Token must be **authorized for SSO** before use

## 📚 Additional Resources

- **[GitHub Token Documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)**
- **[GitHub API Authentication](https://docs.github.com/en/rest/authentication)**
- **[GitHub CLI Authentication](https://cli.github.com/manual/gh_auth_login)**
- **[Security Best Practices](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure)**

---

**🔐 Keep your tokens secure and rotate them regularly!**
