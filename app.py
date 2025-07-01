import streamlit as st
from chatbot import ask_bot

st.set_page_config(page_title="AI Health Chatbot", page_icon="🩺")
st.title("🤖 AI Health Chatbot")
st.markdown("Ask any health-related question and get suggestions.")

user_input = st.text_input("👤 Your question (e.g., I have a headache and fever):")

if st.button("Ask"):
    if user_input:
        with st.spinner("Thinking..."):
            response = ask_bot(user_input)
            st.success(response)
    else:
        st.warning("Please enter a question first.")
