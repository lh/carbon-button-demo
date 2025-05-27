"""
Debug SVG passing between Python and React
"""

import streamlit as st
from carbon_button import carbon_button, CarbonIcons
import json

st.set_page_config(page_title="SVG Debug", page_icon="🔍")

st.title("🔍 SVG Debug Test")

# Show what we're passing
st.header("Python Side")
st.write("CarbonIcons.UPLOAD type:", type(CarbonIcons.UPLOAD))
st.write("CarbonIcons.UPLOAD length:", len(CarbonIcons.UPLOAD))
st.write("First 100 chars:")
st.code(CarbonIcons.UPLOAD[:100])

# Try different ways of passing the icon
st.header("Test Different Icon Formats")

# Test 1: Original
st.write("1. Original SVG string:")
if carbon_button("Test 1", CarbonIcons.UPLOAD, key="test1"):
    st.success("Clicked!")

# Test 2: Explicitly as string
st.write("2. Explicit string conversion:")
if carbon_button("Test 2", str(CarbonIcons.UPLOAD), key="test2"):
    st.success("Clicked!")

# Test 3: Simple SVG
st.write("3. Simple SVG:")
simple_svg = '<svg viewBox="0 0 32 32"><rect x="10" y="10" width="12" height="12" fill="currentColor"/></svg>'
if carbon_button("Test 3", simple_svg, key="test3"):
    st.success("Clicked!")

# Test 4: No icon
st.write("4. No icon (empty string):")
if carbon_button("Test 4", "", key="test4"):
    st.success("Clicked!")

# Test 5: JSON escaped
st.write("5. JSON escaped:")
escaped_svg = json.dumps(CarbonIcons.UPLOAD)[1:-1]  # Remove quotes
st.code(f"Escaped: {escaped_svg[:50]}...")
if carbon_button("Test 5", CarbonIcons.UPLOAD, key="test5"):
    st.success("Clicked!")

st.info("""
**Check the browser console for:**
- "Carbon Button Debug:" messages
- Look at `iconPreview` to see what the React component receives
- Check if the SVG string is intact or corrupted
""")