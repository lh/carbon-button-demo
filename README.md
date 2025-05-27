# Streamlit Carbon Button Component

Carbon Design System buttons for Streamlit apps with automatic dark mode support.

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.29.0+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- 🎨 **Carbon Design System** - Professional, accessible button designs
- 🌓 **Automatic Dark Mode** - Buttons adapt to user's system preferences
- 🎯 **Multiple Styles** - Primary, secondary, danger, and ghost buttons
- 🖼️ **Icon Support** - Includes 20+ Carbon icons
- ⚡ **Easy to Use** - Simple API that feels like native Streamlit
- 🎪 **Fully Customizable** - Override any color for your brand

## Installation

### For Streamlit Community Cloud Deployment

1. Copy the `carbon-button-component` folder to your project
2. Add to your `requirements.txt`:
   ```
   streamlit-carbon-button @ file:./carbon-button-component
   ```

### For Local Development

```bash
cd carbon-button-component
pip install -e .
```

## Quick Start

```python
import streamlit as st
from briquette import carbon_button, CarbonIcons

# Simple button
if carbon_button("Click me!", key="btn1"):
    st.write("Button clicked!")

# Button with icon
if carbon_button("Download", CarbonIcons.DOWNLOAD, key="btn2"):
    st.write("Downloading...")

# Danger button
if carbon_button("Delete", CarbonIcons.DELETE, key="btn3", button_type="danger"):
    st.write("Deleted!")
```

## Usage Guide

### Basic Button

```python
clicked = carbon_button(
    label="Click Me",           # Button text
    key="unique_key"           # Unique identifier (required)
)
```

### Button with Icon

```python
clicked = carbon_button(
    label="Save File",
    icon=CarbonIcons.SAVE,     # Icon from CarbonIcons class
    key="save_btn"
)
```

### Button Types

```python
# Primary (blue) - Important actions
carbon_button("Submit", key="submit", button_type="primary")

# Secondary (grey) - Default style
carbon_button("Cancel", key="cancel", button_type="secondary")

# Danger (red) - Destructive actions
carbon_button("Delete", key="delete", button_type="danger")

# Ghost (transparent) - Less prominent actions
carbon_button("Learn More", key="learn", button_type="ghost")
```

### Full Width Buttons

```python
carbon_button(
    "Process All Files",
    icon=CarbonIcons.PLAY,
    key="process",
    use_container_width=True   # Expands to container width
)
```

### Icon-Only Buttons

```python
# Just leave the label empty
carbon_button("", CarbonIcons.SETTINGS, key="settings")
```

### Custom Colors

```python
my_colors = {
    "rest_bg": "#0f62fe",      # Normal background
    "rest_text": "#ffffff",    # Normal text/icon
    "rest_border": "#0f62fe",  # Normal border
    "hover_bg": "#0353e9",     # Hover background  
    "hover_text": "#ffffff",   # Hover text/icon
    "hover_border": "#0353e9", # Hover border
    "active_bg": "#002d9c",    # Click background
    "active_text": "#ffffff",  # Click text/icon
    "active_border": "#002d9c" # Click border
}

carbon_button("Custom", key="custom", colors=my_colors)
```

## Available Icons

All icons are available through the `CarbonIcons` class:

| Icon | Usage | Description |
|------|-------|-------------|
| `ADD` | `CarbonIcons.ADD` | Plus sign |
| `CHART_BAR` | `CarbonIcons.CHART_BAR` | Bar chart |
| `CLOSE` | `CarbonIcons.CLOSE` | X mark |
| `COPY` | `CarbonIcons.COPY` | Copy document |
| `DELETE` | `CarbonIcons.DELETE` | Trash can |
| `DOCUMENT` | `CarbonIcons.DOCUMENT` | Document/file |
| `DOWNLOAD` | `CarbonIcons.DOWNLOAD` | Download arrow |
| `FILTER` | `CarbonIcons.FILTER` | Filter funnel |
| `HELP` | `CarbonIcons.HELP` | Question mark |
| `HOME` | `CarbonIcons.HOME` | House |
| `INFO` | `CarbonIcons.INFO` | Information i |
| `PLAY` | `CarbonIcons.PLAY` | Play arrow |
| `SAVE` | `CarbonIcons.SAVE` | Floppy disk |
| `SEARCH` | `CarbonIcons.SEARCH` | Magnifying glass |
| `SETTINGS` | `CarbonIcons.SETTINGS` | Gear |
| `SUCCESS` | `CarbonIcons.SUCCESS` | Checkmark |
| `UPLOAD` | `CarbonIcons.UPLOAD` | Upload arrow |
| `WARNING` | `CarbonIcons.WARNING` | Warning triangle |

## Complete Example

```python
import streamlit as st
from briquette import carbon_button, CarbonIcons

st.title("My Dashboard")

# Sidebar navigation
with st.sidebar:
    if carbon_button("🏠 Home", key="nav_home", use_container_width=True):
        st.session_state.page = "home"
    
    if carbon_button("📊 Analytics", key="nav_analytics", use_container_width=True):
        st.session_state.page = "analytics"
    
    if carbon_button("⚙️ Settings", key="nav_settings", use_container_width=True):
        st.session_state.page = "settings"

# Main toolbar
col1, col2, col3, col4 = st.columns(4)

with col1:
    if carbon_button("New", CarbonIcons.ADD, key="new", button_type="primary"):
        st.info("Creating new item...")

with col2:
    if carbon_button("Upload", CarbonIcons.UPLOAD, key="upload"):
        st.info("Upload dialog would open here")

with col3:
    if carbon_button("Download", CarbonIcons.DOWNLOAD, key="download"):
        st.info("Downloading...")

with col4:
    if carbon_button("Delete", CarbonIcons.DELETE, key="delete", button_type="danger"):
        st.warning("Are you sure?")

# Data actions
st.subheader("Data Operations")

if carbon_button("Run Analysis", CarbonIcons.PLAY, key="run", 
                 button_type="primary", use_container_width=True):
    with st.spinner("Analyzing..."):
        import time
        time.sleep(2)
    st.success("Analysis complete!")
```

## Dark Mode Support

The component automatically detects and responds to the user's system dark mode preference. No configuration needed!

**Light Mode Colors:**
- Rest: Warm grey (#e6e2e2)
- Hover: Bright white (#f5f5f5)
- Active: Teal (#50e4e0)

**Dark Mode Colors:**
- Rest: Light pink-grey (#ecdcdc)
- Hover: Off-white (#f6f4f4)
- Active: Light teal (#67cccc)

## API Reference

### carbon_button()

```python
carbon_button(
    label: str,                    # Button text
    icon: str = "",               # SVG icon string (use CarbonIcons)
    key: str = None,              # Unique key (required)
    button_type: str = "primary", # "primary", "secondary", "danger", "ghost"
    disabled: bool = False,       # Disable the button
    use_container_width: bool = False,  # Full width button
    colors: dict = None          # Custom color overrides
) -> bool                        # Returns True when clicked
```

## Troubleshooting

### Button not appearing
- Make sure you've provided a unique `key` parameter
- Check that the component is properly installed

### Icons not showing
- Use icons from the `CarbonIcons` class
- Don't modify the SVG strings

### Deployment issues
- Ensure the `carbon-button-component` folder is in your repository
- Check that `requirements.txt` includes the local package reference

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License is one of the most permissive licenses, allowing you to:
- Use the code commercially
- Modify the code
- Distribute the code
- Use the code privately

## Credits & Attribution

### Carbon Design System Icons
This component includes icons from IBM's Carbon Design System:
- Carbon Design System: https://carbondesignsystem.com/
- Carbon Icons Repository: https://github.com/carbon-design-system/carbon
- Icons License: Apache License 2.0

The Carbon icons are used under the Apache 2.0 license, which is compatible with the MIT license used for this component.

### Built With
- [Streamlit Components](https://docs.streamlit.io/library/components) - Component framework
- [React](https://reactjs.org/) - Frontend framework
- [TypeScript](https://www.typescriptlang.org/) - Type safety

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.