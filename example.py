"""
Example app demonstrating the Carbon Button Component
"""

import streamlit as st
from carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Button Component Demo", page_icon="🎯", layout="wide")

st.title("🎯 Carbon Button Component Demo")
st.markdown("A **proper** Streamlit component - no checkboxes, no hacks!")

# Basic buttons
st.header("Basic Buttons")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("Upload", CarbonIcons.UPLOAD, key="upload1"):
        st.success("Upload clicked!")

with col2:
    if carbon_button("Download", CarbonIcons.DOWNLOAD, key="download1", button_type="secondary"):
        st.info("Download clicked!")

with col3:
    if carbon_button("Delete", CarbonIcons.DELETE, key="delete1", button_type="danger"):
        st.error("Delete clicked!")

with col4:
    if carbon_button("Settings", CarbonIcons.SETTINGS, key="settings1", button_type="ghost"):
        st.info("Settings clicked!")

st.divider()

# Full width buttons
st.header("Full Width Buttons")
col1, col2 = st.columns(2)

with col1:
    if carbon_button("Save Document", CarbonIcons.SAVE, key="save_full", use_container_width=True):
        st.success("Document saved!")

with col2:
    if carbon_button("Search", CarbonIcons.SEARCH, key="search_full", button_type="secondary", use_container_width=True):
        st.info("Searching...")

st.divider()

# Disabled buttons
st.header("Disabled State")
col1, col2, col3 = st.columns(3)

with col1:
    carbon_button("Disabled Primary", CarbonIcons.ADD, key="dis1", disabled=True)

with col2:
    carbon_button("Disabled Secondary", CarbonIcons.COPY, key="dis2", button_type="secondary", disabled=True)

with col3:
    carbon_button("Disabled Danger", CarbonIcons.DELETE, key="dis3", button_type="danger", disabled=True)

st.divider()

# Interactive demo
st.header("Interactive Demo")

button_type = st.selectbox("Button Type", ["primary", "secondary", "danger", "ghost"])
use_full_width = st.checkbox("Use container width")
is_disabled = st.checkbox("Disabled")

if carbon_button(
    "Custom Button", 
    CarbonIcons.ADD, 
    key="custom", 
    button_type=button_type,
    use_container_width=use_full_width,
    disabled=is_disabled
):
    st.balloons()
    st.success("Custom button clicked!")

st.divider()

# Component info
with st.expander("ℹ️ Component Information"):
    st.markdown("""
    ### This is a Real Streamlit Component!
    
    **What makes it different:**
    - Built with React and TypeScript
    - Proper bi-directional communication with Streamlit
    - No hidden checkboxes or CSS hacks
    - Full SVG icon support
    - Follows Carbon Design System specifications
    
    **How it works:**
    1. React component renders the button
    2. Click events are sent to Python via Streamlit's component API
    3. Python returns the click state
    4. Your app reacts to the button click
    
    **Benefits:**
    - Works in all browsers
    - No CSS compatibility issues
    - Proper accessibility support
    - Can be extended with more features
    - Published to PyPI for easy installation
    """)

st.divider()

# Development instructions
with st.expander("🛠️ Development Setup"):
    st.code("""
# 1. Install dependencies
cd frontend
npm install

# 2. Start React dev server
npm start

# 3. In another terminal, set dev mode
export STREAMLIT_CARBON_BUTTON_DEV_MODE=true

# 4. Run your Streamlit app
streamlit run example.py
    """, language="bash")

st.divider()
st.caption("Built with ❤️ using Streamlit Component API")