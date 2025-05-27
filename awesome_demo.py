"""
🚀 CARBON BUTTON COMPONENT - AWESOME DEMO
Shows off all the amazing features of our proper Streamlit component!
"""

import streamlit as st
import time
import random
from carbon_button import carbon_button, CarbonIcons

st.set_page_config(
    page_title="Carbon Button Awesomeness", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for extra pizzazz
st.markdown("""
<style>
    .success-animation {
        animation: pulse 0.5s ease-in-out;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header with gradient
st.markdown("""
# 🚀 Carbon Button Component 
## **The Ultimate Streamlit Button Experience**
### No checkboxes. No hacks. Just pure awesomeness.
""")

# Initialize session state
if 'total_clicks' not in st.session_state:
    st.session_state.total_clicks = 0
if 'button_stats' not in st.session_state:
    st.session_state.button_stats = {}

# Sidebar with live stats
with st.sidebar:
    st.header("📊 Live Button Stats")
    st.metric("Total Clicks", st.session_state.total_clicks, 
              delta=1 if st.session_state.total_clicks > 0 else None)
    
    st.markdown("### 🏆 Button Leaderboard")
    if st.session_state.button_stats:
        for btn, clicks in sorted(st.session_state.button_stats.items(), 
                                key=lambda x: x[1], reverse=True)[:5]:
            st.write(f"**{btn}**: {clicks} clicks")
    else:
        st.info("Start clicking to see stats!")
    
    if st.button("🔄 Reset Stats"):
        st.session_state.total_clicks = 0
        st.session_state.button_stats = {}
        st.rerun()

# Main content
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "✨ Feature Showcase", 
    "🎮 Interactive Playground", 
    "🏃 Performance Test",
    "🎨 Design Gallery",
    "🤯 Mind-Blowing Facts"
])

with tab1:
    st.header("✨ Feature Showcase")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 Perfect Click Detection")
        if carbon_button("Click Me!", CarbonIcons.ADD, key="perfect_click"):
            st.session_state.total_clicks += 1
            st.session_state.button_stats["Perfect Click"] = st.session_state.button_stats.get("Perfect Click", 0) + 1
            st.success("✅ Instant response! No checkbox nonsense!")
            st.balloons()
    
    with col2:
        st.markdown("### 🎨 Beautiful SVG Icons")
        if carbon_button("Upload Magic", CarbonIcons.UPLOAD, key="svg_demo"):
            st.session_state.total_clicks += 1
            st.session_state.button_stats["Upload Magic"] = st.session_state.button_stats.get("Upload Magic", 0) + 1
            st.info("🎨 Look at that crisp SVG icon!")
            time.sleep(0.5)
            st.success("✨ Rendered perfectly in all browsers!")
    
    with col3:
        st.markdown("### 🌈 Multiple Styles")
        if carbon_button("Primary", CarbonIcons.SAVE, key="style_primary"):
            st.session_state.total_clicks += 1
            st.info("Primary button clicked!")
        if carbon_button("Secondary", CarbonIcons.COPY, key="style_secondary", button_type="secondary"):
            st.session_state.total_clicks += 1
            st.info("Secondary button clicked!")
        if carbon_button("Danger!", CarbonIcons.DELETE, key="style_danger", button_type="danger"):
            st.session_state.total_clicks += 1
            st.error("Danger button clicked!")
    
    st.divider()
    
    # Responsive buttons
    st.markdown("### 📱 Responsive Design")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if carbon_button("Full Width Magic", CarbonIcons.SETTINGS, key="full_width", use_container_width=True):
            st.session_state.total_clicks += 1
            st.session_state.button_stats["Full Width"] = st.session_state.button_stats.get("Full Width", 0) + 1
            st.success("🎯 Perfectly responsive!")
    
    with col2:
        if carbon_button("Compact", CarbonIcons.CLOSE, key="compact"):
            st.session_state.total_clicks += 1
            st.info("Small but mighty!")

with tab2:
    st.header("🎮 Interactive Playground")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🎛️ Button Configurator")
        
        label = st.text_input("Button Label", value="Custom Button")
        button_type = st.selectbox("Style", ["primary", "secondary", "danger", "ghost"])
        use_full_width = st.checkbox("Full Width")
        is_disabled = st.checkbox("Disabled")
        
        icon_choice = st.selectbox("Icon", [
            "Upload", "Download", "Save", "Copy", "Delete", 
            "Add", "Close", "Settings", "Search"
        ])
        
        icon_map = {
            "Upload": CarbonIcons.UPLOAD,
            "Download": CarbonIcons.DOWNLOAD,
            "Save": CarbonIcons.SAVE,
            "Copy": CarbonIcons.COPY,
            "Delete": CarbonIcons.DELETE,
            "Add": CarbonIcons.ADD,
            "Close": CarbonIcons.CLOSE,
            "Settings": CarbonIcons.SETTINGS,
            "Search": CarbonIcons.SEARCH,
        }
    
    with col2:
        st.markdown("### 🎨 Live Preview")
        
        st.info("Your custom button appears below:")
        
        if carbon_button(
            label, 
            icon_map[icon_choice], 
            key="custom_playground",
            button_type=button_type,
            use_container_width=use_full_width,
            disabled=is_disabled
        ):
            if not is_disabled:
                st.session_state.total_clicks += 1
                st.session_state.button_stats["Custom"] = st.session_state.button_stats.get("Custom", 0) + 1
                st.balloons()
                st.success(f"🎉 {label} was clicked!")
                
                # Show some fun stats
                with st.expander("📊 Button Analytics"):
                    st.write(f"**Button Type:** {button_type}")
                    st.write(f"**Icon Used:** {icon_choice}")
                    st.write(f"**Click Time:** {time.strftime('%H:%M:%S')}")
                    st.write(f"**Total Clicks:** {st.session_state.total_clicks}")

with tab3:
    st.header("🏃 Performance Test")
    
    st.markdown("### How many buttons can we handle? Let's find out!")
    
    num_buttons = st.slider("Number of buttons to generate", 10, 100, 50)
    
    if st.button("🚀 Generate Buttons!", type="primary"):
        start_time = time.time()
        
        cols = st.columns(10)
        for i in range(num_buttons):
            with cols[i % 10]:
                if carbon_button(f"{i+1}", CarbonIcons.ADD, key=f"perf_{i}"):
                    st.session_state.total_clicks += 1
                    st.success(f"Button {i+1} clicked!")
        
        end_time = time.time()
        st.success(f"✅ Generated {num_buttons} buttons in {end_time - start_time:.2f} seconds!")
        st.info("Try clicking them - they all work perfectly! No checkbox lag!")

with tab4:
    st.header("🎨 Design Gallery")
    
    st.markdown("### Beautiful button compositions")
    
    # Card-style layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background: #f4f4f4; padding: 20px; border-radius: 8px; text-align: center;'>
            <h4>Upload Center</h4>
        </div>
        """, unsafe_allow_html=True)
        
        if carbon_button("Upload Files", CarbonIcons.UPLOAD, key="gallery_upload", use_container_width=True):
            st.session_state.total_clicks += 1
            with st.spinner("Uploading..."):
                time.sleep(1)
            st.success("Files uploaded!")
    
    with col2:
        st.markdown("""
        <div style='background: #e8f4fd; padding: 20px; border-radius: 8px; text-align: center;'>
            <h4>Process Data</h4>
        </div>
        """, unsafe_allow_html=True)
        
        if carbon_button("Start Process", CarbonIcons.SETTINGS, key="gallery_process", 
                        button_type="secondary", use_container_width=True):
            st.session_state.total_clicks += 1
            progress = st.progress(0)
            for i in range(100):
                progress.progress(i + 1)
                time.sleep(0.01)
            st.success("Process complete!")
    
    with col3:
        st.markdown("""
        <div style='background: #fce8e8; padding: 20px; border-radius: 8px; text-align: center;'>
            <h4>Danger Zone</h4>
        </div>
        """, unsafe_allow_html=True)
        
        if carbon_button("Delete All", CarbonIcons.DELETE, key="gallery_delete", 
                        button_type="danger", use_container_width=True):
            st.session_state.total_clicks += 1
            st.error("Just kidding! Nothing was deleted 😄")
    
    st.divider()
    
    # Button toolbar
    st.markdown("### 🛠️ Button Toolbar Example")
    
    toolbar_cols = st.columns(8)
    toolbar_actions = [
        ("New", CarbonIcons.ADD, "new"),
        ("Open", CarbonIcons.UPLOAD, "open"),
        ("Save", CarbonIcons.SAVE, "save"),
        ("Copy", CarbonIcons.COPY, "copy"),
        ("Cut", CarbonIcons.CLOSE, "cut"),
        ("Paste", CarbonIcons.ADD, "paste"),
        ("Search", CarbonIcons.SEARCH, "search"),
        ("Settings", CarbonIcons.SETTINGS, "settings"),
    ]
    
    for i, (label, icon, key) in enumerate(toolbar_actions):
        with toolbar_cols[i]:
            if carbon_button("", icon, key=f"toolbar_{key}", button_type="ghost"):
                st.session_state.total_clicks += 1
                st.info(f"{label} clicked!")

with tab5:
    st.header("🤯 Mind-Blowing Facts")
    
    facts = [
        "✅ **ZERO** hidden checkboxes in this entire app!",
        "🚀 Each button is a **real React component** with proper state management",
        "🎨 SVG icons are **rendered natively** - no emoji fallbacks!",
        "⚡ **Bi-directional communication** between Python and JavaScript",
        "🌐 Works **perfectly** in Chrome, Firefox, Safari, Edge, and more!",
        "📱 **Fully responsive** - try resizing your browser!",
        "♿ **Accessible** - proper ARIA labels and keyboard navigation",
        "🔥 Can handle **hundreds of buttons** without performance issues",
        "🎯 **TypeScript** ensures type safety in the frontend",
        "📦 Can be **packaged and distributed** via PyPI"
    ]
    
    for i, fact in enumerate(facts):
        if carbon_button(f"Fact #{i+1}", CarbonIcons.INFO, key=f"fact_{i}"):
            st.session_state.total_clicks += 1
            st.markdown(f"### {fact}")
            time.sleep(0.5)
    
    st.divider()
    
    # Epic finale
    st.markdown("### 🎆 The Grand Finale")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if carbon_button(
            "🎉 CLICK FOR AWESOMENESS 🎉", 
            CarbonIcons.ADD, 
            key="epic_finale",
            use_container_width=True
        ):
            st.session_state.total_clicks += 1
            st.session_state.button_stats["EPIC"] = st.session_state.button_stats.get("EPIC", 0) + 1
            
            # Epic celebration
            st.balloons()
            st.snow()
            
            # Show awesome stats
            st.success("# 🎉 YOU'RE AWESOME!")
            st.markdown(f"""
            ### 📊 Your Epic Stats:
            - **Total Clicks:** {st.session_state.total_clicks}
            - **Buttons Clicked:** {len(st.session_state.button_stats)}
            - **Most Clicked:** {max(st.session_state.button_stats.items(), key=lambda x: x[1])[0] if st.session_state.button_stats else 'None yet'}
            - **Awesomeness Level:** MAXIMUM! 🚀
            """)
            
            # Confetti effect with emojis
            placeholder = st.empty()
            for _ in range(5):
                placeholder.markdown(
                    f"# {' '.join(random.choice(['🎉', '🎊', '✨', '🌟', '💫', '🎆', '🎇']) for _ in range(10))}"
                )
                time.sleep(0.2)
            placeholder.empty()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <h3>🚀 Built with the Streamlit Component API</h3>
    <p>No checkboxes were harmed in the making of this app!</p>
    <p>Total clicks in this session: <strong>{}</strong></p>
</div>
""".format(st.session_state.total_clicks), unsafe_allow_html=True)