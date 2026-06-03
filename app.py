from dotenv import load_dotenv
from groq import Groq
import streamlit as st
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Page config
st.set_page_config(page_title="Namis - Career Coach", page_icon="💼")
st.title("💼 Namis - Your Career Coach")
st.caption("Ask me anything about job interviews, resumes, and career advice!")

# System prompt
system_prompt = """
You are Namis, a friendly and encouraging career coach chatbot.
Your job is to help people prepare for job interviews, write resumes,
and build confidence in their job search.

Rules:
- Always be warm, positive and supportive
- Give practical, specific advice
- Keep responses concise and easy to read
- If asked about anything unrelated to careers, politely redirect
  back to career topics
"""

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# Display chat history (skip the system message)
for msg in st.session_state.messages:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box at the bottom
if user_input := st.chat_input("Type your message here..."):

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Add to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Get AI response
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Show AI message
    with st.chat_message("assistant"):
        st.markdown(reply)

    # Add to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })