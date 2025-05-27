# Streamlit Carbon Button - Deployment Guide

This guide explains how to use the Carbon Button component in applications deployed on Streamlit Community Cloud.

## Installation

### Option 1: Install from Local Package (Recommended for Development)

1. Include the package in your `requirements.txt`:
```
streamlit-carbon-button @ file:./carbon-button-component
```

2. Place the `carbon-button-component` directory in your project root.

### Option 2: Install from Git (Recommended for Production)

Add to your `requirements.txt`:
```
streamlit-carbon-button @ git+https://github.com/yourusername/streamlit-carbon-button.git
```

### Option 3: Install from PyPI (When Published)

```
streamlit-carbon-button==1.0.1
```

## Usage in Your Streamlit App

```python
import streamlit as st
from carbon_button import carbon_button, CarbonIcons

# Basic button
if carbon_button("Click Me"):
    st.write("Button clicked!")

# Button with icon
if carbon_button("Download", icon=CarbonIcons.DOWNLOAD, button_type="secondary"):
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
```

## Available Button Types

- `primary` - Blue primary action button
- `secondary` - Gray secondary action button  
- `danger` - Red danger/destructive action button
- `ghost` - Transparent ghost button

## Pre-defined Icons

The `CarbonIcons` class provides these icons:
- `UPLOAD`, `DOWNLOAD`, `SAVE`, `COPY`, `DELETE`
- `ADD`, `CLOSE`, `SETTINGS`, `SEARCH`, `FILTER`
- `CHART_BAR`, `DOCUMENT`, `PLAY`, `HELP`, `WARNING`
- `HOME`, `INFO`, `SUCCESS`

## Deployment Checklist

1. ✅ Frontend is built (`npm run build` in frontend directory)
2. ✅ Built files are in `carbon_button/frontend/`
3. ✅ Package is properly configured in `setup.py`
4. ✅ `MANIFEST.in` includes frontend files
5. ✅ Component works without React dev server

## Directory Structure

```
carbon-button-component/
├── carbon_button/
│   ├── __init__.py          # Main component code
│   └── frontend/            # Built React files
│       ├── index.html
│       ├── asset-manifest.json
│       └── static/
│           ├── css/
│           └── js/
├── frontend/                # React source code
│   ├── src/
│   ├── package.json
│   └── build/              # Build output
├── setup.py                 # Package configuration
└── MANIFEST.in             # File inclusion rules
```

## Troubleshooting

### Component not displaying
- Ensure the frontend is built (`npm run build`)
- Check that built files exist in `carbon_button/frontend/`
- Verify the component is properly imported

### Icons not showing
- Make sure to pass valid SVG strings to the `icon` parameter
- Use pre-defined icons from `CarbonIcons` class

### Styling issues
- The component uses inline styles that should work across environments
- Custom colors can be passed via the `colors` parameter

## Development vs Production

The component automatically detects if it's in development mode by checking the `STREAMLIT_CARBON_BUTTON_DEV_MODE` environment variable. In production (Streamlit Community Cloud), it will always use the built files.