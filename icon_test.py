"""
Test icon rendering in Carbon Button Component
"""

import streamlit as st
from carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Icon Test", page_icon="🎨")

st.title("🎨 Icon Rendering Test")

# Test 1: Button with icon
st.header("Test 1: Button with Carbon Icon")
if carbon_button("Upload File", CarbonIcons.UPLOAD, key="upload"):
    st.success("Upload button clicked!")

# Test 2: Show the SVG content
st.header("Test 2: SVG Content")
st.write("Upload SVG content:")
st.code(CarbonIcons.UPLOAD)

# Test 3: Multiple buttons with icons
st.header("Test 3: Multiple Icon Buttons")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("Save", CarbonIcons.SAVE, key="save"):
        st.info("Save clicked!")

with col2:
    if carbon_button("Download", CarbonIcons.DOWNLOAD, key="download", button_type="secondary"):
        st.info("Download clicked!")

with col3:
    if carbon_button("Delete", CarbonIcons.DELETE, key="delete", button_type="danger"):
        st.error("Delete clicked!")

with col4:
    if carbon_button("Settings", CarbonIcons.SETTINGS, key="settings", button_type="ghost"):
        st.info("Settings clicked!")

# Test 4: Button without icon
st.header("Test 4: Button without Icon")
if carbon_button("No Icon", "", key="no_icon"):
    st.success("No icon button clicked!")

# Test 5: Custom SVG
st.header("Test 5: Custom SVG")
custom_svg = '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="10" fill="red"/></svg>'
if carbon_button("Custom", custom_svg, key="custom"):
    st.success("Custom icon button clicked!")

# Instructions
st.info("""
**What to check:**
1. Open browser DevTools (F12)
2. Go to Console tab
3. Look for "Button props:" logs
4. Check if iconLength > 0
5. Inspect the button element to see if SVG is in the DOM
""")