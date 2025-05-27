"""
Minimal test to debug component loading
"""

import streamlit as st
import os

st.title("Minimal Component Test")

# Show environment
st.write("Environment variable:", os.getenv("STREAMLIT_CARBON_BUTTON_DEV_MODE"))

# Try importing
try:
    from carbon_button import carbon_button
    st.success("✅ Import successful")
    
    # Try minimal button
    st.write("Creating button...")
    result = carbon_button("Click me", "", key="minimal")
    st.write(f"Button returned: {result}")
    
except Exception as e:
    st.error(f"❌ Error: {e}")
    import traceback
    st.code(traceback.format_exc())

# Instructions
st.info("""
**To run this test:**

1. Terminal 1:
```bash
cd frontend
npm start
```

2. Terminal 2:
```bash
export STREAMLIT_CARBON_BUTTON_DEV_MODE=true
streamlit run minimal_test.py
```

**Check:**
- Is React running on http://localhost:3000?
- Can you access http://localhost:3000 in your browser?
- Check browser console for errors
- Check Network tab for failed requests
""")