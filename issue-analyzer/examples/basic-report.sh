#!/bin/bash
# Basic GitHub Issues Analysis Example

# Set your repository details
OWNER="microsoft"
REPO="vscode"

echo "📊 Basic GitHub Issues Report"
echo "============================="
echo "Repository: $OWNER/$REPO"
echo "Period: Last 30 days"
echo ""

# Check if main script exists
if [ ! -f "../github-issues-analyzer.py" ]; then
    echo "❌ github-issues-analyzer.py not found"
    echo "Please run this from the examples/ directory"
    exit 1
fi

# Generate basic console report
python3 ../github-issues-analyzer.py \
    --owner "$OWNER" \
    --repo "$REPO" \
    --days 30

echo ""
echo "💡 To export data:"
echo "   CSV: Add --format csv"
echo "   JSON: Add --format json"
