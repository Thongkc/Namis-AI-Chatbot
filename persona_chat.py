from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# System prompt — this defines your chatbot's personality
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

# Start conversation history with the system prompt
conversation_history = [
    {"role": "system", "content": system_prompt}
]

print("Namis (Career Coach) is ready! Type 'quit' to exit.")
print("-" * 40)

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Namis: Good luck with your job search! You've got this! 💪")
        break

    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )

    reply = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    print(f"Maya: {reply}")
    print("-" * 40)