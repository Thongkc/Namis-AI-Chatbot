from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",   # free and fast model
    messages=[
        {"role": "user", "content": "Hello! Who are you?"}
    ]
)

reply = response.choices[0].message.content
print("AI says:", reply)