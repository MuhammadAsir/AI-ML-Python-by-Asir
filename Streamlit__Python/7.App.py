from google import genai          # Import Gemini AI library
import os                         # For accessing environment variables
from dotenv import load_dotenv    # To load variables from .env file
import streamlit as st            # For building a simple web app


load_dotenv()  # Load variables from .env file into the system

# Get API key from environment variables
API_KEY = os.environ.get("GEMINI_API_KEY")

# Create a Gemini client using the API key
client = genai.Client(api_key=API_KEY)

# Send a prompt to the AI model and get response
response = client.models.generate_content(
    model="gemini-3-flash-preview",      # Fast Gemini model
    contents="Tell me a joke about programming."  # Input prompt
)

# Print response in terminal
print(response.text)

# Show response in Streamlit web app
st.markdown(response.text)

"""How the Whole Flow Works-
1.Load environment variables
2.Get API key securely
3.Create a Gemini client
4.Send a prompt to the AI
5.Receive response
Show it in:
Console (print)
Web app (streamlit)"""

"""
load_dotenv() → Load secret key from .env
os.environ.get() → Read the key
genai.Client() → Connect to AI
generate_content() → Ask question
response.text → Get answer
print() → Show in terminal
st.markdown() → Show in web app
"""