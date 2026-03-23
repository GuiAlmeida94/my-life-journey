import streamlit as st

# --- 1. CONFIGURAÇÃO DA PÁGINA (Imediata) ---
st.set_page_config(
    page_title="Guilherme Oyakawa - Life Journey", 
    page_icon="📊", 
    layout="wide"
)

# --- 2. CSS DE ALTA PERFORMANCE ---
# Removi animações complexas que causam Layout Shift (CLS)
st.markdown("""
    <style>
    /* Reset de margens para carregamento mais rápido */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .v-timeline {
        border-left: 4px solid #007bff;
        margin-left: 30px;
        padding-left: 20px;
        position: relative;
    }

    .v-event {
        margin-bottom: 25px;
        position: relative;
        /* Animação ultra simples que não afeta o CLS */
        animation: fadeIn 0.5s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .v-marker {
        position: absolute;
        left: -32px;
        top: 5px;
        width: 16px;
        height: 16px;
        border-radius: 50%;
        background-color: #007bff;
        border: 3px solid white;
    }

    .v-date {
        font-weight: bold;
        color: #007bff;
        font-size: 0.9em;
        margin-bottom: 2px;
    }

    .v-content {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #007bff;
        /* Evita que o card mude de tamanho durante o load */
        min-height: 80px;
    }

    .v-headline {
        font-size: 1.1em;
        font-weight: bold;
        color: #111;
    }
    .v-text { color: #555; font-size: 0.9em; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DADOS COM CACHE ---
@st.cache_data
def get_events():
    return [
        {"date": "Jan 27, 1994", "headline": "🇧🇷 Born in Brazil", "text": "The start of the journey."},
        {"date": "1998 - 2011", "headline": "🇩🇪 Germany Experience", "text": "Academic period and international living."},
        {"date": "2012", "headline": "⚙️ Engineering Intern", "text": "Rucker do Brasil: Catia V5 design."},
        {"date": "2016 - 2018", "headline": "🍦 Store Manager", "text": "Financial control and management."},
        {"date": "2019 - 2021", "headline": "🌐 T-Systems do Brasil", "text": "Service Delivery Management."},
        {"date": "2022", "headline": "📦 Zenatur", "text": "Logistics for Samsung/BGS."},
        {"date": "2023", "headline": "🇮🇹 Move to Italy", "text": "Relocation for European opportunities."},
        {"date": "2023 - 2024", "headline": "🏎️ Micla Engineering", "text": "Automotive testing consultant."},
        {"date": "2024", "headline": "🎓 Master in Data Science", "text": "Graduated from Rome Business School (28/30)."},
        {"date": "2025", "headline": "🇵🇹 Dual Citizenship", "text": "Portuguese Citizenship obtained."},
        {"date": "2025", "headline": "🛠️ BMW Quality Analyst", "text": "Quality analysis for BMW door handles."},
        {"date": "2026", "headline": "🚀 Data Analyst", "text": "Ready for new challenges in Europe!"}
    ]

# --- 4. RENDERIZAÇÃO ---
st.title("📂 Professional Timeline")
st.subheader("Guilherme Oyakawa | Data & Business Analyst")

events = get_events()

# Construção em bloco único para evitar múltiplas chamadas de markdown
timeline_html = '<div class="v-timeline">'
for e in events:
    timeline_html += f"""
    <div class="v-event">
        <div class="v-marker"></div>
        <div class="v-date">{e['date']}</div>
        <div class="v-content">
            <div class="v-headline">{e['headline']}</div>
            <div class="v-text">{e['text']}</div>
        </div>
    </div>"""
timeline_html += '</div>'

st.markdown(timeline_html, unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.header("Key Info")
    st.info("🇧🇷 Brazilian | 🇵🇹 Portuguese")
    st.write("**Languages:** PT, EN, DE, IT")
    st.divider()
    st.header("Skills")
    st.code("Python, SQL, Power BI, Tableau", language='text')
