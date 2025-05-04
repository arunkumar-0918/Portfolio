import streamlit as st
import pandas as pd
import datetime
from PIL import Image
from pathlib import Path
# Go up from /pages/ to /resume/
current_dir = Path(__file__).parent.parent

# Correct paths from the project root
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "arun_circle.png"
image_pic = current_dir / "image" / "creative-thinking.png"
# Set the file path for CSV
csv_file = 'datagram.csv'
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
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def contact():
    # Check if CSV file exists; if not, create it with headers
    if not pd.io.common.file_exists(csv_file):
        df = pd.DataFrame(columns=["id", "name", "email", "message", "date"])
        df.to_csv(csv_file, index=False)

    st.title("Please feel free to connect with me")

    # Streamlit Form
    my_form = st.form(key="form1")
    name = my_form.text_input("Name")
    email = my_form.text_input("Email")
    message = my_form.text_area("Please leave your message")
    submit_button = my_form.form_submit_button(label="Submit")

    if submit_button:
        # Generate unique ID for each form submission
        form_id = len(pd.read_csv(csv_file)) + 1
        current_date = str(datetime.datetime.now())
        
        # Prepare data to append
        new_data = {
            "id": form_id,
            "name": name,
            "email": email,
            "message": message,
            "date": current_date
        }
        
        # Append the new data to the CSV file
        new_df = pd.DataFrame([new_data])  # Create a DataFrame for the new data
        df = pd.read_csv(csv_file)  # Read the current CSV data
        df = pd.concat([df, new_df], ignore_index=True)  # Concatenate the new row
        df.to_csv(csv_file, index=False)  # Save it back to the CSV


        st.success("Form submitted and data saved to the CSV file!")
        st.snow()

    # Show latest data from the CSV file

