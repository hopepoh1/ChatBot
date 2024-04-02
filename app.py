# Q&A Chatbot
import os
from openai import Client
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with your API key
client = Client(api_key=os.getenv("OPENAI_API_KEY"))

## Function to load OpenAI model and get responses
def get_openai_response(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": question}],
        max_tokens=50
    )
    return response.choices[0].message.content.strip()

## Initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input_text = st.text_input("Input: ")

submit_button = st.button("Ask the question")

## If ask button is clicked
if submit_button:
    response = get_openai_response(input_text)
    st.subheader("The Response is")
    st.write(response)
