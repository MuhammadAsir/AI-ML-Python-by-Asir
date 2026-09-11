import streamlit as st

st.title(":blue[Enter your files]",anchor=False)  # Add a title
st.divider()  # Add a horizontal line

st.audio("audio/02-Nitol paye-Fuad.mp3",loop=False)  
# Add an audio player with a specified audio file and loop option
st.divider()

audio_file=st.file_uploader("Upload your audio file", # Add a file uploader for audio files
                       type=["mp3","wav","ogg"],
                       accept_multiple_files=False)

if audio_file:
    st.audio(audio_file)


