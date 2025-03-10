from dotenv import load_dotenv
import os 
import streamlit as st  #to create the interface for power application
from PIL import Image
load_dotenv()


api_key=os.getenv("GOOGLE_API_KEY")
st.set_page_config(page_title="Gemini chatbot")
st.header("Gemini LLM application 😂")
st.subheader("This is my Gemini application")
question=st.text_input("write your question",key="question")
uploaded_file=st.file_uploader("choose your file",type=['jpg','jpeg','png'])

imge=""
if uploaded_file is not None:
    imge=Image.open(uploaded_file)
    st.image(imge, caption='Uploaded Image', use_column_width=True)

sumbit=st.button("sumbit")