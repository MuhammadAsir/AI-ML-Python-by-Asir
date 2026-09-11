import streamlit as st

st.title(":blue[Enter your information]",anchor=False)  # Add a title
st.divider()  # Add a horizontal line

name=st.text_input("Enter your name",placeholder="Type your name...")  # Add a text input for the name

st.write("Your name is:", name)  # Display the entered name
st.divider() 

age=st.number_input("Enter Your age",value=None,placeholder="Type your age...")  # Add a number input for the age

st.write("Your age is:", age)
st.divider()

password=st.text_input("Enter your password",type="password")  # Add a text input for the name

button=st.button("Confirm",type="primary")  # Add a submit button

if button:
    st.write(f"Your name is {name} and age is {age}")
else:
    st.write("Please click the confirm button to submit your information.")