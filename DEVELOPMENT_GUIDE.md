# Carbon Button Component - Development Guide

This guide covers everything you need to develop, customize, and deploy the Carbon Button component.

## 🚀 Quick Start

### Local Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/lh/carbon-button-demo.git
cd carbon-button-demo

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install in development mode
pip install -e .

# 4. Run the demo
streamlit run app.py
```

### Frontend Development (if you need to modify the React component)

```bash
# 1. Install Node.js dependencies
cd frontend
npm install

# 2. Start React development server
npm start

# 3. In another terminal, set development mode and run Streamlit
export STREAMLIT_CARBON_BUTTON_DEV_MODE=true
streamlit run app.py
```

## 🎨 Color Customization

### Using the Live Color Tuner

The color tuner lets you customize button colors in real-time:

```bash
streamlit run color_tuner_live.py
```

This tool allows you to:
- Adjust rest, hover, and active states
- See changes instantly
- Export color configurations
- Test in both light and dark modes

### Current Color Scheme

**Light Mode:**
- Rest: `#e6e2e2` (warm grey)
- Hover: `#f5f5f5` (bright grey)
- Active: `#50e4e0` (teal - matches your logo)

**Dark Mode:**
- Rest: `#ecdcdc` (pink-grey)
- Hover: `#f6f4f4` (very light)
- Active: `#67cccc` (darker teal)

### Applying Custom Colors

```python
custom_colors = {
    "rest_bg": "#e6e2e2",
    "rest_text": "#1a1a1a",
    "rest_border": "#cccccc",
    "hover_bg": "#f5f5f5",
    "hover_text": "#000000",
    "hover_border": "#b0b0b0",
    "active_bg": "#50e4e0",
    "active_text": "#ffffff",
    "active_border": "#404040",
}

carbon_button("Custom Button", colors=custom_colors, key="custom")
```

## 📦 Using in Your Application

### Basic Usage

```python
import streamlit as st
from briquette import carbon_button, CarbonIcons

# Simple button
if carbon_button("Click Me", key="simple"):
    st.write("Button clicked!")

# Button with icon
if carbon_button("Save", icon=CarbonIcons.SAVE, key="save"):
    st.success("Saved!")

# Full width button
carbon_button("Process", key="process", use_container_width=True)

# Different button types
carbon_button("Primary", key="p1", button_type="primary")
carbon_button("Secondary", key="p2", button_type="secondary")
carbon_button("Danger", key="p3", button_type="danger")
carbon_button("Ghost", key="p4", button_type="ghost")
```

### Available Icons

```python
from briquette import CarbonIcons

# File operations
CarbonIcons.UPLOAD
CarbonIcons.DOWNLOAD
CarbonIcons.SAVE
CarbonIcons.COPY
CarbonIcons.DELETE

# Navigation
CarbonIcons.HOME
CarbonIcons.SEARCH
CarbonIcons.SETTINGS
CarbonIcons.FILTER

# Actions
CarbonIcons.ADD
CarbonIcons.CLOSE
CarbonIcons.PLAY
CarbonIcons.INFO
CarbonIcons.HELP
CarbonIcons.WARNING
CarbonIcons.SUCCESS

# Data
CarbonIcons.CHART_BAR
CarbonIcons.DOCUMENT
```

### Advanced Patterns

1. **Icon-only buttons:**
```python
carbon_button("", icon=CarbonIcons.SETTINGS, key="settings_icon")
```

2. **Button groups:**
```python
col1, col2, col3 = st.columns(3)
with col1:
    carbon_button("Option 1", key="opt1")
with col2:
    carbon_button("Option 2", key="opt2")
with col3:
    carbon_button("Option 3", key="opt3")
```

3. **Task management pattern:**
```python
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Add task:")
if carbon_button("Add", icon=CarbonIcons.ADD, key="add_task") and new_task:
    st.session_state.tasks.append(new_task)
    st.rerun()

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([6, 1])
    with col1:
        st.write(task)
    with col2:
        if carbon_button("", icon=CarbonIcons.DELETE, key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.rerun()
```

## 🏗️ Building & Deployment

### Building the Frontend

```bash
# Build the React component
cd frontend
npm run build

# Copy built files to component directory
cp -r build/* ../briquette/frontend/
```

### Creating a Python Package

```bash
# Build the package
python setup.py sdist bdist_wheel

# The package will be in dist/
ls dist/
```

### Deployment Options

1. **Direct from GitHub:**
```bash
pip install git+https://github.com/lh/carbon-button-demo.git
```

2. **PyPI Publishing:**
```bash
pip install twine
twine upload dist/*
# Then users can: pip install streamlit-carbon-button
```

3. **Streamlit Community Cloud:**
- Push to GitHub
- Set main file to `app.py`
- Requirements only needs `streamlit>=1.29.0`

## 🧪 Testing & Debugging

### Run All Tests
```bash
# Verify setup
python verify_setup.py

# Test components
streamlit run test_subtle_style.py
streamlit run test_dark_mode.py
streamlit run test_visibility.py
```

### Debug Tools
- `diagnose_buttons.py` - Diagnose button issues
- `debug_svg.py` - Debug icon rendering
- `test_connection.py` - Test component connection

## 📁 Project Structure

```
carbon-button-component/
├── briquette/              # Python component package
│   ├── __init__.py        # Component implementation
│   └── frontend/          # Pre-built React files
├── frontend/              # React source code
│   ├── src/
│   │   ├── CarbonButton.tsx
│   │   └── index.tsx
│   └── package.json
├── app.py                 # Main demo app
├── color_tuner_live.py    # Color customization tool
├── setup.py              # Package configuration
└── requirements.txt      # Python dependencies
```

## 🔧 Troubleshooting

1. **Buttons not appearing:**
   - Check browser console for errors
   - Verify `briquette/frontend/` contains built files
   - Try `streamlit cache clear`

2. **Import errors:**
   - Ensure package is installed: `pip install -e .`
   - Check Python path includes current directory

3. **Styling issues:**
   - Clear browser cache
   - Check if CSS files are in `briquette/frontend/static/css/`

4. **Dark mode not working:**
   - Component detects system preference
   - Test by changing OS appearance settings

## 📝 Important Notes

- The component is **pre-built** - no Node.js required for deployment
- All icons are **embedded SVGs** - no external dependencies
- State management uses **session state** for persistence
- Dark mode is **automatic** based on system preference

## 🎉 Success!

Your Carbon Button component is now:
- ✅ Deployed at https://carbon-button-demo.streamlit.app/
- ✅ Installable via GitHub
- ✅ Fully customizable with the color tuner
- ✅ Ready for use in any Streamlit application

For questions or issues, please open an issue on GitHub!