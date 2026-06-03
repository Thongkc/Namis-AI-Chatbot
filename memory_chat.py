from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# This list stores the full conversation history
conversation_history = []

print("Chatbot is ready! Type 'quit' to exit.")
print("-" * 40)

while True:
    # Get input from you
    user_input = input("You: ")

    # Exit if user types quit
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Add your message to the history
    conversation_history.append({
        "role": "user",
        "content": user_input
    })

    # Send the FULL history to the AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )

    # Get the AI reply
    reply = response.choices[0].message.content

    # Add AI reply to history too
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    print(f"AI: {reply}")
    print("-" * 40)