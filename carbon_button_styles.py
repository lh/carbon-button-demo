"""
Production-ready Carbon Button styles for your app
Implements the exact design patterns from test_styled_carbon_buttons.py
"""

from carbon_button import carbon_button as _carbon_button, CarbonIcons
import streamlit as st

# Inject custom CSS for the minimal grey style
def inject_carbon_styles():
    """
    Inject CSS to achieve the minimal grey button style.
    Call this once at the top of your app.
    """
    st.markdown("""
    <style>
    /* Your custom light mode colors */
    button[data-testid="baseButton-secondary"] {
        background-color: #e6e2e2 !important;
        color: #1a1a1a !important;
        border: 1px solid #cccccc !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        transition: all 0.15s ease !important;
    }
    
    button[data-testid="baseButton-secondary"]:hover {
        background-color: #f5f5f5 !important;
        color: #000000 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15) !important;
        border-color: #b0b0b0 !important;
    }
    
    button[data-testid="baseButton-secondary"]:active {
        background-color: #50e4e0 !important;  /* Teal accent on click */
        color: #ffffff !important;
        transform: translateY(0) !important;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.1) !important;
        border-color: #404040 !important;
    }
    
    /* Remove focus outline (the blue border) */
    button[data-testid="baseButton-secondary"]:focus {
        outline: none !important;
        border: none !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05) !important;
    }
    
    /* Ghost/outlined style */
    button[data-testid="baseButton-ghost"] {
        background-color: transparent !important;
        color: #393939 !important;
        border: 1px solid #e0e0e0 !important;  /* Light grey border */
        transition: all 0.2s ease !important;
    }
    
    button[data-testid="baseButton-ghost"]:hover {
        background-color: #fafafa !important;  /* Light fill on hover */
        color: #161616 !important;
        border-color: #d0d0d0 !important;
    }
    
    button[data-testid="baseButton-ghost"]:active {
        background-color: #e0e0e0 !important;
        color: #161616 !important;
    }
    
    button[data-testid="baseButton-ghost"]:focus {
        outline: none !important;
        border-color: #e0e0e0 !important;
    }
    
    /* Ensure icons stay visible */
    .carbon-button-icon svg {
        fill: currentColor !important;
    }
    </style>
    """, unsafe_allow_html=True)

def minimal_button(label, icon, key, **kwargs):
    """
    Create a minimal style button (grey background, black icon)
    This is your main requested style.
    """
    return _carbon_button(
        label,
        icon,
        key=key,
        button_type="secondary",
        **kwargs
    )

def outlined_button(label, icon, key, **kwargs):
    """
    Create an outlined button (border only, fills on hover)
    """
    return _carbon_button(
        label,
        icon,
        key=key,
        button_type="ghost",
        **kwargs
    )

def primary_button(label, icon, key, **kwargs):
    """
    Create a primary button (Carbon blue)
    """
    return _carbon_button(
        label,
        icon,
        key=key,
        button_type="primary",
        **kwargs
    )

def danger_button(label, icon, key, **kwargs):
    """
    Create a danger button (red for destructive actions)
    """
    return _carbon_button(
        label,
        icon,
        key=key,
        button_type="danger",
        **kwargs
    )

# Convenience function for icon-only buttons
def icon_button(icon, key, style="minimal", tooltip=None, **kwargs):
    """
    Create an icon-only button
    
    Args:
        icon: Carbon icon SVG
        key: Unique key
        style: "minimal", "outlined", "primary", or "danger"
        tooltip: Optional tooltip text (Note: not currently supported by component)
        **kwargs: Additional button arguments
    """
    button_func = {
        "minimal": minimal_button,
        "outlined": outlined_button,
        "primary": primary_button,
        "danger": danger_button
    }.get(style, minimal_button)
    
    # Note: tooltip parameter is accepted but not used 
    # since the carbon_button component doesn't support help parameter
    
    return button_func("", icon, key, **kwargs)

# Pre-styled button groups for common use cases
def create_toolbar(buttons, style="minimal"):
    """
    Create a horizontal toolbar of icon buttons
    
    Args:
        buttons: List of (icon, key, tooltip) tuples
        style: Button style to use
    
    Returns:
        Dict of button keys and their clicked state
    """
    results = {}
    cols = st.columns(len(buttons))
    
    for i, (icon, key, tooltip) in enumerate(buttons):
        with cols[i]:
            results[key] = icon_button(icon, key, style=style, tooltip=tooltip)
    
    return results

def create_action_buttons(actions, style="minimal", use_container_width=False):
    """
    Create a set of action buttons with labels
    
    Args:
        actions: List of (label, icon, key) tuples
        style: Button style to use
        use_container_width: Whether buttons should fill container
    
    Returns:
        Dict of button keys and their clicked state
    """
    results = {}
    button_func = {
        "minimal": minimal_button,
        "outlined": outlined_button,
        "primary": primary_button,
        "danger": danger_button
    }.get(style, minimal_button)
    
    for label, icon, key in actions:
        results[key] = button_func(
            label, 
            icon, 
            key, 
            use_container_width=use_container_width
        )
    
    return results

# Example usage
if __name__ == "__main__":
    st.set_page_config(page_title="Carbon Button Styles", page_icon="🎨")
    
    # IMPORTANT: Inject styles at the top of your app
    inject_carbon_styles()
    
    st.title("Carbon Button Styles - Ready to Use!")
    st.info("Now using your custom light mode colors with teal active state!")
    
    # Example 1: Minimal buttons (your main style)
    st.header("Minimal Style Buttons")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if minimal_button("Upload", CarbonIcons.UPLOAD, "min1"):
            st.success("Uploaded!")
    
    with col2:
        if minimal_button("Save", CarbonIcons.SAVE, "min2"):
            st.success("Saved!")
    
    with col3:
        if minimal_button("Settings", CarbonIcons.SETTINGS, "min3"):
            st.info("Settings!")
    
    # Example 2: Icon toolbar
    st.header("Icon Toolbar")
    toolbar_buttons = [
        (CarbonIcons.HOME, "home", "Go home"),
        (CarbonIcons.ADD, "add", "Add item"),
        (CarbonIcons.SAVE, "save", "Save file"),
        (CarbonIcons.COPY, "copy", "Copy"),
        (CarbonIcons.DELETE, "delete", "Delete"),
        (CarbonIcons.SETTINGS, "settings", "Settings"),
    ]
    
    toolbar_results = create_toolbar(toolbar_buttons, style="minimal")
    for key, clicked in toolbar_results.items():
        if clicked:
            st.toast(f"{key} clicked!")
    
    # Example 3: Action buttons
    st.header("Action Buttons")
    actions = [
        ("Upload Files", CarbonIcons.UPLOAD, "action_upload"),
        ("Generate Report", CarbonIcons.CHART_BAR, "action_report"),
        ("Export Data", CarbonIcons.DOWNLOAD, "action_export"),
    ]
    
    action_results = create_action_buttons(actions, style="minimal", use_container_width=True)
    for key, clicked in action_results.items():
        if clicked:
            st.info(f"Action: {key}")