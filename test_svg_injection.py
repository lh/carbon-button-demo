"""
Test SVG injection methods
"""

import streamlit as st
from carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="SVG Injection Test", page_icon="🔬")

st.title("🔬 SVG Injection Test")

# First, verify SVG renders in regular Streamlit
st.header("1. Raw SVG in Streamlit Markdown")
st.markdown(f"""
<div style="display: flex; gap: 20px; align-items: center; background: #f0f0f0; padding: 20px;">
    <div style="width: 32px; height: 32px; color: blue;">
        {CarbonIcons.UPLOAD}
    </div>
    <div>This is the Upload icon rendered directly</div>
</div>
""", unsafe_allow_html=True)

# Test our component
st.header("2. Component Button")
if carbon_button("Upload Button", CarbonIcons.UPLOAD, key="upload_test"):
    st.success("Clicked!")

# Inspect what's happening
st.header("3. Debug Info")
st.code(f"""
SVG string length: {len(CarbonIcons.UPLOAD)}
First 150 chars: {CarbonIcons.UPLOAD[:150]}...
Contains <svg>: {CarbonIcons.UPLOAD.startswith('<svg')}
""")

# Different button styles
st.header("4. All Button Styles")
col1, col2, col3, col4 = st.columns(4)

with col1:
    carbon_button("Primary", CarbonIcons.SAVE, key="primary", button_type="primary")
    
with col2:
    carbon_button("Secondary", CarbonIcons.COPY, key="secondary", button_type="secondary")
    
with col3:
    carbon_button("Danger", CarbonIcons.DELETE, key="danger", button_type="danger")
    
with col4:
    carbon_button("Ghost", CarbonIcons.SETTINGS, key="ghost", button_type="ghost")

st.info("""
**What to check:**
1. Can you see the icon in section 1 (raw SVG)?
2. In browser DevTools, inspect a button element
3. Look for the span with class "carbon-button-icon"
4. Check what's inside that span
""")

# Add a test with a very simple SVG
st.header("5. Simple SVG Test")
simple_svg = '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="10" fill="red"/></svg>'
if carbon_button("Red Circle", simple_svg, key="simple"):
    st.success("Simple SVG clicked!")