"""
Test button visibility with updated colors
"""

import streamlit as st
from carbon_button_styles import inject_carbon_styles, minimal_button, CarbonIcons

st.set_page_config(page_title="Button Visibility Test", page_icon="👁️")

# Inject styles
inject_carbon_styles()

st.title("👁️ Button Visibility Test")

# Add a colored background to see button contrast
st.markdown("""
<style>
.main > div {
    padding: 2rem;
    background-color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
### Updated Colors:
- **Normal**: Light grey (#f0f0f0) with shadow
- **Hover**: White (#ffffff) with elevated shadow  
- **Click**: Darker grey (#d0d0d0) with compressed shadow
""")

# Simple button test
st.header("Can you see these buttons?")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Minimal Button:**")
    if minimal_button("Click Me", CarbonIcons.UPLOAD, "vis1"):
        st.success("You found me!")

with col2:
    st.markdown("**Icon Only:**")
    if minimal_button("", CarbonIcons.SETTINGS, "vis2"):
        st.info("Icon clicked!")

with col3:
    st.markdown("**Full Width:**")
    if minimal_button("Full Width", CarbonIcons.SAVE, "vis3", use_container_width=True):
        st.success("Wide button clicked!")

# Color contrast demo
st.header("Color Contrast Demo")

# Create different background colors to test contrast
bg_colors = {
    "White": "#ffffff",
    "Light Grey": "#f8f8f8", 
    "Medium Grey": "#e8e8e8",
    "Dark Grey": "#d0d0d0"
}

for bg_name, bg_color in bg_colors.items():
    st.markdown(f"""
    <div style="background-color: {bg_color}; padding: 1rem; margin: 0.5rem 0; border-radius: 4px;">
        <p style="margin: 0 0 0.5rem 0; color: #000;">Background: {bg_name} ({bg_color})</p>
    </div>
    """, unsafe_allow_html=True)
    
    if minimal_button(f"Button on {bg_name}", CarbonIcons.ADD, f"bg_{bg_name}"):
        st.info(f"Clicked on {bg_name} background!")

# Direct comparison
st.header("Direct Comparison")

comp_col1, comp_col2 = st.columns(2)

with comp_col1:
    st.markdown("**With Shadow (Current):**")
    if minimal_button("Shadow Button", CarbonIcons.UPLOAD, "shadow"):
        st.success("Shadow button clicked!")

with comp_col2:
    st.markdown("**Regular Streamlit Button:**")
    if st.button("Regular Button", key="regular"):
        st.success("Regular button clicked!")

st.info("""
**If buttons are hard to see:**
1. They might need a border
2. Background color might need more contrast
3. Shadow might need to be stronger

Let me know what you see!
""")