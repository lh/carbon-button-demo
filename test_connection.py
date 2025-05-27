"""
Test if the component is connecting properly
"""

import streamlit as st
import os

st.title("Component Connection Test")

# Check environment
env_var = os.getenv("STREAMLIT_CARBON_BUTTON_DEV_MODE")
st.write(f"Environment variable STREAMLIT_CARBON_BUTTON_DEV_MODE: `{env_var}`")

if env_var != "true":
    st.error("❌ Environment variable not set correctly!")
    st.code("""
    export STREAMLIT_CARBON_BUTTON_DEV_MODE=true
    streamlit run test_connection.py
    """)
else:
    st.success("✅ Environment variable is set")

# Test import
try:
    from carbon_button import carbon_button, CarbonIcons
    st.success("✅ Import successful")
except Exception as e:
    st.error(f"❌ Import failed: {e}")
    st.stop()

# Test component declaration
try:
    from carbon_button import _component_func
    st.write("Component function:", _component_func)
    st.write("Component URL/path:", _component_func._url if hasattr(_component_func, '_url') else 'No URL attribute')
except Exception as e:
    st.error(f"Cannot access component internals: {e}")

# Simple button test
st.header("Simple Button Test")

# Test with no icon first
clicked = carbon_button("Test Button (No Icon)", "", key="test_no_icon")
st.write(f"Button clicked: {clicked}")

# Test with simple string
clicked2 = carbon_button("Test Button 2", "ABC", key="test_string")  
st.write(f"Button 2 clicked: {clicked2}")

st.divider()

st.info("""
**Troubleshooting:**

1. Make sure React dev server is running:
   - Go to http://localhost:3000 in your browser
   - You should see the React app

2. Check browser console (F12) for errors

3. Try killing all processes and restart:
   ```bash
   # Kill existing processes
   pkill -f "streamlit run"
   pkill -f "npm start"
   
   # Terminal 1:
   cd frontend
   npm start
   
   # Terminal 2:
   export STREAMLIT_CARBON_BUTTON_DEV_MODE=true
   streamlit run test_connection.py
   ```
""")