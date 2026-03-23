import streamlit as st

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Guilherme Oyakawa - Life Journey", 
    page_icon="📊", 
    layout="wide"
)

# --- 2. DADOS ---
@st.cache_data
def get_timeline_data():
    return [
        {"date": "Jan 27, 1994", "headline": "🇧🇷 Born in Santo André, Brazil", "text": "The start of the journey."},
        {"date": "Aug 1998 - Jan 2000", "headline": "🇩🇪 First International Experience", "text": "Move to Germany - Return Home in 2000."},
        {"date": "Mar 2009 - Jun 2011", "headline": "🇩🇪 Second Experience in Germany", "text": "Academic period attending Realschule and Gymnasium."},
        {"date": "Feb 2012 - Dec 2012", "headline": "⚙️ First Job: Engineering Intern", "text": "Rucker do Brasil: Catia V5 design for Peugeot, VW, and Renault."},
        {"date": "Jul 2016 - Oct 2018", "headline": "🍦 Store Manager", "text": "Managed family business dessert shop."},
        {"date": "Jan 2017", "headline": "🎓 University Enrollment", "text": "Business Management at FASB."},
        {"date": "Oct 2019 - Oct 2021", "headline": "🌐 T-Systems do Brasil", "text": "Service Delivery Management intern."},
        {"date": "Mar 2022 - Dec 2022", "headline": "📦 Business Assistant at Zenatur", "text": "Logistics for Samsung promotional materials."},
        {"date": "Oct 28, 2022", "headline": "🕯️ Personal Loss", "text": "Passing of my mother - A turning point."},
        {"date": "Apr 2023", "headline": "🇮🇹 Transfer to Italy", "text": "Moved to Italy to find opportunities in Europe."},
        {"date": "Aug 2023 - Feb 2024", "headline": "🏎️ Consultant at Micla Engineering", "text": "Supported Italdesign Giugiaro."},
        {"date": "Oct 2023", "headline": "📈 Master in Data Science", "text": "Enrolled at Rome Business School."},
        {"date": "Oct 2024", "headline": "🎓 Master's Graduated", "text": "Finished Master in Data Science (Grade 28/30)."},
        {"date": "May 2025", "headline": "🇵🇹 Dual Citizenship", "text": "Received Portuguese Citizenship - EU Work Authorization."},
        {"date": "Jul 2025 - Dec 2025", "headline": "🛠️ Quality Analyst for BMW", "text": "Quality analysis for BMW door handles."},
        {"date": "Oct 2025", "headline": "📜 Imperial College Certificate", "text": "Data Analytics professional certificate."},
        {"date": "2026", "headline": "🚀 Starting The New Phase", "text": "Ready for new challenges as a Data Analyst!"}
    ]

# --- 3. CONSTRUÇÃO DO CONTEÚDO ---
events = get_timeline_data()

# CSS separado para evitar conflitos de renderização
st.markdown("""
    <style>
    .v-timeline {
        border-left: 3px solid #007bff;
        margin-left: 50px;
        padding-left: 30px;
        position: relative;
    }
    .v-event {
        margin-bottom: 35px;
        position: relative;
    }
    .v-marker {
        position: absolute;
        left: -41px;
        top: 0;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background-color: #007bff;
        border: 4px solid white;
        box-shadow: 0 0 8px rgba(0,123,255,0.3);
    }
    .v-date {
        font-weight: bold;
        color: #007bff;
        font-size: 1.05em;
        margin-bottom: 4px;
    }
    .v-content {
        background: #ffffff;
        padding: 18px;
        border-radius: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
        border-left: 5px solid #007bff;
    }
    .v-headline {
        font-size: 1.25em;
        font-weight: bold;
        margin-bottom: 4px;
        color: #111 !important;
    }
    .v-text { color: #555 !important; font-size: 0.95em; }
    </style>
    """, unsafe_allow_html=True)

st.title("📂 Professional & Personal Timeline")
st.subheader("Guilherme Oyakawa de Almeida | Data & Business Analyst")

# Criamos a string HTML apenas para as divs
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

# INJEÇÃO FINAL - Certifique-se de que o unsafe_allow_html esteja como True
st.write(timeline_html, unsafe_allow_html=True)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.header("Key Information")
    st.write("**Name:** Guilherme Oyakawa de Almeida")
    st.write("**Languages:** PT, EN (C1), DE (B1), IT (B2)")
    st.write("**Citizenship:** Brazilian & Portuguese 🇪🇺")
    st.divider()
    st.header("Technical Skills")
    st.write("🐍 **Python** | 🗄️ **SQL** | 📊 **Power BI & Tableau**")
