#!/bin/bash

echo "Building Carbon Button Component..."

# Build the frontend
cd frontend
echo "Installing dependencies..."
npm install

echo "Building React app..."
npm run build

# Copy build files to Python package
echo "Copying build files..."
rm -rf ../carbon_button/frontend
mkdir -p ../carbon_button/frontend

# Copy the built static files
cp -r build/* ../carbon_button/frontend/

echo "Build complete!"
echo ""
echo "To install the component:"
echo "  pip install ."
echo ""
echo "To use in development mode:"
echo "  export STREAMLIT_CARBON_BUTTON_DEV_MODE=true"
echo "  cd frontend && npm start"