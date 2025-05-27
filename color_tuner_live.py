"""
Live Color Tuner for Carbon Button Component
Real-time color updates!
"""

import streamlit as st
import json
from carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Button Live Color Tuner", page_icon="🎨", layout="wide")

st.title("🎨 Carbon Button Live Color Tuner")
st.markdown("Adjust colors and see changes in real-time!")

# Initialize session state for colors
if 'colors' not in st.session_state:
    st.session_state.colors = {
        "rest_bg": "#e0e0e0",
        "rest_text": "#1a1a1a",
        "rest_border": "#cccccc",
        "hover_bg": "#f5f5f5",
        "hover_text": "#000000",
        "hover_border": "#b0b0b0",
        "active_bg": "#606060",  # Much darker for click
        "active_text": "#ffffff",
        "active_border": "#404040",
    }

# Create two columns - controls and preview
control_col, preview_col = st.columns([1, 1])

with control_col:
    st.header("🎛️ Color Controls")
    
    # Rest state
    st.subheader("Rest State (Normal)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.colors['rest_bg'] = st.color_picker(
            "Background", 
            st.session_state.colors['rest_bg'], 
            key="rest_bg"
        )
    with col2:
        st.session_state.colors['rest_text'] = st.color_picker(
            "Text/Icon", 
            st.session_state.colors['rest_text'], 
            key="rest_text"
        )
    with col3:
        st.session_state.colors['rest_border'] = st.color_picker(
            "Border", 
            st.session_state.colors['rest_border'], 
            key="rest_border"
        )
    
    # Hover state
    st.subheader("Hover State")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.colors['hover_bg'] = st.color_picker(
            "Background", 
            st.session_state.colors['hover_bg'], 
            key="hover_bg"
        )
    with col2:
        st.session_state.colors['hover_text'] = st.color_picker(
            "Text/Icon", 
            st.session_state.colors['hover_text'], 
            key="hover_text"
        )
    with col3:
        st.session_state.colors['hover_border'] = st.color_picker(
            "Border", 
            st.session_state.colors['hover_border'], 
            key="hover_border"
        )
    
    # Active/Click state
    st.subheader("Active State (Click & Hold)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.colors['active_bg'] = st.color_picker(
            "Background", 
            st.session_state.colors['active_bg'], 
            key="active_bg"
        )
    with col2:
        st.session_state.colors['active_text'] = st.color_picker(
            "Text/Icon", 
            st.session_state.colors['active_text'], 
            key="active_text"
        )
    with col3:
        st.session_state.colors['active_border'] = st.color_picker(
            "Border", 
            st.session_state.colors['active_border'], 
            key="active_border"
        )

with preview_col:
    st.header("👁️ Live Preview")
    
    # Preview buttons with custom colors
    st.subheader("Button Examples")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if carbon_button("Upload", CarbonIcons.UPLOAD, "preview1", 
                        button_type="secondary", colors=st.session_state.colors):
            st.success("Clicked!")
    
    with col2:
        if carbon_button("Save", CarbonIcons.SAVE, "preview2", 
                        button_type="secondary", colors=st.session_state.colors):
            st.success("Clicked!")
    
    with col3:
        if carbon_button("Settings", CarbonIcons.SETTINGS, "preview3", 
                        button_type="secondary", colors=st.session_state.colors):
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
            if carbon_button("", icon, f"icon_{name}", 
                           button_type="secondary", colors=st.session_state.colors):
                st.toast(f"{name} clicked!")
    
    # Full width button
    st.subheader("Full Width")
    if carbon_button("Process Files", CarbonIcons.PLAY, "full_width", 
                     button_type="secondary", 
                     use_container_width=True, 
                     colors=st.session_state.colors):
        st.info("Processing...")
    
    # Instructions
    st.info("""
    **Test the states:**
    - **Rest**: Normal button appearance
    - **Hover**: Move your mouse over buttons
    - **Active**: Click and hold the button
    
    Colors update in real-time as you adjust them!
    """)

# Export section
st.divider()
st.header("📤 Export Your Color Scheme")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Current Color Values")
    color_json = json.dumps(st.session_state.colors, indent=2)
    st.code(color_json, language="json")
    
    st.download_button(
        label="⬇️ Download colors.json",
        data=color_json,
        file_name="carbon_button_colors.json",
        mime="application/json"
    )

with col2:
    st.subheader("How to Use These Colors")
    
    python_code = f"""# Use these colors in your app:
from carbon_button import carbon_button, CarbonIcons

# Define your custom colors
my_colors = {json.dumps(st.session_state.colors, indent=4)}

# Use them in your buttons
if carbon_button(
    "My Button", 
    CarbonIcons.SAVE,
    key="my_btn",
    button_type="secondary",
    colors=my_colors
):
    st.write("Button clicked!")
"""
    
    st.code(python_code, language="python")
    
    st.download_button(
        label="⬇️ Download example code",
        data=python_code,
        file_name="carbon_button_example.py",
        mime="text/plain"
    )

# Presets
st.divider()
st.header("🎨 Color Presets")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("High Contrast"):
        st.session_state.colors = {
            "rest_bg": "#d0d0d0",
            "rest_text": "#000000",
            "rest_border": "#a0a0a0",
            "hover_bg": "#e8e8e8",
            "hover_text": "#000000",
            "hover_border": "#808080",
            "active_bg": "#303030",
            "active_text": "#ffffff",
            "active_border": "#000000",
        }
        st.rerun()

with col2:
    if st.button("Subtle"):
        st.session_state.colors = {
            "rest_bg": "#f8f8f8",
            "rest_text": "#333333",
            "rest_border": "#e8e8e8",
            "hover_bg": "#ffffff",
            "hover_text": "#000000",
            "hover_border": "#d0d0d0",
            "active_bg": "#e0e0e0",
            "active_text": "#000000",
            "active_border": "#c0c0c0",
        }
        st.rerun()

with col3:
    if st.button("Dark Theme"):
        st.session_state.colors = {
            "rest_bg": "#3a3a3a",
            "rest_text": "#e0e0e0",
            "rest_border": "#4a4a4a",
            "hover_bg": "#4a4a4a",
            "hover_text": "#ffffff",
            "hover_border": "#5a5a5a",
            "active_bg": "#1a1a1a",
            "active_text": "#ffffff",
            "active_border": "#0a0a0a",
        }
        st.rerun()

with col4:
    if st.button("Reset Default"):
        st.session_state.colors = {
            "rest_bg": "#e0e0e0",
            "rest_text": "#1a1a1a",
            "rest_border": "#cccccc",
            "hover_bg": "#f5f5f5",
            "hover_text": "#000000",
            "hover_border": "#b0b0b0",
            "active_bg": "#606060",
            "active_text": "#ffffff",
            "active_border": "#404040",
        }
        st.rerun()

st.caption("💡 Colors update instantly as you change them!")