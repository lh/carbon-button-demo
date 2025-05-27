# Carbon Button Demo - Streamlit Component

Beautiful, accessible buttons using IBM's Carbon Design System for Streamlit applications.

🎨 **[Live Demo on Streamlit Cloud](https://carbon-button-demo.streamlit.app/)**

## Features

- ✨ **Subtle Styling**: Elegant grey buttons with teal accent on click
- 🌓 **Dark Mode**: Automatic adaptation with pink-grey tones
- 🎯 **20px Icons**: Crisp, larger icons for better visibility
- 🎨 **Logo Match**: Teal accent color matches your branding
- ♿ **Accessible**: Following Carbon Design System principles
- 🚀 **Easy Deploy**: Pre-built - no Node.js required

## Installation

```bash
pip install git+https://github.com/lh/carbon-button-demo.git
```

## Quick Start

```python
import streamlit as st
from briquette import carbon_button, CarbonIcons

if carbon_button("Save Document", icon=CarbonIcons.SAVE, key="save"):
    st.success("Document saved!")
```

## Button Types

All button types use the subtle grey palette by default:
- **Primary**: Main actions
- **Secondary**: Secondary actions  
- **Danger**: Destructive actions (soft coral)
- **Ghost**: Minimal style with border

## Icons

Includes 18 Carbon Design System icons:
- UPLOAD, DOWNLOAD, SAVE, COPY, DELETE
- ADD, CLOSE, SETTINGS, SEARCH, FILTER
- CHART_BAR, DOCUMENT, PLAY, HELP, WARNING
- HOME, INFO, SUCCESS

## Color Scheme

**Light Mode:**
- Rest: `#e6e2e2` (warm grey)
- Hover: `#f5f5f5` (bright)
- Active: `#50e4e0` (teal)

**Dark Mode:**
- Rest: `#ecdcdc` (pink-grey)
- Hover: `#f6f4f4` (very light)
- Active: `#67cccc` (darker teal)

## Development

This component is pre-built for deployment. To modify:

1. Clone the repository
2. Install dependencies: `cd frontend && npm install`
3. Make changes to `frontend/src/CarbonButton.tsx`
4. Build: `npm run build`
5. Copy build files: `cp -r build/* ../briquette/frontend/`

## License

MIT License - See LICENSE file

## Credits

- Icons from [IBM Carbon Design System](https://carbondesignsystem.com/) (Apache 2.0)
- Component by Luke Herbert