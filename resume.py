import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
from pathlib import Path
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
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


# --- LOAD CSS, PDF, PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic_path)

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
- ✔️ 7 Years experience extracting actionable insights from data
- ✔️ Strong hands-on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team player and displaying strong sense of initiative on tasks
""")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# Job 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write("""
- ► Used PowerBI and SQL to redefine and track KPIs surrounding marketing initiatives, boosting conversion rate by 38%
- ► Led a team of 4 analysts to implement A/B tests resulting in 15% more leads
- ► Redesigned data model to improve predictions by 12%
""")

# Job 2
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write("""
- ► Built data models to generate insights, boosting sales efforts by 12%
- ► Modeled renewal likelihood leading to $300K YoY revenue increase
- ► Modeled info to drive auto policy pricing
""")

# Job 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write("""
- ► Devised KPIs across website with cross-functional teams, increasing organic traffic by 120%
- ► Improved customer communication processes by 18%
- ► Oversaw return data handling process
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