"""
Test Carbon Button with Beautiful Icons and Styling
"""
import streamlit as st
from briquette import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Button Beauty Test", layout="wide")

st.title("🎨 Carbon Design System Buttons")
st.markdown("Beautiful, accessible buttons with IBM's Carbon Design System")

# Test different button types with icons
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Primary Actions")
    if carbon_button("Upload File", icon=CarbonIcons.UPLOAD, key="upload", button_type="primary"):
        st.success("✅ Upload initiated!")
    
    if carbon_button("Save Document", icon=CarbonIcons.SAVE, key="save", button_type="primary"):
        st.success("✅ Document saved!")
    
    if carbon_button("Download", icon=CarbonIcons.DOWNLOAD, key="download", button_type="primary"):
        st.success("✅ Download started!")

with col2:
    st.subheader("Secondary Actions")
    if carbon_button("Copy to Clipboard", icon=CarbonIcons.COPY, key="copy", button_type="secondary"):
        st.info("📋 Copied!")
    
    if carbon_button("Filter Results", icon=CarbonIcons.FILTER, key="filter", button_type="secondary"):
        st.info("🔍 Filter applied!")
    
    if carbon_button("View Chart", icon=CarbonIcons.CHART_BAR, key="chart", button_type="secondary"):
        st.info("📊 Chart displayed!")

with col3:
    st.subheader("Danger Actions")
    if carbon_button("Delete Item", icon=CarbonIcons.DELETE, key="delete", button_type="danger"):
        st.error("🗑️ Item deleted!")
    
    if carbon_button("Close Window", icon=CarbonIcons.CLOSE, key="close", button_type="danger"):
        st.error("❌ Window closed!")
    
    if carbon_button("Warning", icon=CarbonIcons.WARNING, key="warning", button_type="danger"):
        st.error("⚠️ Warning acknowledged!")

with col4:
    st.subheader("Ghost Actions")
    if carbon_button("Settings", icon=CarbonIcons.SETTINGS, key="settings", button_type="ghost"):
        st.write("⚙️ Settings opened")
    
    if carbon_button("Search", icon=CarbonIcons.SEARCH, key="search", button_type="ghost"):
        st.write("🔍 Search activated")
    
    if carbon_button("Help", icon=CarbonIcons.HELP, key="help", button_type="ghost"):
        st.write("❓ Help opened")

st.divider()

# Icon-only buttons
st.subheader("Icon-Only Buttons")
cols = st.columns(8)
icon_buttons = [
    ("add", CarbonIcons.ADD, "Add new item"),
    ("home", CarbonIcons.HOME, "Go home"),
    ("info", CarbonIcons.INFO, "More information"),
    ("play", CarbonIcons.PLAY, "Play media"),
    ("doc", CarbonIcons.DOCUMENT, "View document"),
    ("success", CarbonIcons.SUCCESS, "Success!"),
]

for i, (key, icon, tooltip) in enumerate(icon_buttons):
    with cols[i % 8]:
        if carbon_button("", icon=icon, key=f"icon_{key}", button_type="ghost"):
            st.write(tooltip)

st.divider()

# Full width buttons
st.subheader("Full Width Buttons")
col1, col2 = st.columns(2)

with col1:
    if carbon_button("Full Width Primary", icon=CarbonIcons.ADD, key="full_primary", 
                     button_type="primary", use_container_width=True):
        st.success("Full width primary clicked!")

with col2:
    if carbon_button("Full Width Secondary", icon=CarbonIcons.SETTINGS, key="full_secondary", 
                     button_type="secondary", use_container_width=True):
        st.info("Full width secondary clicked!")

st.divider()

# Custom colored buttons
st.subheader("Custom Colored Buttons")
purple_button = {
    "rest_bg": "#6929c4",
    "rest_text": "#ffffff",
    "hover_bg": "#491d8b",
    "hover_text": "#ffffff",
    "active_bg": "#31135e",
    "active_text": "#ffffff"
}

teal_button = {
    "rest_bg": "#009d9a",
    "rest_text": "#ffffff",
    "hover_bg": "#007d79",
    "hover_text": "#ffffff", 
    "active_bg": "#005a5a",
    "active_text": "#ffffff"
}

col1, col2, col3 = st.columns(3)
with col1:
    if carbon_button("Purple Action", icon=CarbonIcons.PLAY, colors=purple_button, key="purple"):
        st.write("🟣 Purple button clicked!")

with col2:
    if carbon_button("Teal Action", icon=CarbonIcons.SUCCESS, colors=teal_button, key="teal"):
        st.write("🟦 Teal button clicked!")

st.divider()

# Interactive demo
st.subheader("Interactive Task Manager")
if 'tasks' not in st.session_state:
    st.session_state.tasks = ["Design new feature", "Review pull request", "Update documentation"]

new_task = st.text_input("Add a new task:")
if carbon_button("Add Task", icon=CarbonIcons.ADD, key="add_task", button_type="primary") and new_task:
    st.session_state.tasks.append(new_task)
    st.rerun()

for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([6, 1, 1])
    with col1:
        st.write(f"📌 {task}")
    with col2:
        if carbon_button("", icon=CarbonIcons.SUCCESS, key=f"complete_{i}", button_type="ghost"):
            st.success(f"✅ Completed: {task}")
    with col3:
        if carbon_button("", icon=CarbonIcons.DELETE, key=f"delete_{i}", button_type="danger"):
            st.session_state.tasks.pop(i)
            st.rerun()