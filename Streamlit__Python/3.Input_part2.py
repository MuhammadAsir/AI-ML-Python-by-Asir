import streamlit as st

st.title(":blue[Enter your information]",anchor=False)  # Add a title
st.divider()  # Add a horizontal line

name=st.text_input("Enter your name",placeholder="Type your name...")  # Add a text input for the name

st.write("Your name is:", name)  # Display the entered name
st.divider() 

age=st.number_input("Enter Your age",value=None,placeholder="Type your age...")  # Add a number input for the age

st.write("Your age is:", age)
st.divider()

pro=st.selectbox("Enter your profession",
                 ("Student","Teacher","Engineer","Doctor","Other"),
                 index=None,accept_new_options=True)  # Add a select box for profession

st.write("Profession:",pro)