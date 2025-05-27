"""
Demo: Automatic Dark Mode for Carbon Buttons
The buttons automatically adapt to your browser's color scheme preference!
"""

import streamlit as st
from carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Buttons - Dark Mode Demo", page_icon="🌓", layout="wide")

st.title("🌓 Carbon Buttons - Automatic Dark Mode")
st.markdown("""
The buttons below automatically switch between light and dark mode based on your browser's preference!

**To test:**
1. Change your system's appearance settings (light/dark mode)
2. Or use your browser's developer tools to toggle `prefers-color-scheme`
3. Watch the buttons automatically adapt!
""")

# Show current color scheme info
st.info("""
**Light Mode Colors:**
- Rest: #e6e2e2 background (warm grey)
- Hover: #f5f5f5 background (bright)
- Active: #50e4e0 background (teal) with white text

**Dark Mode Colors:**
- Rest: #ecdcdc background (light pink-grey)
- Hover: #f6f4f4 background (very light)
- Active: #67cccc background (lighter teal) with black text
""")

st.divider()

# Demo buttons
st.header("Button Examples")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Actions")
    if carbon_button("Upload", CarbonIcons.UPLOAD, "upload", button_type="secondary"):
        st.success("Uploaded!")
    
    if carbon_button("Download", CarbonIcons.DOWNLOAD, "download", button_type="secondary"):
        st.success("Downloaded!")
    
    if carbon_button("Save", CarbonIcons.SAVE, "save", button_type="secondary"):
        st.success("Saved!")

with col2:
    st.subheader("Navigation")
    if carbon_button("Home", CarbonIcons.HOME, "home", button_type="secondary"):
        st.info("Going home...")
    
    if carbon_button("Settings", CarbonIcons.SETTINGS, "settings", button_type="secondary"):
        st.info("Opening settings...")
    
    if carbon_button("Help", CarbonIcons.HELP, "help", button_type="secondary"):
        st.info("Getting help...")

with col3:
    st.subheader("Data")
    if carbon_button("Filter", CarbonIcons.FILTER, "filter", button_type="secondary"):
        st.info("Filtering...")
    
    if carbon_button("Search", CarbonIcons.SEARCH, "search", button_type="secondary"):
        st.info("Searching...")
    
    if carbon_button("Chart", CarbonIcons.CHART_BAR, "chart", button_type="secondary"):
        st.info("Charting...")

with col4:
    st.subheader("Edit")
    if carbon_button("Add", CarbonIcons.ADD, "add", button_type="secondary"):
        st.success("Added!")
    
    if carbon_button("Copy", CarbonIcons.COPY, "copy", button_type="secondary"):
        st.success("Copied!")
    
    if carbon_button("Delete", CarbonIcons.DELETE, "delete", button_type="secondary"):
        st.warning("Deleted!")

st.divider()

# Icon-only toolbar
st.header("Icon Toolbar")
icon_cols = st.columns(10)
icons = [
    (CarbonIcons.HOME, "icon_home"),
    (CarbonIcons.SEARCH, "icon_search"),
    (CarbonIcons.ADD, "icon_add"),
    (CarbonIcons.SAVE, "icon_save"),
    (CarbonIcons.COPY, "icon_copy"),
    (CarbonIcons.DELETE, "icon_delete"),
    (CarbonIcons.FILTER, "icon_filter"),
    (CarbonIcons.SETTINGS, "icon_settings"),
    (CarbonIcons.INFO, "icon_info"),
    (CarbonIcons.HELP, "icon_help"),
]

for i, (icon, key) in enumerate(icons):
    with icon_cols[i]:
        if carbon_button("", icon, key, button_type="secondary"):
            st.toast(f"{key} clicked!")

st.divider()

# Full width buttons
st.header("Full Width Buttons")
col1, col2 = st.columns(2)

with col1:
    if carbon_button("Process All Files", CarbonIcons.PLAY, "process", 
                     button_type="secondary", use_container_width=True):
        with st.spinner("Processing..."):
            import time
            time.sleep(1)
        st.success("Complete!")

with col2:
    if carbon_button("Generate Report", CarbonIcons.DOCUMENT, "report", 
                     button_type="secondary", use_container_width=True):
        with st.spinner("Generating..."):
            import time
            time.sleep(1)
        st.success("Report ready!")

st.divider()

# Technical note
st.caption("""
💡 **Technical Note**: The React component detects `prefers-color-scheme: dark` media query 
and automatically switches between the two color schemes. No manual switching needed!
""")