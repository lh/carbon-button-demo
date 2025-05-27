"""
Interactive Color Tuner for Carbon Button Component
This version works with the actual React component
"""

import streamlit as st
import json
from carbon_button import carbon_button_raw, CarbonIcons

st.set_page_config(page_title="Carbon Button Component Color Tuner", page_icon="🎨", layout="wide")

st.title("🎨 Carbon Button Component Color Tuner")
st.markdown("Fine-tune your button colors with live preview using the actual component")

# Initialize session state for colors
if 'color_scheme' not in st.session_state:
    st.session_state.color_scheme = {
        "rest_bg": "#e0e0e0",
        "rest_text": "#1a1a1a",
        "rest_border": "#cccccc",
        "hover_bg": "#f5f5f5",
        "hover_text": "#000000",
        "hover_border": "#b0b0b0",
        "active_bg": "#c0c0c0",
        "active_text": "#000000",
        "active_border": "#999999",
    }

# Create two columns - controls and preview
control_col, preview_col = st.columns([1, 1])

with control_col:
    st.header("🎛️ Color Controls")
    
    # Rest state
    st.subheader("Rest State (Normal)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.color_scheme['rest_bg'] = st.color_picker(
            "Background", 
            st.session_state.color_scheme['rest_bg'], 
            key="rest_bg"
        )
    with col2:
        st.session_state.color_scheme['rest_text'] = st.color_picker(
            "Text/Icon", 
            st.session_state.color_scheme['rest_text'], 
            key="rest_text"
        )
    with col3:
        st.session_state.color_scheme['rest_border'] = st.color_picker(
            "Border", 
            st.session_state.color_scheme['rest_border'], 
            key="rest_border"
        )
    
    # Hover state
    st.subheader("Hover State")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.color_scheme['hover_bg'] = st.color_picker(
            "Background", 
            st.session_state.color_scheme['hover_bg'], 
            key="hover_bg"
        )
    with col2:
        st.session_state.color_scheme['hover_text'] = st.color_picker(
            "Text/Icon", 
            st.session_state.color_scheme['hover_text'], 
            key="hover_text"
        )
    with col3:
        st.session_state.color_scheme['hover_border'] = st.color_picker(
            "Border", 
            st.session_state.color_scheme['hover_border'], 
            key="hover_border"
        )
    
    # Active/Click state
    st.subheader("Active State (Click)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.color_scheme['active_bg'] = st.color_picker(
            "Background", 
            st.session_state.color_scheme['active_bg'], 
            key="active_bg"
        )
    with col2:
        st.session_state.color_scheme['active_text'] = st.color_picker(
            "Text/Icon", 
            st.session_state.color_scheme['active_text'], 
            key="active_text"
        )
    with col3:
        st.session_state.color_scheme['active_border'] = st.color_picker(
            "Border", 
            st.session_state.color_scheme['active_border'], 
            key="active_border"
        )
    
    # Show current values
    st.subheader("Current Color Values")
    st.code(json.dumps(st.session_state.color_scheme, indent=2), language="json")

with preview_col:
    st.header("👁️ Live Preview")
    st.info("⚠️ Note: This preview shows the default component colors. To see your custom colors, we need to modify the React component to accept color props.")
    
    # Preview buttons with default component
    st.subheader("Button Examples")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if carbon_button_raw("Upload", CarbonIcons.UPLOAD, "preview1", button_type="secondary"):
            st.success("Clicked!")
    
    with col2:
        if carbon_button_raw("Save", CarbonIcons.SAVE, "preview2", button_type="secondary"):
            st.success("Clicked!")
    
    with col3:
        if carbon_button_raw("Settings", CarbonIcons.SETTINGS, "preview3", button_type="secondary"):
            st.success("Clicked!")
    
    # Icon only buttons
    st.subheader("Icon Only")
    icon_cols = st.columns(6)
    icons = [
        (CarbonIcons.HOME, "home"),
        (CarbonIcons.ADD, "add"),
        (CarbonIcons.COPY, "copy"),
        (CarbonIcons.DELETE, "delete"),
        (CarbonIcons.SEARCH, "search"),
        (CarbonIcons.FILTER, "filter"),
    ]
    
    for i, (icon, name) in enumerate(icons):
        with icon_cols[i]:
            if carbon_button_raw("", icon, f"icon_{name}", button_type="secondary"):
                st.toast(f"{name} clicked!")

# Export section
st.divider()
st.header("📤 Export and Next Steps")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Color Scheme")
    color_json = json.dumps(st.session_state.color_scheme, indent=2)
    
    st.download_button(
        label="⬇️ Download colors.json",
        data=color_json,
        file_name="carbon_button_colors.json",
        mime="application/json"
    )

with col2:
    st.subheader("How to Apply These Colors")
    st.markdown("""
    The React component currently uses hardcoded colors. To use your custom colors:
    
    1. Share your color scheme with me
    2. I'll update the React component to accept color props
    3. Or I can hardcode your preferred colors into the component
    
    **Quick Option**: Click the download button and share the JSON file with me, 
    and I'll update the component with your exact colors!
    """)

# Instructions
st.divider()
st.info("""
**Current Limitation**: The React component doesn't yet accept color props, so this tuner shows 
what colors you want but can't apply them in real-time. Share your color choices with me and 
I'll update the component!

**Testing Interactions**:
- Hover over buttons to see hover state
- Click and hold to see active state
- The actual colors will be whatever is hardcoded in the React component
""")