import streamlit as st

# Set page configuration
st.set_page_config(page_title="GenAI Tool", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main-title { 
            text-align: center; 
            font-size: 40px; 
            font-weight: bold; 
        }
        .sub-title { 
            text-align: center; 
            font-size: 18px; 
            color: gray; 
        }
        .coming-soon { 
            text-align: center; 
            font-size: 22px; 
            font-weight: bold; 
            margin-top: 20px; 
            color: #ff4b4b;
        }
        .stSidebar { 
            background-color: #1e1e1e !important; 
            padding: 20px;
        }
        .sidebar-item {
            font-size: 16px;
            font-weight: bold;
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("**Choose a feature from the sidebar:**")
st.sidebar.markdown("📄 **LinkedIn Post**")
st.sidebar.markdown("🖼 **Profile Picture Generation**")
st.sidebar.markdown("🎨 **Visuals Generation**")
st.sidebar.markdown("📜 **Cheat Sheets**")
st.sidebar.markdown("📊 **Excel Dashboards**")
st.sidebar.markdown("🔗 **API**")

# Main Content
st.markdown('<div class="main-title">GenAI Tool App 🚀</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Your AI-powered tool for LinkedIn posts, profile pictures, visuals, cheat sheets, and dashboards!</div>', unsafe_allow_html=True)
st.markdown('<div class="coming-soon">🚀  Multipage navigation and exciting features!</div>', unsafe_allow_html=True)
