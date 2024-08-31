import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Mykola Korbut")
    content = """
    Hi, I am Mykola! I am a Python beginner. I started learn python with Python Mega Course by Ardit Sulce.
    This is my portfolio app. 
    """

    st.info(content)