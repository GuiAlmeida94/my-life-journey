import streamlit as st
from streamlit_timeline import timeline

# Page setup
st.set_page_config(
    page_title="Guilherme Oyakawa - Life Journey", 
    page_icon="📊", 
    layout="wide"
)

# Custom CSS to hide the hamburger menu and footer
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

st.title("📂 Professional & Personal Timeline")
st.subheader("Guilherme Oyakawa de Almeida | Data & Business Analyst")

# Data structure
items = {
    "events": [
        {
            "start_date": {"year": "1994", "month": "1", "day": "27"},
            "text": {
                "headline": "<img src='https://flagcdn.com/w40/br.png' width='25'> Born in Santo André, Brazil",
                "text": "The start of the journey - Star of the Journey."
            }
        },
        {
            "start_date": {"year": "1998", "month": "8"},
            "end_date": {"year": "2000", "month": "1"},
            "text": {
                "headline": "<img src='https://flagcdn.com/w40/de.png' width='25'> First International Experience",
                "text": "Move to Germany - Return Home in 2000."
            }
        },
        {
            "start_date": {"year": "2009", "month": "3"},
            "end_date": {"year": "2011", "month": "6"},
            "text": {
                "headline": "<img src='https://flagcdn.com/w40/de.png' width='25'> Second Experience in Germany",
                "text": "Academic period attending Realschule and Gymnasium."
            }
        },
        {
            "start_date": {"year": "2012", "month": "2"},
            "text": {
                "headline": "⚙️ First Job: Engineering Intern",
                "text": "Rucker do Brasil: Catia V5 design for Peugeot, Volkswagen, and Renault."
            }
        },
        {
            "start_date": {"year": "2016", "month": "7"},
            "text": {
                "headline": "🍦 Store Manager",
                "text": "Managed family business dessert shop. Focus on financial control."
            }
        },
        {
            "start_date": {"year": "2017", "month": "1"},
            "text": {
                "headline": "🎓 University Enrollment",
                "text": "Business Management at FASB."
            }
        },
        {
            "start_date": {"year": "2019", "month": "10"},
            "text": {
                "headline": "🌐 T-Systems do Brasil",
                "text": "Service Delivery Management intern. Working with global teams in English."
            }
        },
        {
            "start_date": {"year": "2022", "month": "3"},
            "text": {
                "headline": "📦 Business Assistant at Zenatur",
                "text": "Logistics for Samsung promotional materials at BGS."
            }
        },
        {
            "start_date": {"year": "2022", "month": "10", "day": "28"},
            "text": {
                "headline": "🕯️ Personal Loss",
                "text": "Passing of my mother - A turning point in my life."
            }
        },
        {
            "start_date": {"year": "2023", "month": "4"},
            "text": {
                "headline": "<img src='https://flagcdn.com/w40/it.png' width='25'> Transfer to Italy",
                "text": "Moved to Italy to find opportunities in Europe."
            }
        },
        {
            "start_date": {"year": "2023", "month": "8"},
            "text": {
                "headline": "🏎️ Consultant at Micla Engineering",
                "text": "Supported Italdesign Giugiaro in automotive testing."
            }
        },
        {
            "start_date": {"year": "2023", "month": "10"},
            "text": {
                "headline": "📈 Master in Data Science",
                "text": "Enrolled at Rome Business School."
            }
        },
        {
            "start_date": {"year": "2024", "month": "10"},
            "text": {
                "headline": "🎓 Master's Graduated",
                "text": "Finished Master in Data Science (Grade 28/30)."
            }
        },
        {
            "start_date": {"year": "2025", "month": "5"},
            "text": {
                "headline": "<img src='https://flagcdn.com/w40/pt.png' width='25'> Dual Citizenship",
                "text": "Received Portuguese Citizenship - EU Work Authorization."
            }
        },
        {
            "start_date": {"year": "2025", "month": "7"},
            "text": {
                "headline": "🛠️ Quality Operator for BMW",
                "text": "Coveract/Minibea: Quality analysis for BMW door handles."
            }
        },
        {
            "start_date": {"year": "2025", "month": "10"},
            "text": {
                "headline": "📜 Imperial College Certificate",
                "text": "Data Analytics professional certificate."
            }
        },
        {
            "start_date": {"year": "2026"},
            "text": {
                "headline": "🚀 Starting The New Phase",
                "text": "Ready for new challenges as a Data Analyst in Europe!"
            }
        }
    ]
}

# Rendering
timeline(items, height=700)

# Sidebar with expanded info and skills
with st.sidebar:
    st.header("Key Information")
    st.write("**Name:** Guilherme Oyakawa de Almeida")
    st.write("**Languages:** Portuguese, English, German, Italian")
    st.write("**Citizenship:** Brazilian & Portuguese 🇪🇺")
    
    st.divider()
    
    st.header("Technical Skills")
    st.write("🐍 **Python** (Pandas, Numpy, Matplotlib, Seaborn , Sci-kit learn)")
    st.write("🗄️ **SQL** (Queries, Data Modeling)")
    st.write("📊 **Business Intelligence** (Power BI, Tableau)")
    
    st.divider()
