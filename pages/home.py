import streamlit as st
from PIL import Image
from pathlib import Path
from pathlib import Path

# Go up from /pages/ to /resume/
current_dir = Path(__file__).parent.parent

# Correct paths from the project root
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "arun_circle.png"
image_pic = current_dir / "image" / "creative-thinking.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "My App"
PAGE_ICON = "📊"
NAME = "Arunkumar A"
DESCRIPTION = "Senior Data Analyst, assisting enterprises by supporting data-driven decision-making."
EMAIL = "arunrmdeee@gmail.com"
PROJECTS = {
"🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320"
}
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)
# --- PAGE CONFIG ---
SOCIAL_MEDIA = {
"LinkedIn": {
    "link": "https://www.linkedin.com/in/arun-kumar-2b2148179/",
    "logo": "https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg"
},
"GitHub": {
    "link": "https://github.com/arunkumar-0918",
    "logo": "https://upload.wikimedia.org/wikipedia/commons/c/c2/GitHub_Invertocat_Logo.svg"
},
"Twitter": {
    "link": "https://x.com/arunrmdeee",
    "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b7/X_logo.jpg"
}
}
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic_path)
def showhome():
    # --- LOAD CSS, PDF, PROFILE PIC ---
    

    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic)

    with col2:
        st.title(NAME)
        st.write('\n')
        st.write(DESCRIPTION)
        st.write('\n')
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
        st.write('\n')
        st.write("📫", EMAIL)
        st.write('\n')
        st.write('\n')
        st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
        cols = st.columns([1, 1, 1])  # Evenly distribute the columns

    # Loop through platforms
    for index, (platform, details) in enumerate(SOCIAL_MEDIA.items()):
        with cols[index]:
            st.markdown(
                f"""
                <div style="
                    background-color: white;
                    width: 40px;
                    height: 40px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 90%;
                    box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
                    margin: 0;
                    padding: 0;
                ">
                    <a href="{details['link']}" target="_blank">
                        <img src="{details['logo']}" alt="{platform}" style="width: 20px; height: 20px; object-fit:contain;" />
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
    # --- SOCIAL LINKS ---


    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write("---")
    st.write("""
    - ✔️ Results-driven Software Engineer with 4+ years of experience specializing in data analytics, automation, and cloud-native solution development. Proven ability to deliver scalable, high-impact solutions that reduce manual effort and drive business insights.
    - ✔️ Automation Specialist: Designed and deployed low-code/no-code tools using Power BI, Power Apps, and Azure Data Factory, automating workflows and saving up to 80% manual effort.
    - ✔️ Cloud & DevOps Practitioner: Proficient in AWS and Azure, with hands-on experience in CI/CD pipelines, Kubernetes, and end-to-end cloud deployment.
    - ✔️ AI Learner & N8N Explorer: Actively building AI-driven automations and intelligent workflows using N8N, Python, and ML frameworks to enhance data-driven processes.
    - ✔️ Business-Focused Engineer: Strong track record of aligning technical solutions with stakeholder needs—developed 10+ dashboards and automation tools improving data accessibility across teams.
    """)

    # --- WORK HISTORY ---
    st.write('\n')
    st.subheader("Work History")
    st.write("---")

    # Job 1
    # Job 1
    st.write('\n')
    st.markdown("&nbsp;", unsafe_allow_html=True)
    st.write("🚧", "**Senior Software Engineer | HCL Technologies Pvt. Ltd.**")
    st.write("05/2024 - Present")
    st.write("""
    - ► Delivered 5+ Power BI dashboards aligned to stakeholder KPIs, reducing manual reporting by 30%  
    - ► Automated workflows using Power Apps, Power Automate, and UIPath, improving team efficiency by 40%  
    - ► Built cross-functional digital solutions using Figma and Power Platform  
    - ► Conducted onboarding sessions and documentation, achieving 90% adoption of BI tools  
    """)

    # Job 2
    st.write('\n')
    st.markdown("&nbsp;", unsafe_allow_html=True)
    st.write("🚧", "**Software Engineer | HCL Technologies Pvt. Ltd.**")
    st.write("05/2022 - 05/2024")
    st.write("""
    - ► Created low-code apps and automated workflows, saving up to 80% manual effort  
    - ► Developed ETL pipelines via Azure Data Factory and Synapse Analytics for centralized reporting  
    - ► Built secure Azure Data Lakes to enhance compliance and data accessibility  
    - ► Improved dashboard availability and pipeline reliability by coordinating with DevOps  
    """)

    # Job 3
    st.write('\n')
    st.markdown("&nbsp;", unsafe_allow_html=True)
    st.write("🚧", "**Software Engineer | HCL Technologies Pvt. Ltd.**")
    st.write("02/2021 - 05/2022")
    st.write("""
    - ► Built 10+ Power BI dashboards for R&D, finance, and sales to support decision-making  
    - ► Automated recurring reports, cutting reporting cycle time by 70%  
    - ► Created Figma UI wireframes for dashboard validation and adoption  
    - ► Designed tailored analytics solutions through stakeholder collaboration  
    """)

    # Job 4
    st.write('\n')
    st.markdown("&nbsp;", unsafe_allow_html=True)
    st.write("🚧", "**Freelance Automation & BI Developer | Remote**")
    st.write("01/2020 - Present")
    st.write("""
    - ► Built automation workflows using N8N, OpenAI, and Python for lead tracking and CRM integrations  
    - ► Developed dashboards and analytics pipelines using Power BI and AWS stack  
    - ► Designed AI-based bots and workflow engines for small businesses  
    - ► Consulted across domains to deliver scalable, automated data solutions  
    """)



    # Social media links


    st.write('\n')
    st.write('\n')

    # Create columns
    # Adjust column widths and container sizes
    # Add CSS to reduce column spacing
    st.markdown("""
    <style>
        /* Reduce space between columns */
        [data-testid=column] {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
        
        /* Remove vertical gap in columns */
        [data-testid=stVerticalBlock] {
            gap: 0rem !important;
        }
        
        /* Optional: Make the icons closer together */
        .social-icon-container {
            margin: 0 -0.25rem !important;
        }
    </style>
    """, unsafe_allow_html=True)
