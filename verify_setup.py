"""
Verify Carbon Button Component Setup
"""

import os
import streamlit as st
import streamlit.components.v1 as components

st.title("🔍 Component Setup Verification")

# Check environment variable
st.header("1. Environment Variable")
dev_mode = os.getenv("STREAMLIT_CARBON_BUTTON_DEV_MODE", "not set")
st.write(f"STREAMLIT_CARBON_BUTTON_DEV_MODE = `{dev_mode}`")

if dev_mode.lower() != "true":
    st.error("❌ Dev mode is not enabled!")
    st.code("export STREAMLIT_CARBON_BUTTON_DEV_MODE=true")
else:
    st.success("✅ Dev mode is enabled")

# Check if we can access localhost:3000
st.header("2. React Dev Server")
st.write("The React dev server should be running on http://localhost:3000")
st.write("You can verify by visiting: http://localhost:3000")

# Try a simple component
st.header("3. Simple Component Test")
st.write("Testing basic Streamlit component functionality...")

# Create a minimal test component
test_component = components.declare_component(
    "test_component",
    url="http://localhost:3000"
)

# Try to render it
try:
    result = test_component(test="hello", key="test_key")
    st.success("✅ Component rendered successfully!")
    st.write(f"Component returned: {result}")
except Exception as e:
    st.error(f"❌ Component failed to render: {e}")

# Import and test our component
st.header("4. Carbon Button Import Test")
try:
    from carbon_button import carbon_button, CarbonIcons
    st.success("✅ Import successful")
    
    # Check what the component function looks like
    st.write("Component function:", carbon_button.__module__)
    
    # Try to use it
    st.write("Attempting to render a button...")
    clicked = carbon_button("Test Button", "", key="import_test")
    if clicked:
        st.success("Button clicked!")
        
except Exception as e:
    st.error(f"❌ Import failed: {e}")
    import traceback
    st.code(traceback.format_exc())

# Manual instructions
st.header("📋 Manual Setup Checklist")
st.markdown("""
1. **Terminal 1 - React Dev Server:**
   ```bash
   cd carbon-button-component/frontend
   npm install  # if not done yet
   npm start    # should run on port 3000
   ```

2. **Terminal 2 - Streamlit App:**
   ```bash
   cd carbon-button-component
   export STREAMLIT_CARBON_BUTTON_DEV_MODE=true
   pip install -e .  # Install package in development mode
   streamlit run verify_setup.py
   ```

3. **Check Browser:**
   - Open http://localhost:3000 - you should see the React app
   - Check browser console (F12) for any errors
   - Check Network tab to see if Streamlit is trying to connect
""")

# Show current working directory
st.header("5. File Paths")
st.write(f"Current working directory: {os.getcwd()}")
st.write(f"Python file location: {__file__}")

# Check if package is installed
st.header("6. Package Installation")
try:
    import carbon_button
    st.success(f"✅ carbon_button package found at: {carbon_button.__file__}")
except ImportError:
    st.error("❌ carbon_button package not found. Run: pip install -e .")