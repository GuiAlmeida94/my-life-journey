import streamlit as st

# 1. Configuração Imediata
st.set_page_config(page_title="Guilherme Oyakawa", layout="wide")

# 2. CSS Estático (Inline para evitar requisições extras)
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {max-width: 1000px; margin: 0 auto;}
    .v-timeline {border-left: 3px solid #007bff; margin-left: 20px; padding-left: 20px;}
    .v-event {margin-bottom: 20px; font-family: sans-serif;}
    .v-content {background: #fdfdfd; padding: 12px; border-radius: 8px; border: 1px solid #eee; border-left: 4px solid #007bff;}
    .v-date {color: #007bff; font-weight: bold; font-size: 0.9rem;}
    .v-headline {font-weight: bold; font-size: 1.1rem; color: #222;}
    .v-text {color: #666; font-size: 0.9rem;}
    </style>
""", unsafe_allow_html=True)

# 3. Dados Hardcoded (Sem funções para máxima velocidade)
events = [
    {"d": "1994-2011", "h": "🇧🇷 Born & 🇩🇪 Germany", "t": "Early life and international background."},
    {"d": "2012-2021", "h": "⚙️ Engineering & T-Systems", "t": "Technical internships and Service Delivery."},
    {"d": "2022-2024", "h": "🇮🇹 Italy & Master's", "t": "Master in Data Science (28/30) at Rome Business School."},
    {"d": "2025-2026", "h": "🇵🇹 Quality Analyst & Data Analyst", "t": "Ready for European Data opportunities."}
]

# 4. Renderização Direta
st.title("Guilherme Oyakawa | Portfolio")
st.write("Data & Business Analyst")

html = '<div class="v-timeline">'
for e in events:
    html += f'<div class="v-event"><div class="v-date">{e["d"]}</div><div class="v-content"><div class="v-headline">{e["h"]}</div><div class="v-text">{e["t"]}</div></div></div>'
html += '</div>'

st.markdown(html, unsafe_allow_html=True)

# 5. Sidebar Minimalista
st.sidebar.markdown("### Contact & Skills")
st.sidebar.code("Python | SQL | BI", language='text')
