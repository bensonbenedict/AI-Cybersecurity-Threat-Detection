import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Space+Grotesk:wght@400;700&display=swap');

        /* Global Typography and Background */
        html, body, [class*="css"]  {
            font-family: 'Outfit', sans-serif;
            color: #e2e8f0;
        }

        h1, h2, h3, .st-emotion-cache-10trblm {
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 700;
            background: linear-gradient(135deg, #10b981, #6366f1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(99, 102, 241, 0.2);
        }

        /* Animated Dark Cosmic Background */
        .stApp {
            background: radial-gradient(circle at 10% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 40%),
                        radial-gradient(circle at 90% 80%, rgba(16, 185, 129, 0.15) 0%, transparent 40%),
                        linear-gradient(135deg, #09070f 0%, #030206 100%);
            background-size: 200% 200%;
            animation: spaceBG 25s ease infinite alternate;
        }

        @keyframes spaceBG {
            0% { background-position: 0% 0%; }
            50% { background-position: 100% 100%; }
            100% { background-position: 0% 100%; }
        }

        /* Card Container (Tac-Card) */
        .tac-card {
            background: rgba(15, 11, 25, 0.65) !important;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(99, 102, 241, 0.15);
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .tac-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
            box-shadow: 0 10px 40px 0 rgba(99, 102, 241, 0.15);
            transform: translateY(-2px);
        }

        /* Glowing Tactical Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #10b981 0%, #6366f1 100%) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.75rem 2rem !important;
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 700 !important;
            letter-spacing: 0.5px !important;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
            box-shadow: 0 0 15px rgba(99, 102, 241, 0.4) !important;
        }
        
        .stButton > button:hover {
            transform: scale(1.02) !important;
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.6) !important;
            background: linear-gradient(135deg, #6366f1 0%, #10b981 100%) !important;
            border-color: transparent !important;
            color: #ffffff !important;
        }

        /* Input Controls Glassmorphism */
        div[data-baseweb="input"] > div {
            background-color: rgba(15, 11, 25, 0.5) !important;
            border: 1px solid rgba(99, 102, 241, 0.2) !important;
            border-radius: 12px !important;
            color: #ffffff !important;
            transition: all 0.3s ease !important;
        }

        div[data-baseweb="input"] > div:focus-within {
            border-color: #10b981 !important;
            box-shadow: 0 0 12px rgba(16, 185, 129, 0.4) !important;
        }

        div[data-baseweb="input"] input {
            color: #10b981 !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
        }

        /* Custom Streamlit Tabs Styling */
        button[data-baseweb="tab"] {
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 700 !important;
            font-size: 1.1rem !important;
            color: #94a3b8 !important;
            border-bottom: 2px solid transparent !important;
            transition: all 0.3s ease !important;
            background: transparent !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
            color: #10b981 !important;
            border-bottom: 2px solid #10b981 !important;
            text-shadow: 0 0 10px rgba(16, 185, 129, 0.3) !important;
        }

        /* Hide Sidebar completely if needed */
        [data-testid="stSidebar"] {
            background-color: #030206 !important;
            border-right: 1px solid rgba(99, 102, 241, 0.1) !important;
        }

        /* Success and Error Alerts */
        .st-emotion-cache-1v0mbdj {
            background-color: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 12px;
            backdrop-filter: blur(8px);
        }

        .st-emotion-cache-12w0qpk {
            background-color: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
            border-radius: 12px;
            backdrop-filter: blur(8px);
        }

        </style>
    """, unsafe_allow_html=True)
