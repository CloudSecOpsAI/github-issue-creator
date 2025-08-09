#!/bin/bash
# Advanced Analysis Example with Custom Date Ranges

# Configuration
OWNER="google"
REPO="kubernetes"
START_DATE="2024-01-01"
END_DATE="2024-03-31"

echo "📊 Advanced GitHub Issues Analysis"
echo "================================="
echo "Repository: $OWNER/$REPO"
echo "Period: $START_DATE to $END_DATE"
echo "Format: JSON Export for Dashboard"
echo ""

# Check if main script exists
if [ ! -f "../github-issues-analyzer.py" ]; then
    echo "❌ github-issues-analyzer.py not found"
    echo "Please run this from the examples/ directory"
    exit 1
fi

echo "🔄 Generating quarterly analysis..."

# Generate comprehensive JSON report
python3 ../github-issues-analyzer.py \
    --owner "$OWNER" \
    --repo "$REPO" \
    --since "$START_DATE" \
    --until "$END_DATE" \
    --format json

echo ""
echo "✅ Advanced analysis complete!"
echo ""
echo "💡 Use this JSON data for:"
echo "   • Dashboard integration"
echo "   • Automated reporting"
echo "   • Data pipeline processing"
echo "   • API consumption"
