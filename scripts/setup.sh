#!/bin/bash
# GitHub Utilities Setup Script

echo "🛠️ GitHub Utilities Setup"
echo "========================="

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python version
echo -e "\n📍 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
    echo -e "${GREEN}✅ Python ${PYTHON_VERSION} found${NC}"
else
    echo -e "${RED}❌ Python 3 not found. Please install Python 3.7+${NC}"
    exit 1
fi

# Check pip
echo -e "\n📍 Checking pip..."
if command -v pip &> /dev/null; then
    echo -e "${GREEN}✅ pip found${NC}"
else
    echo -e "${RED}❌ pip not found. Please install pip${NC}"
    exit 1
fi

# Install dependencies
echo -e "\n📦 Installing dependencies..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Dependencies installed successfully${NC}"
else
    echo -e "${RED}❌ Failed to install dependencies${NC}"
    exit 1
fi

# Setup environment file
echo -e "\n🔑 Setting up environment..."
if [ ! -f ".env" ]; then
    cp issue-creator/env.example .env
    echo -e "${GREEN}✅ Environment file created${NC}"
    echo -e "${YELLOW}⚠️  Please edit .env and add your GitHub token${NC}"
else
    echo -e "${YELLOW}⚠️  .env file already exists${NC}"
fi

# Check git configuration
echo -e "\n🔧 Checking git configuration..."
GIT_NAME=$(git config --global user.name 2>/dev/null)
GIT_EMAIL=$(git config --global user.email 2>/dev/null)

if [ -n "$GIT_NAME" ] && [ -n "$GIT_EMAIL" ]; then
    echo -e "${GREEN}✅ Git configured: $GIT_NAME <$GIT_EMAIL>${NC}"
else
    echo -e "${YELLOW}⚠️  Git not fully configured${NC}"
    echo -e "${YELLOW}   Run: git config --global user.name 'Your Name'${NC}"
    echo -e "${YELLOW}   Run: git config --global user.email 'your@email.com'${NC}"
fi

# Test scripts
echo -e "\n🧪 Testing scripts..."
cd issue-creator/
if python3 github-issue-creator.py --help > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Issue Creator working${NC}"
else
    echo -e "${RED}❌ Issue Creator has issues${NC}"
fi

cd ../issue-analyzer/
if python3 github-issues-analyzer.py --help > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Issue Analyzer working${NC}"
else
    echo -e "${RED}❌ Issue Analyzer has issues${NC}"
fi

cd ..

echo -e "\n🎉 Setup Complete!"
echo -e "\n📚 Next Steps:"
echo -e "   1. Edit .env file with your GitHub token"
echo -e "   2. Read docs/getting-started.md"
echo -e "   3. Try the examples in each tool directory"
echo -e "\n🚀 Happy automating!"