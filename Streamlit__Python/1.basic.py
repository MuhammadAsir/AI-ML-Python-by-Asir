"""
Streamlit is a powerful and easy-to-use framework for building interactive web applications
in Python.It allows you to create beautiful and functional apps with minimal code. """

import streamlit as st

st.title("Welcome to Streamlit!")  # Add a title
st.header("Content 1",divider=True)  # Add a header
st.subheader("Content 2")  # Add a subheader

st.write(":world_map: Hello World")  # Add a text input box

st.markdown("Hello **Asir**") # Add markdown text with bold formatting
st.markdown("*How are you*") # Add markdown text with italic formatting
st.markdown(":red[*All good!!!*]") # Add markdown text with red color
st.markdown(":blue-background[*Absolutely!!!*]") # Add markdown text with blue background color
a=100
b=200
st.write(a,b)