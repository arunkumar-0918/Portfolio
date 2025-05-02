import streamlit as st
import pandas as pd
import datetime

# Set the file path for CSV
csv_file = 'datagram.csv'

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
df = pd.read_csv(csv_file)
st.dataframe(df.style.hide(axis="index"))
