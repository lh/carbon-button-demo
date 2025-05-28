# Carbon Button Component - Troubleshooting Guide

This guide captures all the issues we encountered and their solutions.

## 🔥 Critical Issues We Solved

### 1. **Component Returns NULL/undefined**

**Problem**: Buttons appear but return NULL instead of values.

**Root Cause**: Streamlit components MUST call `Streamlit.setComponentValue()` on mount.

**Solution**: In `CarbonButton.tsx`, add to `componentDidMount()`:
```typescript
const initialValue = this.props.args?.default || 0
this.setState({ numClicks: initialValue }, () => {
  Streamlit.setComponentValue(this.state.numClicks)
  Streamlit.setFrameHeight()
})
```

### 2. **Buttons Only Appear After Zoom/Resize**

**Problem**: Components invisible until browser zoom changes.

**Root Cause**: Streamlit needs to know component height.

**Solution**: Call `Streamlit.setFrameHeight()` in:
- `componentDidMount()`
- `componentDidUpdate()`

### 3. **State Lost on Streamlit Rerun**

**Problem**: Button clicks not detected or reset on rerun.

**Root Cause**: Component uses `default=0` which resets every time.

**Solution**: Track previous state in session state:
```python
# In briquette/__init__.py
prev_clicks_key = f"__carbon_button_prev_{key}"
if prev_clicks_key not in st.session_state:
    st.session_state[prev_clicks_key] = 0

component_value = _component_func(
    # ... other args ...
    default=st.session_state[prev_clicks_key],
)

clicked = False
if component_value is not None and component_value > st.session_state[prev_clicks_key]:
    clicked = True
    st.session_state[prev_clicks_key] = component_value

return clicked
```

### 4. **Import Errors on Streamlit Cloud**

**Problem**: "Module not found" or "Main module does not exist".

**Solutions**:
1. Add current directory to Python path in `app.py`:
   ```python
   import sys
   import os
   sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
   ```

2. Simple `requirements.txt` (no local paths):
   ```
   streamlit>=1.29.0
   ```

3. Ensure main file matches Streamlit Cloud settings (e.g., `app.py`)

### 5. **React Component Not Loading**

**Problem**: Component iframe empty or shows error.

**Checklist**:
1. Built files exist in `briquette/frontend/`
2. `index.html` references correct JS/CSS files
3. `MANIFEST.in` includes frontend files
4. `setup.py` package_data includes all static files

### 6. **Hidden Checkbox Approach Failed**

**Problem**: Checkboxes visible and crash app on click.

**Why it failed**: Streamlit's internal handling conflicts with programmatic state changes.

**Solution**: Proper component approach with state management (as implemented).

## 📋 Pre-Deployment Checklist

Before deploying, verify:

```bash
# 1. Frontend is built
cd frontend && npm run build
cp -r build/* ../briquette/frontend/

# 2. Package structure is correct
ls briquette/frontend/  # Should have index.html, static/

# 3. Test locally
pip install -e .
streamlit run app.py

# 4. Verify imports work
python -c "from briquette import carbon_button, CarbonIcons"
```

## 🚫 Common Pitfalls

1. **Don't use relative imports** in deployed apps
2. **Don't reference local file paths** in requirements.txt
3. **Don't forget unique keys** for each button
4. **Don't modify component state** without session state
5. **Don't skip** `Streamlit.setComponentValue()` on mount

## 🔧 Debug Commands

```bash
# Clear all caches
streamlit cache clear

# Check component registration
python -c "import streamlit.components.v1 as components; print(components)"

# Verify package installation
pip show streamlit-carbon-button

# Test component isolation
python -c "from briquette import _component_func; print(_component_func)"
```

## 💡 Key Insights

1. **Streamlit components are stateless** - each rerun remounts
2. **Session state is persistent** - use for tracking
3. **Component lifecycle** matters - initialize properly
4. **Pre-built is better** - avoid Node.js in production
5. **Simple is reliable** - minimal dependencies

These were the hard lessons that took us from "buttons don't work" to a beautiful, functional component!