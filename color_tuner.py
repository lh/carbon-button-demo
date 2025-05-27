"""
Interactive Color Tuner for Carbon Buttons
Adjust all colors and export your perfect color scheme!
"""

import streamlit as st
import json
from carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Button Color Tuner", page_icon="🎨", layout="wide")

st.title("🎨 Carbon Button Color Tuner")
st.markdown("Fine-tune your button colors and export the settings")

# Initialize session state for colors
if 'color_scheme' not in st.session_state:
    st.session_state.color_scheme = {
        "light": {
            "page_bg": "#ffffff",
            "rest_bg": "#e0e0e0",
            "rest_text": "#1a1a1a",
            "rest_border": "#cccccc",
            "hover_bg": "#f5f5f5",
            "hover_text": "#000000",
            "hover_border": "#b0b0b0",
            "click_bg": "#c0c0c0",
            "click_text": "#000000",
            "click_border": "#999999",
            "disabled_bg": "#f0f0f0",
            "disabled_text": "#999999",
            "disabled_border": "#e0e0e0",
        },
        "dark": {
            "page_bg": "#1a1a1a",
            "rest_bg": "#3a3a3a",
            "rest_text": "#e0e0e0",
            "rest_border": "#4a4a4a",
            "hover_bg": "#4a4a4a",
            "hover_text": "#ffffff",
            "hover_border": "#5a5a5a",
            "click_bg": "#2a2a2a",
            "click_text": "#ffffff",
            "click_border": "#1a1a1a",
            "disabled_bg": "#2a2a2a",
            "disabled_text": "#666666",
            "disabled_border": "#3a3a3a",
        }
    }

# Mode selector
mode = st.radio("Mode", ["Light Mode", "Dark Mode"], horizontal=True)
current_mode = "light" if mode == "Light Mode" else "dark"
colors = st.session_state.color_scheme[current_mode]

# Apply current color scheme
st.markdown(f"""
<style>
/* Page background */
.stApp > .main {{
    background-color: {colors['page_bg']};
}}

/* Custom button styles */
button[data-testid="baseButton-secondary"] {{
    background-color: {colors['rest_bg']} !important;
    color: {colors['rest_text']} !important;
    border: 1px solid {colors['rest_border']} !important;
    transition: all 0.15s ease !important;
}}

button[data-testid="baseButton-secondary"]:hover {{
    background-color: {colors['hover_bg']} !important;
    color: {colors['hover_text']} !important;
    border-color: {colors['hover_border']} !important;
}}

button[data-testid="baseButton-secondary"]:active {{
    background-color: {colors['click_bg']} !important;
    color: {colors['click_text']} !important;
    border-color: {colors['click_border']} !important;
}}

button[data-testid="baseButton-secondary"]:disabled {{
    background-color: {colors['disabled_bg']} !important;
    color: {colors['disabled_text']} !important;
    border-color: {colors['disabled_border']} !important;
    opacity: 1 !important;
}}
</style>
""", unsafe_allow_html=True)

# Create two columns - controls and preview
control_col, preview_col = st.columns([1, 1])

with control_col:
    st.header("🎛️ Color Controls")
    
    # Page background
    st.subheader("Page Background")
    new_page_bg = st.color_picker("Page Background", colors['page_bg'], key=f"page_bg_{current_mode}")
    if new_page_bg != colors['page_bg']:
        colors['page_bg'] = new_page_bg
        st.rerun()
    
    # Rest state
    st.subheader("Rest State (Normal)")
    col1, col2, col3 = st.columns(3)
    with col1:
        new_rest_bg = st.color_picker("Background", colors['rest_bg'], key=f"rest_bg_{current_mode}")
        if new_rest_bg != colors['rest_bg']:
            colors['rest_bg'] = new_rest_bg
            st.rerun()
    with col2:
        new_rest_text = st.color_picker("Text/Icon", colors['rest_text'], key=f"rest_text_{current_mode}")
        if new_rest_text != colors['rest_text']:
            colors['rest_text'] = new_rest_text
            st.rerun()
    with col3:
        new_rest_border = st.color_picker("Border", colors['rest_border'], key=f"rest_border_{current_mode}")
        if new_rest_border != colors['rest_border']:
            colors['rest_border'] = new_rest_border
            st.rerun()
    
    # Hover state
    st.subheader("Hover State")
    col1, col2, col3 = st.columns(3)
    with col1:
        new_hover_bg = st.color_picker("Background", colors['hover_bg'], key=f"hover_bg_{current_mode}")
        if new_hover_bg != colors['hover_bg']:
            colors['hover_bg'] = new_hover_bg
            st.rerun()
    with col2:
        new_hover_text = st.color_picker("Text/Icon", colors['hover_text'], key=f"hover_text_{current_mode}")
        if new_hover_text != colors['hover_text']:
            colors['hover_text'] = new_hover_text
            st.rerun()
    with col3:
        new_hover_border = st.color_picker("Border", colors['hover_border'], key=f"hover_border_{current_mode}")
        if new_hover_border != colors['hover_border']:
            colors['hover_border'] = new_hover_border
            st.rerun()
    
    # Click state
    st.subheader("Click State (Active)")
    col1, col2, col3 = st.columns(3)
    with col1:
        new_click_bg = st.color_picker("Background", colors['click_bg'], key=f"click_bg_{current_mode}")
        if new_click_bg != colors['click_bg']:
            colors['click_bg'] = new_click_bg
            st.rerun()
    with col2:
        new_click_text = st.color_picker("Text/Icon", colors['click_text'], key=f"click_text_{current_mode}")
        if new_click_text != colors['click_text']:
            colors['click_text'] = new_click_text
            st.rerun()
    with col3:
        new_click_border = st.color_picker("Border", colors['click_border'], key=f"click_border_{current_mode}")
        if new_click_border != colors['click_border']:
            colors['click_border'] = new_click_border
            st.rerun()
    
    # Disabled state
    st.subheader("Disabled State")
    col1, col2, col3 = st.columns(3)
    with col1:
        new_disabled_bg = st.color_picker("Background", colors['disabled_bg'], key=f"disabled_bg_{current_mode}")
        if new_disabled_bg != colors['disabled_bg']:
            colors['disabled_bg'] = new_disabled_bg
            st.rerun()
    with col2:
        new_disabled_text = st.color_picker("Text/Icon", colors['disabled_text'], key=f"disabled_text_{current_mode}")
        if new_disabled_text != colors['disabled_text']:
            colors['disabled_text'] = new_disabled_text
            st.rerun()
    with col3:
        new_disabled_border = st.color_picker("Border", colors['disabled_border'], key=f"disabled_border_{current_mode}")
        if new_disabled_border != colors['disabled_border']:
            colors['disabled_border'] = new_disabled_border
            st.rerun()

with preview_col:
    st.header("👁️ Live Preview")
    
    # Preview buttons
    st.subheader("Button Examples")
    
    # Regular buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if carbon_button("Upload", CarbonIcons.UPLOAD, f"preview1_{current_mode}", button_type="secondary"):
            st.success("Clicked!")
    
    with col2:
        if carbon_button("Save", CarbonIcons.SAVE, f"preview2_{current_mode}", button_type="secondary"):
            st.success("Clicked!")
    
    with col3:
        if carbon_button("Settings", CarbonIcons.SETTINGS, f"preview3_{current_mode}", button_type="secondary"):
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
            if carbon_button("", icon, f"icon_{name}_{current_mode}", button_type="secondary"):
                st.toast(f"{name} clicked!")
    
    # Disabled button
    st.subheader("Disabled State")
    carbon_button("Disabled Button", CarbonIcons.CLOSE, f"disabled_{current_mode}", 
                  button_type="secondary", disabled=True)
    
    # Full width
    st.subheader("Full Width")
    if carbon_button("Process Files", CarbonIcons.PLAY, f"full_{current_mode}", 
                     button_type="secondary", use_container_width=True):
        st.info("Processing...")
    
    # State instructions
    st.info("""
    **Test the states:**
    - **Rest**: Normal appearance
    - **Hover**: Move mouse over buttons
    - **Click**: Click and hold
    - **Disabled**: See the disabled button above
    """)

# Export section
st.divider()
st.header("📤 Export Your Color Scheme")

col1, col2 = st.columns(2)

with col1:
    # Show current settings as JSON
    st.subheader("Current Settings")
    color_json = json.dumps(st.session_state.color_scheme, indent=2)
    st.code(color_json, language="json")

with col2:
    # Export options
    st.subheader("Export Options")
    
    # Download JSON
    st.download_button(
        label="⬇️ Download color_scheme.json",
        data=color_json,
        file_name="carbon_button_colors.json",
        mime="application/json"
    )
    
    # Generate Python code
    python_code = f"""# Carbon Button Color Scheme
# Generated by Color Tuner

CARBON_BUTTON_COLORS = {json.dumps(st.session_state.color_scheme, indent=4)}

# Usage in your app:
# from carbon_button_styles import inject_carbon_styles
# inject_carbon_styles(CARBON_BUTTON_COLORS['{current_mode}'])
"""
    
    st.download_button(
        label="⬇️ Download color_scheme.py",
        data=python_code,
        file_name="carbon_button_colors.py",
        mime="text/plain"
    )
    
    # Copy to clipboard instructions
    st.info("""
    **To share your colors:**
    1. Adjust colors using the controls
    2. Download the JSON or Python file
    3. Share the file with me
    4. I'll update your component with these exact colors!
    """)

# Preset themes
st.divider()
st.header("🎨 Preset Themes")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Carbon Classic", key="preset1"):
        st.session_state.color_scheme[current_mode] = {
            "page_bg": "#ffffff" if current_mode == "light" else "#161616",
            "rest_bg": "#f4f4f4" if current_mode == "light" else "#393939",
            "rest_text": "#161616" if current_mode == "light" else "#f4f4f4",
            "rest_border": "#e0e0e0" if current_mode == "light" else "#525252",
            "hover_bg": "#e0e0e0" if current_mode == "light" else "#4c4c4c",
            "hover_text": "#161616" if current_mode == "light" else "#ffffff",
            "hover_border": "#c6c6c6" if current_mode == "light" else "#6f6f6f",
            "click_bg": "#c6c6c6" if current_mode == "light" else "#262626",
            "click_text": "#161616" if current_mode == "light" else "#ffffff",
            "click_border": "#a8a8a8" if current_mode == "light" else "#161616",
            "disabled_bg": "#ffffff" if current_mode == "light" else "#262626",
            "disabled_text": "#c6c6c6" if current_mode == "light" else "#525252",
            "disabled_border": "#e0e0e0" if current_mode == "light" else "#393939",
        }
        st.rerun()

with col2:
    if st.button("High Contrast", key="preset2"):
        st.session_state.color_scheme[current_mode] = {
            "page_bg": "#ffffff" if current_mode == "light" else "#000000",
            "rest_bg": "#333333" if current_mode == "light" else "#ffffff",
            "rest_text": "#ffffff" if current_mode == "light" else "#000000",
            "rest_border": "#000000" if current_mode == "light" else "#ffffff",
            "hover_bg": "#000000" if current_mode == "light" else "#cccccc",
            "hover_text": "#ffffff" if current_mode == "light" else "#000000",
            "hover_border": "#000000" if current_mode == "light" else "#999999",
            "click_bg": "#666666" if current_mode == "light" else "#333333",
            "click_text": "#ffffff" if current_mode == "light" else "#ffffff",
            "click_border": "#333333" if current_mode == "light" else "#000000",
            "disabled_bg": "#cccccc" if current_mode == "light" else "#333333",
            "disabled_text": "#666666" if current_mode == "light" else "#666666",
            "disabled_border": "#999999" if current_mode == "light" else "#444444",
        }
        st.rerun()

with col3:
    if st.button("Subtle", key="preset3"):
        st.session_state.color_scheme[current_mode] = {
            "page_bg": "#fafafa" if current_mode == "light" else "#1e1e1e",
            "rest_bg": "#f5f5f5" if current_mode == "light" else "#2d2d2d",
            "rest_text": "#333333" if current_mode == "light" else "#d4d4d4",
            "rest_border": "#f0f0f0" if current_mode == "light" else "#404040",
            "hover_bg": "#ffffff" if current_mode == "light" else "#3a3a3a",
            "hover_text": "#000000" if current_mode == "light" else "#ffffff",
            "hover_border": "#e0e0e0" if current_mode == "light" else "#525252",
            "click_bg": "#e8e8e8" if current_mode == "light" else "#252525",
            "click_text": "#000000" if current_mode == "light" else "#ffffff",
            "click_border": "#d0d0d0" if current_mode == "light" else "#1a1a1a",
            "disabled_bg": "#fafafa" if current_mode == "light" else "#252525",
            "disabled_text": "#b0b0b0" if current_mode == "light" else "#606060",
            "disabled_border": "#f5f5f5" if current_mode == "light" else "#353535",
        }
        st.rerun()

with col4:
    if st.button("Reset to Default", key="preset4"):
        st.session_state.color_scheme = {
            "light": {
                "page_bg": "#ffffff",
                "rest_bg": "#e0e0e0",
                "rest_text": "#1a1a1a",
                "rest_border": "#cccccc",
                "hover_bg": "#f5f5f5",
                "hover_text": "#000000",
                "hover_border": "#b0b0b0",
                "click_bg": "#c0c0c0",
                "click_text": "#000000",
                "click_border": "#999999",
                "disabled_bg": "#f0f0f0",
                "disabled_text": "#999999",
                "disabled_border": "#e0e0e0",
            },
            "dark": {
                "page_bg": "#1a1a1a",
                "rest_bg": "#3a3a3a",
                "rest_text": "#e0e0e0",
                "rest_border": "#4a4a4a",
                "hover_bg": "#4a4a4a",
                "hover_text": "#ffffff",
                "hover_border": "#5a5a5a",
                "click_bg": "#2a2a2a",
                "click_text": "#ffffff",
                "click_border": "#1a1a1a",
                "disabled_bg": "#2a2a2a",
                "disabled_text": "#666666",
                "disabled_border": "#3a3a3a",
            }
        }
        st.rerun()

st.divider()
st.caption("💡 Tip: Use the preset themes as starting points, then fine-tune to your preference!")