import streamlit as st
from pages import home, skills, project, contact

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "home"

# Set page config
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for fixed navbar
st.markdown("""
<style>
    .fixed-nav {
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 999;
        display: flex;
        gap: 8px;
        background-color: rgba(255,255,255,0.9);
        padding: 8px;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .navbar-spacer {
        height: 60px;
    }
</style>
""", unsafe_allow_html=True)

# Create a container for the fixed navbar
nav_cols = st.columns([5,1,1,1,1])
with nav_cols[0]:
    st.write("")  # Empty space to push buttons right
with nav_cols[1]:
    if st.button("Home"):
        st.session_state.page = "home"
with nav_cols[2]:
    if st.button("Skills"):
        st.session_state.page = "skills"
with nav_cols[3]:
    if st.button("Projects"):
        st.session_state.page = "project"
with nav_cols[4]:
    if st.button("Contact"):
        st.session_state.page = "contact"

# Add spacer
st.markdown("<div class='navbar-spacer'></div>", unsafe_allow_html=True)

# Show the appropriate page
if st.session_state.page == "home":
    home.show()
elif st.session_state.page == "skills":
    skills.show()
elif st.session_state.page == "project":
    project.show()
elif st.session_state.page == "contact":
    contact.show()