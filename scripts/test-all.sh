#!/bin/bash
# GitHub Utilities - Test All Tools

echo "🧪 GitHub Utilities - Test Suite"
echo "================================"
echo ""

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Run setup.sh first."
    exit 1
fi

# Source environment
source .env

# Check if GitHub token is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ GITHUB_TOKEN not set in .env file."
    echo "Please add your GitHub token to .env and try again."
    exit 1
fi

echo "✅ Environment check passed"
echo ""

# Test Issue Creator
echo "🔍 Testing Issue Creator..."
echo "============================"
cd issue-creator
if python3 github-issue-creator.py --config config-examples/basic-config.json --file examples/sample-items.txt --dry-run; then
    echo "✅ Issue Creator test passed"
else
    echo "❌ Issue Creator test failed"
fi
cd ..
echo ""

# Test Issue Analyzer
echo "🔍 Testing Issue Analyzer..."
echo "============================="
cd issue-analyzer
if python3 github-issues-analyzer.py --owner microsoft --repo vscode --days 7 | head -20; then
    echo "✅ Issue Analyzer test passed"
else
    echo "❌ Issue Analyzer test failed"
fi
cd ..
echo ""

echo "🎉 Test suite completed!"
echo ""
echo "💡 If tests passed, you're ready to use GitHub Utilities!"
echo "📚 See README.md for full documentation and usage examples."
