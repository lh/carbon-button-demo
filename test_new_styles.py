"""
Test the new cosmetic changes - no blue borders, better color progression
"""

import streamlit as st
from carbon_button_styles import inject_carbon_styles, minimal_button, icon_button, create_toolbar, CarbonIcons

st.set_page_config(page_title="New Button Styles", page_icon="✨", layout="wide")

# Inject the updated styles
inject_carbon_styles()

st.title("✨ Updated Carbon Button Styles")
st.markdown("No blue borders • Subtle shadows • Better color progression")

# Color progression explanation
st.info("""
**Color Progression:**
- **Normal**: Slightly brighter than background (#fafafa) 
- **Hover**: Even brighter (#ffffff) with elevated shadow
- **Click**: Darker (#e0e0e0) with compressed shadow
- **No blue borders** - Clean, modern look!
""")

# Main buttons showcase
st.header("Minimal Style Buttons")
st.markdown("Notice the subtle shadow instead of borders")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if minimal_button("Upload", CarbonIcons.UPLOAD, "test1"):
        st.success("Clicked!")

with col2:
    if minimal_button("Download", CarbonIcons.DOWNLOAD, "test2"):
        st.info("Clicked!")

with col3:
    if minimal_button("Save", CarbonIcons.SAVE, "test3"):
        st.success("Clicked!")

with col4:
    if minimal_button("Copy", CarbonIcons.COPY, "test4"):
        st.info("Clicked!")

with col5:
    if minimal_button("Settings", CarbonIcons.SETTINGS, "test5"):
        st.info("Clicked!")

# Icon-only buttons
st.header("Icon-Only Buttons")
st.markdown("Clean, no borders, just subtle shadows")

toolbar = create_toolbar([
    (CarbonIcons.HOME, "home", "Home"),
    (CarbonIcons.ADD, "add", "Add new"),
    (CarbonIcons.SAVE, "save", "Save"),
    (CarbonIcons.COPY, "copy", "Copy"),
    (CarbonIcons.DELETE, "delete", "Delete"),
    (CarbonIcons.UPLOAD, "upload", "Upload"),
    (CarbonIcons.DOWNLOAD, "download", "Download"),
    (CarbonIcons.SETTINGS, "settings", "Settings"),
    (CarbonIcons.SEARCH, "search", "Search"),
    (CarbonIcons.FILTER, "filter", "Filter"),
], style="minimal")

for key, clicked in toolbar.items():
    if clicked:
        st.toast(f"{key} clicked!")

# Full width buttons
st.header("Full Width Buttons")
col1, col2 = st.columns(2)

with col1:
    if minimal_button("Process All Files", CarbonIcons.PLAY, "full1", use_container_width=True):
        with st.spinner("Processing..."):
            import time
            time.sleep(1)
        st.success("Complete!")

with col2:
    if minimal_button("Export Report", CarbonIcons.DOWNLOAD, "full2", use_container_width=True):
        st.info("Exporting...")

# Different button states side by side
st.header("Button States")
st.markdown("Hover over buttons to see the smooth transitions")

state_col1, state_col2, state_col3 = st.columns(3)

with state_col1:
    st.markdown("### Normal State")
    st.markdown("Background: #fafafa")
    minimal_button("Normal", CarbonIcons.INFO, "state1")

with state_col2:
    st.markdown("### Hover State")
    st.markdown("Background: #ffffff")
    st.caption("(Hover to see)")
    minimal_button("Hover Me", CarbonIcons.INFO, "state2")

with state_col3:
    st.markdown("### Active State")
    st.markdown("Background: #e0e0e0")
    st.caption("(Click to see)")
    minimal_button("Click Me", CarbonIcons.INFO, "state3")

# Comparison with other styles
st.header("Style Comparison")

comp_col1, comp_col2, comp_col3 = st.columns(3)

with comp_col1:
    st.subheader("Minimal (Updated)")
    st.caption("No borders, subtle shadow")
    if minimal_button("Upload File", CarbonIcons.UPLOAD, "comp1"):
        st.success("Clean look!")

with comp_col2:
    st.subheader("Primary")
    st.caption("Carbon blue style")
    from carbon_button_styles import primary_button
    if primary_button("Upload File", CarbonIcons.UPLOAD, "comp2"):
        st.info("Primary clicked!")

with comp_col3:
    st.subheader("Ghost/Outlined")
    st.caption("Light border only")
    from carbon_button_styles import outlined_button
    if outlined_button("Upload File", CarbonIcons.UPLOAD, "comp3"):
        st.info("Ghost clicked!")

# Visual guide
st.header("Visual Guide")
st.markdown("""
### What changed:
1. **No blue focus borders** - Clean focus state
2. **Subtle shadows** instead of borders for depth
3. **Better color progression**:
   - Normal: Slightly elevated from page
   - Hover: Lifts up and brightens
   - Click: Presses down and darkens
4. **Smoother transitions** - Professional micro-interactions

### The result:
- More modern, clean appearance
- Better visual feedback
- No distracting blue outlines
- Maintains accessibility (buttons still focusable)
""")

# Test focus state
st.header("Test Focus State")
st.markdown("Tab through these buttons - no blue borders!")

focus_cols = st.columns(4)
for i in range(4):
    with focus_cols[i]:
        minimal_button(f"Tab {i+1}", CarbonIcons.ADD, f"focus{i}")