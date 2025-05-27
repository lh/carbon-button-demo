# Carbon Button Component - Usage Guide for Beginners

This guide will help you add beautiful Carbon Design buttons to your Streamlit app in just a few minutes!

## 🚀 Quick Setup (5 minutes)

### Step 1: Copy the Component

Copy the entire `carbon-button-component` folder into your Streamlit project folder.

Your project structure should look like this:
```
my-streamlit-app/
├── app.py                    # Your main Streamlit app
├── requirements.txt          # Your dependencies
└── carbon-button-component/  # The component folder (copy this!)
    ├── carbon_button/
    ├── setup.py
    └── ... other files
```

### Step 2: Update requirements.txt

Add this line to your `requirements.txt`:
```
streamlit-carbon-button @ file:./carbon-button-component
```

### Step 3: Use in Your App

In your `app.py` (or whatever your main file is called):

```python
import streamlit as st
from carbon_button import carbon_button, CarbonIcons

st.title("My App")

# That's it! Now you can use carbon buttons:
if carbon_button("Click Me!", key="my_button"):
    st.balloons()
```

## 📚 Common Examples

### Example 1: Save Button
```python
if carbon_button("Save", CarbonIcons.SAVE, key="save_btn"):
    st.success("File saved!")
```

### Example 2: Delete Button (Red)
```python
if carbon_button("Delete", CarbonIcons.DELETE, key="del_btn", button_type="danger"):
    st.warning("Item deleted!")
```

### Example 3: Row of Icon Buttons
```python
col1, col2, col3 = st.columns(3)

with col1:
    if carbon_button("", CarbonIcons.HOME, key="home"):
        st.write("Going home...")

with col2:
    if carbon_button("", CarbonIcons.SETTINGS, key="settings"):
        st.write("Opening settings...")

with col3:
    if carbon_button("", CarbonIcons.HELP, key="help"):
        st.write("Getting help...")
```

### Example 4: Full Width Button
```python
if carbon_button("Download Report", CarbonIcons.DOWNLOAD, key="download",
                 use_container_width=True):
    st.write("Downloading...")
```

## 🎨 Button Types

- **Secondary** (default): Grey buttons for most actions
- **Primary**: Blue buttons for main actions
- **Danger**: Red buttons for delete/remove actions
- **Ghost**: Transparent buttons for subtle actions

```python
carbon_button("Secondary", key="b1", button_type="secondary")  # Grey (default)
carbon_button("Primary", key="b2", button_type="primary")      # Blue
carbon_button("Danger", key="b3", button_type="danger")        # Red
carbon_button("Ghost", key="b4", button_type="ghost")          # Transparent
```

## 🎯 Important Tips

### Always Use Unique Keys!
Every button needs a unique `key`:
```python
# ✅ Good - unique keys
carbon_button("Save", key="save_btn")
carbon_button("Save", key="save_btn_2")

# ❌ Bad - duplicate keys (will cause errors)
carbon_button("Save", key="save")
carbon_button("Save", key="save")
```

### Icons are Optional
```python
# With icon
carbon_button("Save", CarbonIcons.SAVE, key="save1")

# Without icon
carbon_button("Save", key="save2")
```

### Return Value
Buttons return `True` when clicked:
```python
if carbon_button("Submit", key="submit"):
    # This code runs when button is clicked
    process_form()
    st.success("Form submitted!")
```

## 🚢 Deploying to Streamlit Cloud

1. Push your project (including the `carbon-button-component` folder) to GitHub
2. Deploy on Streamlit Cloud as normal
3. The buttons will work automatically!

## 🆘 Troubleshooting

### "Component not found" error
- Make sure the `carbon-button-component` folder is in your project
- Check that `requirements.txt` has the correct line

### Button not appearing
- Make sure each button has a unique `key`
- Check for typos in the import statement

### Icons not showing
- Use icons from `CarbonIcons` class (e.g., `CarbonIcons.SAVE`)
- Don't modify the icon strings

## 📧 Need Help?

If you get stuck:
1. Check the examples above
2. Look at the main README.md for more details
3. Make sure you've followed all steps exactly

Happy coding! 🎉