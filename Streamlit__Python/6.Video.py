import streamlit as st

st.title(":blue[Enter your files]",anchor=False)  # Add a title
st.divider()  # Add a horizontal line


video_file=st.file_uploader("Upload your video file", # Add a file uploader for video files
                       type=["mp4","avi","mkv"],
                       accept_multiple_files=False)

button=st.button("Play Video")  # Add a button to play the video

if button:
   if video_file:
    st.video(video_file)
    st.success("Video is uploaded!")
   else:
     st.error("Please upload a video file to play.")