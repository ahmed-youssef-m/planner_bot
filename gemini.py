from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from config import sys_instruct

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API key is missing. Set the GEMINI_API_KEY environment variable.")

client = genai.Client(api_key=API_KEY)


def get_chat_session():
    try:
        return client.chats.create(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(system_instruction=sys_instruct),
        )
    except Exception as e:
        print(f"Error creating chat session: {e}")
        return None


def send_message(data: str):
    chat_session = get_chat_session()
    if chat_session:
        try:
            response = chat_session.send_message(data)
            return response.text
        except Exception as e:
            print(f"Error sending message: {e}")
            return "Error: Unable to process request."
    return "Error: Unable to process request."
