import streamlit as st
from send_email import send_email

st.header("Contact Me")
st.info("My email: mykolakorbut@icloud.com")

with st.form(key="email_from"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Email from portfolio app

From: {user_email}
{raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
