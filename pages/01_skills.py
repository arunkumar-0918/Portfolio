import streamlit as st


# Set page title and layout

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

st.title("💼 My Skills")

Cloud_skills = {
    "Azure": 80,
    "Azure Synapse": 70,
    "Azure Databricks": 70,
    "Azure Devops": 70,
    "AWS Glue": 70,
    "Terraform": 70,
    "AWS code pipeline": 70,
    "ECS": 70,
    "EKR": 70,
    "Docker": 65,
    "Git": 75,
    "AWS": 70
}
PowerPlatform_skills = {
    "PowerApps": 70,
    "PowerAutomate": 70,
}
dataVisualization_skills = {
    "Power BI": 70,
    "Grafana": 70,
    "QuickSight": 70,
    "Tableau": 70,
    "Plotly": 70,

}
Database_Skills = {
    "Postgres": 70,
    "MongoDB": 70,
    "MySQL": 70,
    "Cassandra": 70,
}

# Skill data
skills = {
    "Python": 90,
    "Apache Flink": 80,
    "Kafka": 85,
    "Airflow": 70,
    "Azure Data Factory": 75,
    "Apache Spark": 70
}
Cloud_skills_logos={
    "Azure": "https://raw.githubusercontent.com/devicons/devicon/master/icons/azure/azure-original.svg",
    "AWS": "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
    "Git": "https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg",
    "Docker": "https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg",
    "Azure Synapse": "https://www.freelogovectors.net/wp-content/uploads/2022/03/azure_synapse_analytics_logo_freelogovectors.net_.png", 
    "Azure Databricks": "https://images.seeklogo.com/logo-png/61/1/databricks-icon-logo-png_seeklogo-611588.png",
    "Azure Devops": "https://1000logos.net/wp-content/uploads/2024/08/Azure-DevOps-Logo.png",
    "AWS Glue": "https://www.cloudmantra.net/wp-content/uploads/2018/04/AWS_GLue__1_400x260.png",
    "AWS code pipeline": "https://symbols.getvecta.com/stencil_12/3_aws-codepipeline.670ed60e36.svg",
    "ECS": "https://symbols.getvecta.com/stencil_9/14_amazon-ecs.c923666086.svg",
    "EKR": "https://cdn.prod.website-files.com/5f05d5858fab461d0d08eaeb/634ff70e43a9f038e0092fc8_eks_light.svg",  
    "Terraform": "https://images.seeklogo.com/logo-png/34/1/terraform-logo-png_seeklogo-340983.png",

}
PowerPlatform_skills_logos={
    "PowerApps":"https://img.icons8.com/?size=100&id=jXuZmZPUKCPS&format=png&color=000000",
    "PowerAutomate": "https://img.icons8.com/?size=100&id=kTTt25v6Drpd&format=png&color=000000",
}
dataVisualization_skills_logos={
    "Power BI": "https://img.icons8.com/?size=100&id=qYfwpsRXEcpc&format=png&color=000000",
    "Grafana": "https://images.seeklogo.com/logo-png/33/1/grafana-logo-png_seeklogo-336503.png",
    "QuickSight": "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*KL4vQyb9MEI9y2eyb4WEGQ.png",
    "Tableau": "https://logos-world.net/wp-content/uploads/2021/10/Tableau-Logo.png",
    "Plotly": "https://studyopedia.com/wp-content/uploads/2023/07/Plotly-Python-Library.jpg",
}
Database_Skills_logos={
    "Postgres": "https://upload.wikimedia.org/wikipedia/commons/2/29/Postgresql_elephant.svg",
    "MongoDB": "https://cdn.worldvectorlogo.com/logos/mongodb-icon-2.svg",
    "MySQL": "https://cdn.freebiesupply.com/logos/large/2x/mysql-5-logo-png-transparent.png",
    "Cassandra": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/cassandra/cassandra-original.svg",   

}
# Skill logos (local or URL)
skill_logos = {
    "Python": "https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg",
    "Apache Flink": "https://flink.apache.org/img/logo/png/200/flink_squirrel_200_color.png",
    "Kafka": "https://upload.wikimedia.org/wikipedia/commons/0/01/Apache_Kafka_logo.svg",
    "Airflow":"https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/apacheairflow/apacheairflow-original.svg",
    "Azure Data Factory": "https://logowik.com/content/uploads/images/azure-data-factory2539.jpg",
    "Azure Databricks": "https://www.element61.be/sites/default/files/img_competences/databricks_icon.png",
    "Apache Spark": "https://spark.apache.org/images/spark-logo-back.png"
        
}

st.markdown("### Cloud Skills")

cols = st.columns(3)
for i, (skill, percent) in enumerate(Cloud_skills.items()):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style="background-color: white; width:100px; height:100px; display: flex; align-items: center; justify-content: center; border-radius: 10px; box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1); margin-bottom: 8px;">
                <img src="{Cloud_skills_logos[skill]}" style="width:60px; height:60px; object-fit:contain;" />
            </div>
            <p><strong>{skill}</strong></p>
            """,
            unsafe_allow_html=True
        )
st.markdown("---")

st.markdown("### Power Platform Skills")
cols = st.columns(3)
for i, (skill, percent) in enumerate(PowerPlatform_skills.items()):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style="background-color: white; width:100px; height:100px; display: flex; align-items: center; justify-content: center; border-radius: 10px; box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1); margin-bottom: 8px;">
                <img src="{PowerPlatform_skills_logos[skill]}" style="width:60px; height:60px; object-fit:contain;" />
                
            </div>
            <p><strong>{skill}</strong></p>
            """,
            unsafe_allow_html=True
        )


st.markdown("---")

st.markdown("### Data Visualization Skills")
cols = st.columns(3)
for i, (skill, percent) in enumerate(dataVisualization_skills.items()):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style="background-color: white; width:100px; height:100px; display: flex; align-items: center; justify-content: center; border-radius: 10px; box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1); margin-bottom: 8px;">
                <img src="{dataVisualization_skills_logos[skill]}" style="width:60px; height:60px; object-fit:contain;" />
            </div>
            <p><strong>{skill}</strong></p>
            """,
            unsafe_allow_html=True
        )
st.markdown("---")

st.markdown("### Database Skills")
cols = st.columns(3)
for i, (skill, percent) in enumerate(Database_Skills.items()):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style="background-color: white; width:100px; height:100px; display: flex; align-items: center; justify-content: center; border-radius: 10px; box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1); margin-bottom: 8px;">
                <img src="{Database_Skills_logos[skill]}" style="width:60px; height:60px; object-fit:contain;" />
            </div>
            <p><strong>{skill}</strong></p>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

st.markdown("### Other Skills")
cols = st.columns(3)
for i, (skill, percent) in enumerate(skills.items()):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style="background-color: white; width:100px; height:100px; display: flex; align-items: center; justify-content: center; border-radius: 10px; box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1); margin-bottom: 8px;">
                <img src="{skill_logos[skill]}" style="width:60px; height:60px; object-fit:contain;" />
            </div>
            <p><strong>{skill}</strong></p>
            """,
            unsafe_allow_html=True
        )
