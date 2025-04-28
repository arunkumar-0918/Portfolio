import streamlit as st
st.markdown(
    """
    <style>
        div[data-testid="collapsedControl"] {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Example Project Entries
project_list = [
    {
        "title": "Sales Dashboard",
        "description": "Developed a real-time sales dashboard using Power BI, Python, and SQL for tracking KPIs across regions.",
        "tech_stack": "Power BI, Python, SQL"
    },
    {
        "title": "Customer Churn Prediction",
        "description": "Built a machine learning model to predict customer churn with 85% accuracy using scikit-learn and Pandas.",
        "tech_stack": "Python, scikit-learn, Pandas"
    },
    {
        "title": "Spotify Data Analytics",
        "description": "Created a data pipeline to extract and analyze Spotify listening habits, visualized insights in Power BI.",
        "tech_stack": "Python, Power BI, Spotify API"
    }
]

for project in project_list:
    st.markdown(f"""
    ### {project['title']}
    🛠️ {project['tech_stack']}  
    {project['description']}
    """)
    st.write('\n')  # space between projects

