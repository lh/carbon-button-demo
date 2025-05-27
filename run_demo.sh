#!/bin/bash

echo "🚀 Starting Carbon Button Demo"
echo "=============================="

# Export the environment variable
export STREAMLIT_CARBON_BUTTON_DEV_MODE=true
echo "✅ Set STREAMLIT_CARBON_BUTTON_DEV_MODE=true"

# Change to the correct directory
cd "$(dirname "$0")"
echo "📁 Working directory: $(pwd)"

# Check if React dev server is running
if lsof -Pi :3000 -sTCP:LISTEN -t >/dev/null ; then
    echo "✅ React dev server is running on port 3000"
else
    echo "❌ React dev server is NOT running on port 3000"
    echo "Please run in another terminal:"
    echo "  cd frontend && npm start"
    exit 1
fi

# Run the demo
echo ""
echo "🎯 Starting Streamlit app..."
streamlit run awesome_demo.py