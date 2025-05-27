"""
Example Streamlit app using Carbon buttons
Ready for deployment on Streamlit Community Cloud
"""

import streamlit as st
from carbon_button import carbon_button, CarbonIcons

st.set_page_config(page_title="My App with Carbon Buttons", page_icon="🚀")

st.title("My Application")
st.markdown("Using beautiful Carbon Design buttons!")

# Simple button
if carbon_button("Click Me", key="simple"):
    st.balloons()
    st.success("You clicked the button!")

# Button with icon
col1, col2, col3 = st.columns(3)

with col1:
    if carbon_button("Upload", CarbonIcons.UPLOAD, "upload", button_type="secondary"):
        st.info("Upload started...")

with col2:
    if carbon_button("Save", CarbonIcons.SAVE, "save", button_type="secondary"):
        st.success("Saved!")

with col3:
    if carbon_button("Delete", CarbonIcons.DELETE, "delete", button_type="danger"):
        st.warning("Deleted!")

# Full width button
if carbon_button("Process Everything", CarbonIcons.PLAY, "process", 
                 button_type="secondary", use_container_width=True):
    with st.spinner("Processing..."):
        import time
        time.sleep(2)
    st.success("Complete! 🎉")