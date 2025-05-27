"""
Debug test for Carbon Button Component
"""

import streamlit as st
from carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Button Debug", page_icon="🔍")

st.title("🔍 Carbon Button Debug Test")

# Test 1: Basic button
st.header("Test 1: Basic Button")
if carbon_button("Test Button", CarbonIcons.UPLOAD, key="test1"):
    st.success("Button clicked!")

# Test 2: Check what's being passed
st.header("Test 2: Icon Content")
st.code(CarbonIcons.UPLOAD[:100] + "...")  # Show first 100 chars

# Test 3: Button without icon
st.header("Test 3: Button without icon")
if carbon_button("No Icon Button", "", key="test2"):
    st.success("No icon button clicked!")

# Test 4: Simple SVG test
st.header("Test 4: Direct SVG in Streamlit")
st.markdown(f"""
<div style="width: 32px; height: 32px;">
{CarbonIcons.UPLOAD}
</div>
""", unsafe_allow_html=True)

# Test 5: All button types
st.header("Test 5: All Button Types")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("Primary", CarbonIcons.ADD, key="type1"):
        st.info("Primary clicked")

with col2:
    if carbon_button("Secondary", CarbonIcons.COPY, key="type2", button_type="secondary"):
        st.info("Secondary clicked")

with col3:
    if carbon_button("Danger", CarbonIcons.DELETE, key="type3", button_type="danger"):
        st.info("Danger clicked")

with col4:
    if carbon_button("Ghost", CarbonIcons.SETTINGS, key="type4", button_type="ghost"):
        st.info("Ghost clicked")

# Test 6: Component communication check
st.header("Test 6: Component Value Check")
click_count = carbon_button("Click Counter", CarbonIcons.ADD, key="counter")
st.write(f"Component returned: {click_count}")

# Test 7: Manual SVG
st.header("Test 7: Manual SVG String")
manual_svg = '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="10" fill="currentColor"/></svg>'
if carbon_button("Manual SVG", manual_svg, key="manual"):
    st.success("Manual SVG button clicked!")

# Show all available icons
st.header("Available Icons")
icon_list = [attr for attr in dir(CarbonIcons) if not attr.startswith('_')]
st.write(f"Total icons available: {len(icon_list)}")
st.write("Icons:", icon_list)