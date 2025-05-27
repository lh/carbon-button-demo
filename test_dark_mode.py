"""
Test dark mode for Carbon buttons
"""
import streamlit as st
from briquette import carbon_button, CarbonIcons

st.set_page_config(page_title="Carbon Buttons - Dark Mode Test", layout="wide")

st.title("🌓 Carbon Buttons - Light & Dark Mode")
st.markdown("""
The buttons automatically adapt to your system's dark mode setting.

**To test:**
1. On macOS: System Preferences → Appearance → Select Light/Dark
2. On Windows: Settings → Personalization → Colors → Choose your mode
3. The buttons will update their colors automatically!
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Button Examples")
    if carbon_button("Save Document", icon=CarbonIcons.SAVE, key="save"):
        st.success("Saved!")
    
    if carbon_button("Upload Files", icon=CarbonIcons.UPLOAD, key="upload"):
        st.success("Uploaded!")
    
    if carbon_button("Settings", icon=CarbonIcons.SETTINGS, key="settings", button_type="ghost"):
        st.info("Settings opened")

with col2:
    st.subheader("Color Scheme")
    st.markdown("""
    **Light Mode:**
    - Background: Light grey (#e6e2e2)
    - Text: Dark (#1a1a1a)
    - Active: Teal (#50e4e0)
    
    **Dark Mode:**
    - Background: Dark grey (#3a3a3a)
    - Text: Light
    - Active: Darker teal (#67cccc)
    """)

st.divider()

# Show current mode detection
st.markdown("""
<script>
const isDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
const modeText = isDark ? '🌙 Dark Mode Detected' : '☀️ Light Mode Detected';
document.getElementById('mode-indicator').innerText = modeText;

// Update when changed
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    const newMode = e.matches ? '🌙 Dark Mode Detected' : '☀️ Light Mode Detected';
    document.getElementById('mode-indicator').innerText = newMode;
});
</script>
<div id="mode-indicator" style="font-size: 20px; font-weight: bold; margin: 20px 0;">Detecting mode...</div>
""", unsafe_allow_html=True)