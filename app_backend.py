import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

API_KEY = os.getenv("API_KEY")
MODEL = "meta-llama/llama-4-maverick:free"

conversation_history = [
    {"role": "system", "content": "You are a helpful and informative voice assistant specialized in digital services in India. Answer briefly."}
]

def ask_llama(prompt):
    conversation_history.append({"role": "user", "content": prompt})
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": conversation_history
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            conversation_history.append({"role": "assistant", "content": reply})
            return reply
        else:
            return f"Error: ({response.status_code})"
    except Exception as e:
        return f"Exception: {str(e)}"
