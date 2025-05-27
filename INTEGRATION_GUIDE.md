# 🚀 Carbon Button Integration Guide

## Quick Start

### 1. Install the Component

```bash
cd carbon-button-component
pip install -e .
```

### 2. Basic Usage in Your App

```python
import streamlit as st
from carbon_button import carbon_button, CarbonIcons

# Simple button
if carbon_button("Save", CarbonIcons.SAVE, key="save_btn"):
    st.success("Saved!")
```

### 3. Using the Styled Buttons (Recommended)

```python
import streamlit as st
from carbon_button_styles import (
    inject_carbon_styles,
    minimal_button,
    icon_button,
    create_toolbar,
    CarbonIcons
)

# IMPORTANT: Add this at the top of your app
inject_carbon_styles()

# Your minimal grey style buttons
if minimal_button("Upload", CarbonIcons.UPLOAD, key="upload"):
    st.success("File uploaded!")

# Icon-only button
if icon_button(CarbonIcons.SETTINGS, key="settings", tooltip="Open settings"):
    st.info("Settings clicked")

# Create a toolbar
toolbar = create_toolbar([
    (CarbonIcons.HOME, "home", "Home"),
    (CarbonIcons.SAVE, "save", "Save"),
    (CarbonIcons.COPY, "copy", "Copy"),
])
```

## 📋 Complete Example App

```python
import streamlit as st
from carbon_button_styles import *

st.set_page_config(page_title="My App", page_icon="📱")

# Essential: Inject the custom styles
inject_carbon_styles()

st.title("My Document Manager")

# Search bar with button
col1, col2 = st.columns([5, 1])
with col1:
    search = st.text_input("Search files...", label_visibility="collapsed")
with col2:
    if minimal_button("Search", CarbonIcons.SEARCH, "search"):
        st.info(f"Searching for: {search}")

# Document actions toolbar
st.subheader("Quick Actions")
toolbar = create_toolbar([
    (CarbonIcons.ADD, "new", "New document"),
    (CarbonIcons.UPLOAD, "upload", "Upload"),
    (CarbonIcons.DOWNLOAD, "download", "Download"),
    (CarbonIcons.DELETE, "delete", "Delete"),
], style="minimal")

# Handle toolbar clicks
for action, clicked in toolbar.items():
    if clicked:
        st.toast(f"{action} action triggered!")

# File list with action buttons
files = ["report.pdf", "data.xlsx", "presentation.pptx"]

for i, file in enumerate(files):
    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
    
    with col1:
        st.write(f"📄 {file}")
    with col2:
        if icon_button(CarbonIcons.DOWNLOAD, f"dl_{i}", style="minimal"):
            st.toast(f"Downloading {file}")
    with col3:
        if icon_button(CarbonIcons.COPY, f"cp_{i}", style="minimal"):
            st.toast("Link copied!")
    with col4:
        if icon_button(CarbonIcons.DELETE, f"del_{i}", style="outlined"):
            st.error(f"Delete {file}?")
```

## 🎨 Button Styles

### Minimal (Your Main Style)
```python
minimal_button("Label", CarbonIcons.ICON, "key")
```
- Grey background (#f4f4f4)
- Black icon (#393939)
- Darker on hover (#e0e0e0)
- Inverts on click (white on dark grey)

### Outlined
```python
outlined_button("Label", CarbonIcons.ICON, "key")
```
- Transparent background
- Black border
- Fills with black on hover

### Primary
```python
primary_button("Label", CarbonIcons.ICON, "key")
```
- Carbon blue (#0f62fe)
- White text/icons
- Darker blue on hover

### Danger
```python
danger_button("Label", CarbonIcons.ICON, "key")
```
- Red background (#da1e28)
- For destructive actions

## 🛠️ Advanced Features

### Full Width Buttons
```python
minimal_button("Submit", CarbonIcons.ADD, "submit", use_container_width=True)
```

### Disabled State
```python
minimal_button("Can't Click", CarbonIcons.CLOSE, "disabled", disabled=True)
```

### Icon-Only with Tooltip
```python
icon_button(CarbonIcons.HELP, "help", tooltip="Get help", style="minimal")
```

### Button Groups
```python
actions = [
    ("Save Draft", CarbonIcons.SAVE, "save_draft"),
    ("Publish", CarbonIcons.UPLOAD, "publish"),
    ("Delete", CarbonIcons.DELETE, "delete"),
]

results = create_action_buttons(actions, style="minimal")
for key, clicked in results.items():
    if clicked:
        # Handle action
        pass
```

## 📦 Available Icons

- **File Operations**: UPLOAD, DOWNLOAD, SAVE, COPY, DELETE
- **Navigation**: HOME, CLOSE, ADD, SEARCH, FILTER
- **Actions**: PLAY, SETTINGS, HELP, INFO, WARNING
- **Data**: CHART_BAR, DOCUMENT, SUCCESS

## 💡 Tips

1. **Always inject styles**: Call `inject_carbon_styles()` once at the top
2. **Use consistent style**: Stick to minimal for most buttons
3. **Icon-only for toolbars**: Saves space, looks clean
4. **Tooltips for icon buttons**: Improves usability
5. **Danger sparingly**: Only for destructive actions

## 🐛 Troubleshooting

**Buttons not styled correctly?**
- Make sure you called `inject_carbon_styles()`
- Check that you're using the style wrapper functions

**Icons not showing?**
- Verify the React dev server is running (for dev mode)
- Check browser console for errors

**Clicks not registering?**
- Ensure unique keys for each button
- Don't reuse keys across reruns

---

Ready to build amazing UIs with proper Carbon Design buttons! 🚀