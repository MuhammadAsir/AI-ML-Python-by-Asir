import streamlit as st

st.title(":blue[Enter your files]",anchor=False)  # Add a title
st.divider()  # Add a horizontal line

pic=st.file_uploader("Enter your image",
                 type=["jpg","jpeg","png"],accept_multiple_files=True)


if pic:
    col=st.columns(len(pic))
    for i,j in enumerate(pic): 
#i and j are index and value of pic list,enumerate is used to get index and value of list at the same time
        with col[i]:  #to display images in columns
            st.image(j)


print(type(pic))

st.image("https://cdn.pixabay.com/photo/2014/02/27/16/10/flowers-276014_1280.jpg")# Display an image from a URL
st.image("image/4k-lamborghini-gallardo-xkrze3st3fqf52y2.jpg") # Display an image from storage