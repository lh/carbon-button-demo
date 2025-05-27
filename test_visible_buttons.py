"""
Test the MORE VISIBLE button styles
"""

import streamlit as st
from carbon_button_styles import inject_carbon_styles, minimal_button, icon_button, create_toolbar, CarbonIcons

st.set_page_config(page_title="Visible Buttons", page_icon="👀", layout="wide")

# Inject styles
inject_carbon_styles()

st.title("👀 More Visible Carbon Buttons")

st.success("""
**Updated for better visibility:**
- Medium grey background (#e0e0e0) instead of very light
- Subtle border for definition (#cccccc)
- Stronger shadows
- Almost black text (#1a1a1a)
""")

# Main showcase
st.header("Now You Should See These!")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if minimal_button("Upload", CarbonIcons.UPLOAD, "vis1"):
        st.success("✅ Upload clicked!")

with col2:
    if minimal_button("Download", CarbonIcons.DOWNLOAD, "vis2"):
        st.info("⬇️ Download clicked!")

with col3:
    if minimal_button("Save", CarbonIcons.SAVE, "vis3"):
        st.success("💾 Saved!")

with col4:
    if minimal_button("Settings", CarbonIcons.SETTINGS, "vis4"):
        st.info("⚙️ Settings!")

# Icon toolbar
st.header("Icon Toolbar")
st.markdown("These should be clearly visible now:")

toolbar = create_toolbar([
    (CarbonIcons.HOME, "home", "Home"),
    (CarbonIcons.ADD, "add", "Add"),
    (CarbonIcons.SAVE, "save", "Save"),
    (CarbonIcons.COPY, "copy", "Copy"),
    (CarbonIcons.DELETE, "delete", "Delete"),
    (CarbonIcons.SEARCH, "search", "Search"),
], style="minimal")

# Show clicks
for key, clicked in toolbar.items():
    if clicked:
        st.toast(f"✅ {key} clicked!", icon="🎯")

# States demonstration
st.header("Button States")

state_col1, state_col2, state_col3 = st.columns(3)

with state_col1:
    st.markdown("""
    ### Normal
    - Background: #e0e0e0
    - Border: #cccccc
    - Shadow: Yes
    """)
    minimal_button("Normal State", CarbonIcons.INFO, "state1")

with state_col2:
    st.markdown("""
    ### Hover
    - Background: #f5f5f5
    - Elevated shadow
    - Lifts up
    """)
    minimal_button("Hover Over Me", CarbonIcons.INFO, "state2")

with state_col3:
    st.markdown("""
    ### Click
    - Background: #c0c0c0
    - Inset shadow
    - Presses down
    """)
    minimal_button("Click Me", CarbonIcons.INFO, "state3")

# Comparison
st.header("Before vs After")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Your Minimal Buttons")
    st.caption("With proper visibility")
    if minimal_button("Visible Button", CarbonIcons.UPLOAD, "compare1"):
        st.success("Much better!")

with col2:
    st.markdown("### Regular Streamlit")
    st.caption("For comparison")
    if st.button("Regular Button", key="compare2"):
        st.info("Standard button")

# Full width example
st.header("Full Width Actions")

if minimal_button("Process All Files", CarbonIcons.PLAY, "full1", use_container_width=True):
    with st.spinner("Processing..."):
        import time
        time.sleep(1)
    st.success("✅ All files processed!")

if minimal_button("Generate Report", CarbonIcons.CHART_BAR, "full2", use_container_width=True):
    st.info("📊 Generating report...")

# Color info
st.header("Color Specifications")

st.markdown("""
| State | Background | Text | Border | Shadow |
|-------|------------|------|--------|--------|
| Normal | #e0e0e0 | #1a1a1a | #cccccc | 0 2px 4px rgba(0,0,0,0.1) |
| Hover | #f5f5f5 | #000000 | #b0b0b0 | 0 4px 8px rgba(0,0,0,0.15) |
| Click | #c0c0c0 | #000000 | #999999 | inset 0 2px 4px rgba(0,0,0,0.1) |

**Result**: Buttons that are clearly visible while maintaining a clean, professional look!
""")