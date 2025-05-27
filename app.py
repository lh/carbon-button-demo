"""
Streamlit Carbon Button Component Demo
This app demonstrates the Carbon Design System button component for Streamlit.
"""

import streamlit as st
from briquette import carbon_button, CarbonIcons

st.set_page_config(
    page_title="Carbon Button Demo",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Carbon Button Component Demo")
st.markdown("Beautiful, accessible buttons using IBM's Carbon Design System")

# Create columns for layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Button Types")
    
    if carbon_button("Primary Button", key="primary"):
        st.success("Primary button clicked!")
    
    if carbon_button("Secondary Button", button_type="secondary", key="secondary"):
        st.info("Secondary button clicked!")
    
    if carbon_button("Danger Button", button_type="danger", key="danger"):
        st.error("Danger button clicked!")
    
    if carbon_button("Ghost Button", button_type="ghost", key="ghost"):
        st.write("Ghost button clicked!")

with col2:
    st.subheader("Buttons with Icons")
    
    if carbon_button("Upload File", icon=CarbonIcons.UPLOAD, key="upload"):
        st.write("Upload initiated...")
    
    if carbon_button("Download", icon=CarbonIcons.DOWNLOAD, button_type="secondary", key="download"):
        st.write("Download started...")
    
    if carbon_button("Save Changes", icon=CarbonIcons.SAVE, button_type="primary", key="save"):
        st.write("Changes saved!")
    
    if carbon_button("Delete", icon=CarbonIcons.DELETE, button_type="danger", key="delete"):
        st.write("Item deleted!")

with col3:
    st.subheader("Special States")
    
    if carbon_button("Full Width", use_container_width=True, key="full_width"):
        st.write("Full width button clicked!")
    
    carbon_button("Disabled Button", disabled=True, key="disabled")
    
    # Custom styled button
    custom_colors = {
        "rest_bg": "#6929c4",
        "rest_text": "#ffffff",
        "hover_bg": "#491d8b",
        "hover_text": "#ffffff",
        "active_bg": "#31135e",
        "active_text": "#ffffff"
    }
    
    if carbon_button("Custom Colors", colors=custom_colors, key="custom"):
        st.write("Custom styled button clicked!")

st.divider()

# More examples
st.subheader("More Icon Examples")

icon_cols = st.columns(4)

icons = [
    ("Settings", CarbonIcons.SETTINGS),
    ("Search", CarbonIcons.SEARCH),
    ("Filter", CarbonIcons.FILTER),
    ("Add", CarbonIcons.ADD),
    ("Copy", CarbonIcons.COPY),
    ("Home", CarbonIcons.HOME),
    ("Info", CarbonIcons.INFO),
    ("Help", CarbonIcons.HELP),
]

for i, (label, icon) in enumerate(icons):
    with icon_cols[i % 4]:
        if carbon_button(label, icon=icon, button_type="ghost", key=f"icon_{i}"):
            st.write(f"{label} clicked!")

st.divider()

# Code example
st.subheader("Example Code")

with st.expander("Show code example"):
    st.code("""
from briquette import carbon_button, CarbonIcons

# Basic button
if carbon_button("Click Me"):
    st.write("Button clicked!")

# Button with icon and custom type
if carbon_button("Download", 
                 icon=CarbonIcons.DOWNLOAD, 
                 button_type="secondary"):
    st.write("Download started!")

# Custom styled button
custom_colors = {
    "rest_bg": "#0f62fe",
    "rest_text": "#ffffff",
    "hover_bg": "#0353e9",
    "hover_text": "#ffffff",
    "active_bg": "#002d9c",
    "active_text": "#ffffff"
}

if carbon_button("Custom Button", colors=custom_colors):
    st.write("Custom button clicked!")
    """, language="python")

st.divider()

st.markdown("""
### Features
- 🎨 **Carbon Design System** - Professional, accessible design
- 🎯 **Multiple Button Types** - Primary, Secondary, Danger, Ghost
- 🖼️ **SVG Icon Support** - Sharp icons at any size
- 🎨 **Customizable Colors** - Full control over button appearance
- 📱 **Responsive** - Works great on all screen sizes
- ♿ **Accessible** - Follows WCAG guidelines

### Deployment
This component is ready for deployment on Streamlit Community Cloud. 
The built frontend files are included in the package, so no Node.js build step is required during deployment.
""")