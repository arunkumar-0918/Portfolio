import streamlit as st
from PIL import Image
from pathlib import Path
from streamlit_navigation_bar import st_navbar
current_dir = Path(__file__).parent.parent if "__file__" in locals() else Path.cwd()
print(current_dir)
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "arun_circle.png"
image_pic = current_dir / "image" / "creative-thinking.png"
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
# --- GENERAL SETTINGS ---
PAGE_TITLE = "My App"
PAGE_ICON = "📊"
NAME = "Arunkumar A"
DESCRIPTION = "Senior Data Analyst, assisting enterprises by supporting data-driven decision-making."
EMAIL = "arunrmdeee@gmail.com"
import pages as pg
pages = {
    "home": "🏠 Home",
    "skills": "🛠️ Skills",
    "project": "📁 Projects",
    "contact": "📞 Contact"
}
styles = {
    "nav": {
        "background": "linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6))",
        "display": "flex",
        "justify-content": "center",
        "align-items": "center",  # Vertical centering
        "padding": "0px 0", 
        "position": "fixed",
        "top": "0",
        "width": "100%",
        "z-index": "1000",
        "box-sizing": "border-box",
        "gap": "0",  # Remove gaps between items
        "margin": "0"  # Remove default margins
    },
    "span": {
        "padding": "10px 20px",
        "border-radius": "20px",
        "background-color": "rgba(255, 255, 255, 0.1)",
        "margin": "0",  # Remove horizontal margins
        "transition": "all 0.3s ease",
        "display": "inline-flex",
        "align-items": "center",
        "height": "40px",
        "box-sizing": "border-box",
        "cursor": "pointer"
    },
    "active": {
        "background-color": "white",
        "color": "black",
        "font-weight": "bold",
        "padding": "10px 20px",
        "border-radius": "20px",
        "margin": "0",  # Remove horizontal margins
        "display": "inline-flex",
        "align-items": "center",
        "height": "40px",
        "box-sizing": "border-box",
        "cursor": "pointer"
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}
pages = {
    "home": "🏠 Home",
    "skills": "🛠️ Skills",
    "project": "📁 Projects",
    "contact": "📞 Contact"
}

# Show navbar using the values (the user-friendly labels)
page_label = st_navbar(
    list(pages.values()),
    styles=styles,
    options=options,
)

# Find the key (like "home") corresponding to the selected label
page_key = next(key for key, value in pages.items() if value == page_label)

functions = {
    "home": pg.showhome,
    "skills": pg.skills,
    "project": pg.showproject,
    "contact": pg.contact,
}

go_to = functions.get(page_key)
if go_to:
    go_to()

