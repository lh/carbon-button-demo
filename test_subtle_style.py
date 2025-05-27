"""
Test the subtle Carbon button styling with teal accents
"""
import streamlit as st
from briquette import carbon_button, CarbonIcons

st.set_page_config(page_title="Subtle Carbon Buttons", layout="wide")

st.title("Subtle Carbon Design System")
st.markdown("Beautiful, minimal buttons with teal accent on click - matching your logo")

# Main demo
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Essential Actions")
    if carbon_button("Save Document", icon=CarbonIcons.SAVE, key="save"):
        st.success("✓ Saved")
    
    if carbon_button("Upload Files", icon=CarbonIcons.UPLOAD, key="upload"):
        st.success("✓ Uploaded")
    
    if carbon_button("Download", icon=CarbonIcons.DOWNLOAD, key="download"):
        st.success("✓ Downloaded")

with col2:
    st.subheader("Tools & Settings")
    if carbon_button("Settings", icon=CarbonIcons.SETTINGS, key="settings"):
        st.info("Settings panel")
    
    if carbon_button("Filter", icon=CarbonIcons.FILTER, key="filter"):
        st.info("Filters applied")
    
    if carbon_button("Search", icon=CarbonIcons.SEARCH, key="search"):
        st.info("Search activated")

with col3:
    st.subheader("Data & Reports")
    if carbon_button("View Chart", icon=CarbonIcons.CHART_BAR, key="chart"):
        st.info("Chart displayed")
    
    if carbon_button("Documents", icon=CarbonIcons.DOCUMENT, key="doc"):
        st.info("Documents opened")
    
    if carbon_button("Copy", icon=CarbonIcons.COPY, key="copy"):
        st.info("Copied to clipboard")

st.divider()

# Icon toolbar
st.subheader("Clean Icon Toolbar")
cols = st.columns(8)
icons = [
    (CarbonIcons.HOME, "icon_home", "Home"),
    (CarbonIcons.ADD, "icon_add", "Add"),
    (CarbonIcons.DOCUMENT, "icon_docs", "Documents"),
    (CarbonIcons.CHART_BAR, "icon_chart", "Analytics"),
    (CarbonIcons.SETTINGS, "icon_settings", "Settings"),
    (CarbonIcons.INFO, "icon_info", "Info"),
]

for i, (icon, key, label) in enumerate(icons[:6]):
    with cols[i]:
        if carbon_button("", icon=icon, key=key, button_type="ghost"):
            st.toast(label)

st.divider()

# Task manager with subtle styling
st.subheader("Task Manager")
if 'tasks' not in st.session_state:
    st.session_state.tasks = ["Review documentation", "Update dependencies", "Run tests"]

col1, col2 = st.columns([3, 1])
with col1:
    new_task = st.text_input("Add a task", label_visibility="collapsed", placeholder="Enter a new task...")
with col2:
    if carbon_button("Add Task", icon=CarbonIcons.ADD, key="add_task", use_container_width=True) and new_task:
        st.session_state.tasks.append(new_task)
        st.rerun()

for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([10, 1, 1])
    with col1:
        st.write(task)
    with col2:
        if carbon_button("", icon=CarbonIcons.SUCCESS, key=f"done_{i}", button_type="ghost"):
            st.success(f"✓ {task}")
    with col3:
        if carbon_button("", icon=CarbonIcons.DELETE, key=f"del_{i}", button_type="ghost"):
            st.session_state.tasks.pop(i)
            st.rerun()

st.divider()
st.info("💡 Click and hold buttons to see the beautiful teal accent color that matches your logo!")