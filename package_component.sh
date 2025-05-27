#!/bin/bash

echo "📦 Packaging Carbon Button Component for Deployment"
echo "================================================"

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    echo "❌ Error: setup.py not found. Please run from the component root directory."
    exit 1
fi

# Check if frontend is built
if [ ! -d "carbon_button/frontend/static" ]; then
    echo "⚠️  Frontend not built. Building now..."
    cd frontend
    npm install
    npm run build
    cd ..
    
    # Copy built files
    echo "📋 Copying built files to package directory..."
    cp -r frontend/build/* carbon_button/frontend/
fi

# Clean up old builds
echo "🧹 Cleaning up old builds..."
rm -rf dist build *.egg-info

# Create source distribution
echo "📦 Creating source distribution..."
python setup.py sdist

# Create wheel distribution
echo "🎯 Creating wheel distribution..."
pip install --upgrade wheel
python setup.py bdist_wheel

echo "✅ Package created successfully!"
echo ""
echo "📍 Distribution files created in ./dist/"
echo ""
echo "To install locally for testing:"
echo "  pip install dist/streamlit_carbon_button-1.0.1-py3-none-any.whl"
echo ""
echo "To upload to PyPI:"
echo "  pip install twine"
echo "  twine upload dist/*"
echo ""
echo "For Streamlit Community Cloud deployment:"
echo "  - Include entire component directory in your repo"
echo "  - Add to requirements.txt: streamlit-carbon-button @ file:./carbon-button-component"