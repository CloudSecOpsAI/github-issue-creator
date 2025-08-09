#!/bin/bash
# Example script for creating GitHub issues

echo "🚀 GitHub Issue Creator - Example Usage"
echo "======================================"

# Check if main script exists
if [ ! -f "../github-issue-creator.py" ]; then
    echo "❌ github-issue-creator.py not found"
    echo "Please run this from the examples/ directory"
    exit 1
fi

echo "📝 Available configurations:"
echo "1. Basic features (../config-examples/basic-config.json)"
echo "2. Feature requests (../config-examples/feature-requests.json)"
echo "3. Compliance tracking (../config-examples/compliance-tracking.json)"
echo ""

echo "Choose an example (1-3):"
read -r choice

case $choice in
    1)
        CONFIG="../config-examples/basic-config.json"
        echo "🔧 Using basic configuration..."
        ;;
    2)
        CONFIG="../config-examples/feature-requests.json"
        echo "🔧 Using feature requests configuration..."
        ;;
    3)
        CONFIG="../config-examples/compliance-tracking.json"
        echo "🔧 Using compliance tracking configuration..."
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "📋 Running dry-run test with $CONFIG"
echo "============================================"

# Run dry-run first
python3 ../github-issue-creator.py --config "$CONFIG" --file sample-items.txt --dry-run

echo ""
echo "💡 To actually create issues, run:"
echo "python3 ../github-issue-creator.py --config $CONFIG --file sample-items.txt --no-dry-run"
