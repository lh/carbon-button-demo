"""
Test SVG rendering in different ways
"""

import streamlit as st
from carbon_button import carbon_button, CarbonIcons

st.title("SVG Rendering Test")

# Method 1: Direct SVG in markdown
st.header("Method 1: Direct SVG in Markdown")
st.markdown(f"""
<div style="display: flex; gap: 20px; align-items: center;">
    <div>
        <p>Upload Icon:</p>
        {CarbonIcons.UPLOAD}
    </div>
    <div>
        <p>Download Icon:</p>
        {CarbonIcons.DOWNLOAD}
    </div>
</div>
""", unsafe_allow_html=True)

# Method 2: SVG in component
st.header("Method 2: SVG in Component")
if carbon_button("Upload", CarbonIcons.UPLOAD, key="upload"):
    st.success("Upload clicked")

# Method 3: Check SVG string
st.header("Method 3: Inspect SVG String")
st.text("First 200 characters of Upload SVG:")
st.code(CarbonIcons.UPLOAD[:200])

# Method 4: Component with inline style
st.header("Method 4: Different SVG formats")

# Try different SVG formats
svg_formats = {
    "With xmlns": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="8" fill="currentColor"/></svg>',
    "Without xmlns": '<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="8" fill="currentColor"/></svg>',
    "With width/height": '<svg width="32" height="32" viewBox="0 0 32 32"><circle cx="16" cy="16" r="8" fill="currentColor"/></svg>',
    "Simple path": '<svg viewBox="0 0 32 32"><path d="M8 8h16v16H8z" fill="currentColor"/></svg>',
}

for name, svg in svg_formats.items():
    st.write(f"**{name}:**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div style="width: 32px; height: 32px;">{svg}</div>', unsafe_allow_html=True)
    with col2:
        if carbon_button(name, svg, key=f"format_{name}"):
            st.info(f"{name} clicked!")

# Method 5: Component with no icon
st.header("Method 5: Buttons without icons")
if carbon_button("Primary", "", key="no_icon_1"):
    st.info("Primary clicked")
if carbon_button("Secondary", "", key="no_icon_2", button_type="secondary"):
    st.info("Secondary clicked")