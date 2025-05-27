"""
Simplest possible test of the Carbon Button Component
"""

import streamlit as st
from carbon_button import carbon_button

st.title("Simple Carbon Button Test")

# Test 1: Button with hardcoded SVG
st.write("Test 1: Hardcoded SVG")
simple_svg = '<svg viewBox="0 0 32 32"><rect x="8" y="8" width="16" height="16" fill="currentColor"/></svg>'

if carbon_button("Test with Simple SVG", simple_svg, key="test1"):
    st.success("Button clicked!")

# Test 2: Button without icon
st.write("Test 2: No Icon")
if carbon_button("No Icon", "", key="test2"):
    st.success("No icon button clicked!")

# Test 3: Button with text icon
st.write("Test 3: Text instead of SVG")
if carbon_button("Text Icon", "📤", key="test3"):
    st.success("Text icon button clicked!")

# Check what the component is receiving
st.write("---")
st.write("Debug: SVG content being passed:")
st.code(simple_svg)