import streamlit as st
import pandas as pd
import datetime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
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

engine = create_engine('sqlite:///datastorage.db')  # This creates a local SQLite file

# Create table if it doesn't exist
metadata = MetaData()

form_data = Table(
    'form_data', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('email', String),
    Column('message', String),
    Column('date', String),
)

metadata.create_all(engine)

st.title("Please free to connect with me")

# Streamlit Form
my_form = st.form(key="form1")
name = my_form.text_input("Name")
email = my_form.text_input("Email")
message = my_form.text_area("please leave your message")
submit_button = my_form.form_submit_button(label="Submit")

if submit_button:
    # Insert into database
    with engine.begin() as conn:  # <-- use engine.begin()
        insert_stmt = form_data.insert().values(
            name=name,
            email=email,
            message=message,
            date=str(datetime.datetime.now())
        )
        conn.execute(insert_stmt)

    st.success("Form submitted and data saved to database!")
    st.snow()

# Show latest data
#df = pd.read_sql_table('form_data', con=engine)
#st.dataframe(df.style.hide(axis="index"))
