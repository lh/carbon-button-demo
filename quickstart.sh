#!/bin/bash

echo "🚀 Carbon Button Component Quick Start"
echo "====================================="
echo ""

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "❌ npm is required but not installed."
    echo "Please install Node.js and npm first."
    exit 1
fi

echo "📦 Installing frontend dependencies..."
cd frontend
npm install

echo ""
echo "🔧 Starting development servers..."
echo ""

# Start React dev server in background
echo "Starting React dev server on http://localhost:3000..."
npm start &
REACT_PID=$!

# Wait for React server to start
sleep 5

# Set development mode and run Streamlit
cd ..
echo ""
echo "Starting Streamlit app..."
export STREAMLIT_CARBON_BUTTON_DEV_MODE=true
streamlit run example.py

# Cleanup on exit
trap "kill $REACT_PID" EXIT