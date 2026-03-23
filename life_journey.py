import streamlit as st

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Guilherme Oyakawa - Life Journey", 
    page_icon="📊", 
    layout="wide"
)

# --- 2. ESTILOS CSS (OTIMIZADOS PARA PERFORMANCE) ---
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .v-timeline {
        border-left: 3px solid #007bff;
        margin-left: 50px;
        padding-left: 30px;
        position: relative;
    }

    @keyframes reveal {
        from { opacity: 0; transform: translateY(30px) scale(0.95); }
        to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .v-event {
        margin-bottom: 40px;
        position: relative;
        view-timeline-name: --item;
        view-timeline-axis: block;
        animation: reveal both;
        animation-timeline: --item;
        animation-range: entry 5% cover 25%;
    }

    .v-marker {
        position: absolute;
        left: -41px;
        top: 0;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: #007bff;
        border: 4px solid white;
        box-shadow: 0 0 8px rgba(0,123,255,0.4);
    }

    .v-date {
        font-weight: bold;
        color: #007bff;
        font-size: 1.1em;
        margin-bottom: 5px;
    }

    .v-content {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-left: 6px solid #007bff;
    }

    .v-headline {
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: 5px;
        color: #111;
    }
    .v-text { color: #444; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DADOS (COM CACHE PARA VELOCIDADE) ---
@st.cache_data
def get_timeline_data():
