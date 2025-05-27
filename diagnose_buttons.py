"""
Diagnose button rendering issues
"""

import streamlit as st
from carbon_button import carbon_button, CarbonIcons
from carbon_button_styles import inject_carbon_styles, minimal_button

st.set_page_config(page_title="Button Diagnosis", page_icon="🔍")

st.title("🔍 Button Diagnosis")

# First, test WITHOUT custom styles
st.header("1. Raw Component (No Custom Styles)")
st.write("These should be visible but with default Streamlit styling:")

col1, col2, col3 = st.columns(3)

with col1:
    if carbon_button("Primary", CarbonIcons.UPLOAD, "raw1", button_type="primary"):
        st.success("Primary clicked!")

with col2:
    if carbon_button("Secondary", CarbonIcons.SAVE, "raw2", button_type="secondary"):
        st.success("Secondary clicked!")

with col3:
    if carbon_button("Danger", CarbonIcons.DELETE, "raw3", button_type="danger"):
        st.success("Danger clicked!")

st.divider()

# Now with custom styles
st.header("2. With Custom Styles")
inject_carbon_styles()

if minimal_button("Styled Button", CarbonIcons.UPLOAD, "styled1"):
    st.success("Styled button clicked!")

st.divider()

# Test if SVG is rendering
st.header("3. SVG Icon Test")
st.write("Can you see this icon directly?")
st.markdown(f"""
<div style="background: #f0f0f0; padding: 20px; border: 2px solid #333;">
    <p>Raw SVG Icon (should see upload arrow):</p>
    <div style="width: 32px; height: 32px; color: black;">
        {CarbonIcons.UPLOAD}
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# Test with very obvious styling
st.header("4. High Contrast Test")
st.markdown("""
<style>
.high-contrast button {
    background-color: #333 !important;
    color: white !important;
    border: 3px solid red !important;
    padding: 20px !important;
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="high-contrast">', unsafe_allow_html=True)
if carbon_button("HIGH CONTRAST", CarbonIcons.WARNING, "high_contrast"):
    st.success("High contrast clicked!")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# Test basic Streamlit button
st.header("5. Regular Streamlit Button")
if st.button("Regular Streamlit Button", key="regular"):
    st.success("Regular button works!")

st.divider()

# Debug info
st.header("6. Debug Information")
st.code(f"""
Icon length: {len(CarbonIcons.UPLOAD)}
Icon content (first 100 chars): {CarbonIcons.UPLOAD[:100]}...
Icon is string: {isinstance(CarbonIcons.UPLOAD, str)}
""")

# Component state check
st.header("7. Component State")
try:
    # Test if component is loading
    result = carbon_button("Test", "", "test_empty")
    st.write(f"Empty icon button returned: {result}")
except Exception as e:
    st.error(f"Component error: {e}")

st.info("""
**Please tell me:**
1. Which sections show visible buttons?
2. Can you see the raw SVG icon in section 3?
3. Does the high contrast button show up?
4. Any error messages in the browser console?
""")