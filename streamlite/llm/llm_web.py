"""
creating a web-based chatbot using LLM API (openai python sdk) with streamlit 
Text input fro qs
chat-style message display
openai api integration
converation history 
system prompt
clear converation button
error handling
api key protection

"""
import os
import streamlit as st
from dotenv import load_dotenv
from openai import (
    OpenAI,
    APIConnectionError,
    APIStatusError,
    RateLimitError,
)

load_dotenv()

API_KEY = ""
MODEL = os.getenv("MODEL", "gpt-4.1-mini")


st.set_page_config(page_title="Chatbot with LLM API", page_icon="🤖", layout="wide")

st.title("🤖 AI Chatbot ")
st.caption("A web-based chatbot using LLM API (OpenAI Python SDK) with Streamlit")

if not API_KEY:
    st.error("OPENAI_API_KEY not found in environment variables. Please set it in your .env file.")
    st.stop()

client = OpenAI(api_key=API_KEY)


#define the system prompt
SYSTEM_PROMPT = """
You are a helpful AI assistant and Python teacher.
Explain concepts clearly using beginner-friendly language.
Give practical examples when useful.
If you are unsure about something, say so.

"""


if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Settings")
    st.write(f"Model: {MODEL}")

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.success("Conversation cleared!")
        st.rerun()


#display the conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
#get user input
question = st.chat_input("Ask a question...")


if question:
    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.responses.create(
                    model=MODEL,
                    instructions=SYSTEM_PROMPT,
                    input=st.session_state.messages,
                )

                answer = response.output_text

                st.session_state.messages.append({"role": "assistant", "content": answer})

                st.markdown(answer)

            except RateLimitError:
                st.session_state.messages.pop()
                st.error("Rate limit exceeded. Please try again later.")
            except APIConnectionError:
                st.session_state.messages.pop()
                st.error("Connection error. Please check your internet connection and try again.")
            except APIStatusError as e:
                st.session_state.messages.pop()
                st.error(f"API status error: {e}. Please try again later.")

            except Exception as e:
                st.session_state.messages.pop()
                st.error(f"An unexpected error occurred: {e}. Please try again later.")
