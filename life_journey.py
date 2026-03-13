import streamlit as st
from streamlit_timeline import timeline

# Page setup for a professional look
st.set_page_config(
    page_title="Guilherme Oyakawa - Professional Journey", 
    page_icon="📊", 
    layout="wide"
)

st.title("📂 Professional & Personal Timeline")
st.subheader("Guilherme Oyakawa de Almeida | Data & Business Analyst")

# Data structure containing your life events
# Comments in English to maintain the coding standard
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
                "text": "Move to Germany - A multicultural childhood beginning."
            }
        },
        {{
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
                "text": "<b>Rucker do Brasil:</b> Developed technical drawing skills using Catia V5 for major clients like Peugeot, Volkswagen, and Renault."
            }
        },
        {
            "start_date": {"year": "2016", "month": "7"},
            "text": {
                "headline": "🍦 Store Manager - Family Business",
                "text": "Managed operations, inventory, and financial control, optimizing cash flow and customer experience."
            }
        },
        {
            "start_date": {"year": "2017", "month": "1"},
            "text": {
                "headline": "🎓 Business Management Degree",
                "text": "Enrolled at Faculdade São Bernardo (FASB) to solidify business foundations."
            }
        },
        {
            "start_date": {"year": "2019", "month": "10"},
            "text": {
                "headline": "🌐 Intern at T-Systems do Brasil",
                "text": "Assisted Service Delivery Managers (SDMs) and conducted daily meetings with global teams in English."
            }
        },
        {
            "start_date": {"year": "2022", "month": "3"},
            "text": {
                "headline": "📦 Business Assistant at Zenatur",
                "text": "Coordinated logistics for Samsung promotional materials at major events like Brasil Game Show (BGS)."
            }
        },
        {
            "start_date": {"year": "2022", "month": "10", "day": "28"},
            "text": {
                "headline": "🕯️ Personal Loss",
                "text": "Passing of my mother. A moment of profound personal transformation and resilience."
            }
        },
        {
            "start_date": {"year": "2023", "month": "4"},
            "text": {
                "headline": "<img src='https://flagcdn.com/w40/it.png' width='25'> Transfer to Italy",
                "text": "Relocated to Italy to explore European professional opportunities."
            }
        },
        {
            "start_date": {"year": "2023", "month": "8"},
            "text": {
                "headline": "🏎️ Consultant at Micla Engineering",
                "text": "Supported <b>Italdesign Giugiaro</b> in automotive durability testing and process improvement."
            }
        },
        {
            "start_date": {"year": "2023", "month": "10"},
            "text": {
                "headline": "📈 Master in Data Science",
                "text": "Enrolled at Rome Business School to transition into advanced data analytics."
            }
        },
        {
            "start_date": {"year": "2024", "month": "10"},
            "text": {
                "headline": "🎓 Master's Degree Completed",
                "text": "Finished Master in Data Science with a high grade of 28/30."
            }
        },
        {
            "start_date": {"year": "2025", "month": "5"},
            "text": {
                "headline": "<img src='https://flagcdn.com/w40/pt.png' width='25'> Portuguese Citizenship",
                "text": "Dual citizenship granted, allowing full work authorization across the EU."
            }
        },
        {
            "start_date": {"year": "2025", "month": "7"},
            "text": {
                "headline": "🛠️ Quality Operator at Coveract",
                "text": "Worked at Minibea Access Solutions for <b>BMW</b>, analyzing performance charts and ensuring quality standards."
            }
        },
        {
            "start_date": {"year": "2025", "month": "10"},
            "text": {
                "headline": "📜 Professional Certificate - Imperial College",
                "text": "Specializing in Data Analytics at Imperial College Business School."
            }
        },
        {
            "start_date": {"year": "2026"},
            "text": {
                "headline": "🚀 The New Phase",
                "text": "Looking forward to new challenges as a Data Analyst in Europe!"
            }
        }
    ]
}

# Render the timeline component
timeline(items, height=700)

# Sidebar for quick facts
with st.sidebar:
    st.image("https://img.icons8.com/clouds/100/data-configuration.png")
    st.header("Key Information")
    st.write("**Full Name:** Guilherme Oyakawa de Almeida")
    st.write("**Languages:** Portuguese, English, German, italian")
    st.write("**Citzenship:** Brazilian & Portuguese")
    st.write("**Top Skills:** Python, SQL, Power BI, Tableau, Data Science")
