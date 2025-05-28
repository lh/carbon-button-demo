# Clean Package Repository Structure

## Recommended: Create `streamlit-carbon-button` Repository

For production use, create a clean package-only repository:

### Repository Structure
```
streamlit-carbon-button/
├── src/
│   └── briquette/
│       ├── __init__.py        # Component wrapper (340 lines)
│       └── frontend/          # Built files only
│           ├── index.html
│           └── static/
│               ├── css/
│               │   └── main.*.css
│               └── js/
│                   └── main.*.js
├── frontend-src/              # Source for developers
│   ├── src/
│   │   ├── CarbonButton.tsx
│   │   ├── index.tsx
│   │   └── index.css
│   ├── package.json
│   ├── tsconfig.json
│   └── README.md             # Frontend dev instructions
├── examples/
│   ├── basic_usage.py        # Simple example
│   ├── custom_colors.py      # Color customization
│   └── requirements.txt      # Just: streamlit>=1.29.0
├── setup.py                  # Package config
├── setup.cfg                 # Additional metadata
├── MANIFEST.in              # Include frontend files
├── requirements.txt         # Just: streamlit>=0.63
├── README.md               # User documentation
├── LICENSE                 # MIT License
├── CHANGELOG.md           # Version history
└── .gitignore            # Exclude node_modules, etc.
```

### Installation Methods

1. **From PyPI (future):**
   ```bash
   pip install streamlit-carbon-button
   ```

2. **From GitHub:**
   ```bash
   pip install git+https://github.com/lh/streamlit-carbon-button.git
   ```

3. **Development:**
   ```bash
   git clone https://github.com/lh/streamlit-carbon-button.git
   cd streamlit-carbon-button
   pip install -e .
   ```

### Why Separate?

1. **Clean installs** - No test files in user's environment
2. **Smaller package** - ~2MB instead of ~50MB
3. **Professional** - Like other Streamlit components
4. **Maintainable** - Clear separation of concerns

### Migration Commands

```bash
# Create new clean repo
mkdir streamlit-carbon-button-clean
cd streamlit-carbon-button-clean

# Copy only essential files
cp -r ../carbon-button-component/briquette src/
cp ../carbon-button-component/setup.py .
cp ../carbon-button-component/MANIFEST.in .
cp ../carbon-button-component/LICENSE .

# Copy frontend source for development
mkdir frontend-src
cp -r ../carbon-button-component/frontend/src frontend-src/
cp ../carbon-button-component/frontend/package.json frontend-src/
cp ../carbon-button-component/frontend/tsconfig.json frontend-src/

# Create minimal examples
mkdir examples
echo "from briquette import carbon_button, CarbonIcons

import streamlit as st

if carbon_button('Click me!', icon=CarbonIcons.PLAY, key='demo'):
    st.balloons()
" > examples/basic_usage.py

# Initialize git
git init
git add .
git commit -m "Initial commit: Clean package structure"
```

This gives users a professional package without the development clutter!