# Carbon Button Component - Quick Deployment Guide

## 🚀 Deploying to Streamlit Community Cloud

### Step 1: Prepare Your Repository

Your repository structure should look like this:
```
your-app/
├── streamlit_app.py           # Your Streamlit app
├── requirements.txt           # Dependencies
└── carbon-button-component/   # This component directory
    ├── carbon_button/
    │   ├── __init__.py
    │   └── frontend/          # Built React files (required!)
    ├── setup.py
    └── MANIFEST.in
```

### Step 2: Update requirements.txt

Add this line to your `requirements.txt`:
```
streamlit-carbon-button @ file:./carbon-button-component
```

### Step 3: Use in Your App

```python
from carbon_button import carbon_button, CarbonIcons

if carbon_button("Click Me", icon=CarbonIcons.UPLOAD):
    st.write("Button clicked!")
```

### Step 4: Deploy

1. Push your repository to GitHub
2. Connect to Streamlit Community Cloud
3. Deploy!

## ⚠️ Important Notes

- The `frontend/build` files MUST be included (already built for you)
- No Node.js or npm required on Streamlit Community Cloud
- The component uses the built files, not the React dev server

## 📦 What's Included

- ✅ Pre-built React frontend
- ✅ All Carbon Design System button styles
- ✅ 18 pre-defined Carbon icons
- ✅ Custom color support
- ✅ Full accessibility features

## 🐛 Troubleshooting

**Component not showing?**
- Check that `carbon_button/frontend/` contains the built files
- Ensure your import is correct: `from carbon_button import carbon_button`

**Deployment fails?**
- Make sure the entire `carbon-button-component` directory is in your repo
- Check that `requirements.txt` has the correct path

## 📝 Example App

See `streamlit_app.py` for a complete demo application ready to deploy!