import streamlit as st

# Page setup
st.set_page_config(
    page_title="Guilherme Oyakawa - Life Journey", 
    page_icon="📊", 
    layout="wide"
)

# Infallible CSS for Vertical Timeline with smooth entrance
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .v-timeline {
        border-left: 3px solid #007bff;
        margin-left: 50px;
        padding-left: 30px;
        position: relative;
        padding-top: 10px;
    }
    .v-event {
        margin-bottom: 40px;
        position: relative;
        animation: fadeInUp 0.8s ease-out forwards;
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
        font-size: 1em;
        margin-bottom: 5px;
    }
    .v-content {
        background: #ffffff;
        padding: 18px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        border-left: 5px solid #007bff;
    }
    .v-headline {
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .v-text {
        font-size: 0.95em;
        color: #444;
        line-height: 1.4;
    }
    </style>
    """, unsafe_allow_html=True)

# Main Title
st.title("📂 Professional & Personal Timeline")
st.subheader("Guilherme Oyakawa de Almeida | Data & Business Analyst")

# Data structure
events = [
    {"date": "Jan 27, 1994", "headline": "<img src='https://flagcdn.com/w40/br.png' width='25'> Born in Santo André, Brazil", "text": "The start of the journey - Star of the Journey."},
    {"date": "Aug 1998 - Jan 2000", "headline": "<img src='https://flagcdn.com/w40/de.png' width='25'> First International Experience", "text": "Move to Germany - Return Home in 2000."},
    {"date": "Mar 2009 - Jun 2011", "headline": "<img src='https://flagcdn.com/w40/de.png' width='25'> Second Experience in Germany", "text": "Academic period attending Realschule and Gymnasium."},
    {"date": "Feb 2012", "headline": "⚙️ First Job: Engineering Intern", "text": "Rucker do Brasil: Catia V5 design for Peugeot, Volkswagen, and Renault."},
    {"date": "Jul 2016", "headline": "🍦 Store Manager", "text": "Managed family business dessert shop. Focus on financial control."},
    {"date": "Jan 2017", "headline": "🎓 University Enrollment", "text": "Business Management at FASB."},
    {"date": "Oct 2019", "headline": "🌐 T-Systems do Brasil", "text": "Service Delivery Management intern. Working with global teams in English."},
    {"date": "Mar 2022", "headline": "📦 Business Assistant at Zenatur", "text": "Logistics for Samsung promotional materials at BGS."},
    {"date": "Oct 28, 2022", "headline": "🕯️ Personal Loss", "text": "Passing of my mother - A turning point in my life."},
    {"date": "Apr 2023", "headline": "<img src='https://flagcdn.com/w40/it.png' width='25'> Transfer to Italy", "text": "Moved to Italy to find opportunities in Europe."},
    {"date": "Aug 2023", "headline": "🏎️ Consultant at Micla Engineering", "text": "Supported Italdesign Giugiaro in automotive testing."},
    {"date": "Oct 2023", "headline": "📈 Master in Data Science", "text": "Enrolled at Rome Business School."},
    {"date": "Oct 2024", "headline": "🎓 Master's Graduated", "text": "Finished Master in Data Science (Grade 28/30)."},
    {"date": "May 2025", "headline": "<img src='https://flagcdn.com/w40/pt.png' width='25'> Dual Citizenship", "text": "Received Portuguese Citizenship - EU Work Authorization."},
    {"date": "Jul 2025", "headline": "🛠️ Quality Operator for BMW", "text": "Coveract/Minibea: Quality analysis for BMW door handles."},
    {"date": "Oct 2025", "headline": "📜 Imperial College Certificate", "text": "Data Analytics professional certificate."},
    {"date": "2026", "headline": "🚀 Starting The New Phase", "text": "Ready for new challenges as a Data Analyst in Europe!"}
]

# Rendering
st.markdown('<div class="v-timeline">', unsafe_allow_html=True)
for event in events:
    st.markdown(f"""
    <div class="v-event">
        <div class="v-marker"></div>
        <div class="v-date">{event['date']}</div>
        <div class="v-content">
            <div class="v-headline">{event['headline']}</div>
            <div class="v-text">{event['text']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("Key Information")
    st.write("**Name:** Guilherme Oyakawa de Almeida")
    st.write("**Languages:** Portuguese, English, German, Italian")
    st.write("**Citizenship:** Brazilian & Portuguese 🇪🇺")
    st.divider()
    st.header("Technical Skills")
    st.write("🐍 **Python** (Pandas, Numpy, Matplotlib, Seaborn, Sci-kit learn)")
    st.write("🗄️ **SQL** (Queries, Data Modeling)")
    st.write("📊 **Business Intelligence** (Power BI, Tableau)")
