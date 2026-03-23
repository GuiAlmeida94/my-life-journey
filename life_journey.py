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
    # List of events - Using Emojis for better LCP performance
    return [
        {"date": "Jan 27, 1994", "headline": "🇧🇷 Born in Santo André, Brazil", "text": "The start of the journey."},
        {"date": "Aug 1998 - Jan 2000", "headline": "🇩🇪 First International Experience", "text": "Move to Germany - Return Home in 2000."},
        {"date": "Mar 2009 - Jun 2011", "headline": "🇩🇪 Second Experience in Germany", "text": "Academic period attending Realschule and Gymnasium."},
        {"date": "Feb 2012 - Dec 2012", "headline": "⚙️ First Job: Engineering Intern", "text": "Rucker do Brasil: Catia V5 design for Peugeot, VW, and Renault."},
        {"date": "Jul 2016 - Oct 2018", "headline": "🍦 Store Manager", "text": "Managed family business dessert shop. Focus on financial control."},
        {"date": "Jan 2017", "headline": "🎓 University Enrollment", "text": "Business Management at FASB."},
        {"date": "Oct 2019 - Oct 2021", "headline": "🌐 T-Systems do Brasil", "text": "Service Delivery Management intern. Working with global teams."},
        {"date": "Mar 2022 - Dec 2022", "headline": "📦 Business Assistant at Zenatur", "text": "Logistics for Samsung promotional materials at BGS."},
        {"date": "Oct 28, 2022", "headline": "🕯️ Personal Loss", "text": "Passing of my mother - A turning point in my life."},
        {"date": "Apr 2023", "headline": "🇮🇹 Transfer to Italy", "text": "Moved to Italy to find opportunities in Europe."},
        {"date": "Aug 2023 - Feb 2024", "headline": "🏎️ Consultant at Micla Engineering", "text": "Supported Italdesign Giugiaro in automotive testing."},
        {"date": "Oct 2023", "headline": "📈 Master in Data Science", "text": "Enrolled at Rome Business School."},
        {"date": "Oct 2024", "headline": "🎓 Master's Graduated", "text": "Finished Master in Data Science (Grade 28/30)."},
        {"date": "May 2025", "headline": "🇵🇹 Dual Citizenship", "text": "Received Portuguese Citizenship - EU Work Authorization."},
        {"date": "Jul 2025 - Dec 2025", "headline": "🛠️ Quality Analyst for BMW", "text": "Coveract/Minibea: Quality analysis for BMW door handles."},
        {"date": "Oct 2025", "headline": "📜 Imperial College Certificate", "text": "Data Analytics professional certificate."},
        {"date": "2026", "headline": "🚀 Starting The New Phase", "text": "Ready for new challenges as a Data Analyst in Europe!"}
    ]

# --- 4. LÓGICA DE RENDERIZAÇÃO ---
st.title("📂 Professional & Personal Timeline")
st.subheader("Guilherme Oyakawa de Almeida | Data & Business Analyst")

events = get_timeline_data()

# Inicializamos a variável antes do loop (Crucial para evitar NameError)
timeline_html = '<div class="v-timeline">'

for event in events:
    timeline_html += f"""
    <div class="v-event">
        <div class="v-marker"></div>
        <div class="v-date">{event['date']}</div>
        <div class="v-content">
            <div class="v-headline">{event['headline']}</div>
            <div class="v-text">{event['text']}</div>
        </div>
    </div>
    """

timeline_html += '</div>'

# Injeção única no Streamlit
st.markdown(timeline_html, unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.header("Key Information")
    st.write("**Name:** Guilherme Oyakawa de Almeida")
    st.write("**Languages:** PT (Native), EN (C1), DE (B1), IT (B2)")
    st.write("**Citizenship:** Brazilian & Portuguese 🇪🇺")
    st.divider()
    st.header("Technical Skills")
    st.write("🐍 **Python** (Pandas, Numpy, Scikit-learn)")
    st.write("🗄️ **SQL** (Queries, Data Modeling)")
    st.write("📊 **BI** (Power BI, Tableau)")
