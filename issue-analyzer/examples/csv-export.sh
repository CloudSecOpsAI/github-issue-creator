#!/bin/bash
# CSV Export Example for GitHub Issues Analysis

# Configuration
OWNER="facebook"
REPO="react"
LABELS="bug,enhancement"

echo "📊 CSV Export Example"
echo "===================="
echo "Repository: $OWNER/$REPO"
echo "Labels: $LABELS"
echo "Period: Last 60 days"
echo "Format: CSV Export"
echo ""

# Check if main script exists
if [ ! -f "../github-issues-analyzer.py" ]; then
    echo "❌ github-issues-analyzer.py not found"
    echo "Please run this from the examples/ directory"
    exit 1
fi

# Generate CSV report
echo "🔄 Generating CSV report..."
python3 ../github-issues-analyzer.py \
    --owner "$OWNER" \
    --repo "$REPO" \
    --labels "$LABELS" \
    --days 60 \
    --format csv

echo ""
echo "✅ CSV file generated!"
echo "💡 You can now:"
echo "   • Open the CSV in Excel/Google Sheets"
echo "   • Import into data analysis tools"
echo "   • Use for reporting dashboards"
