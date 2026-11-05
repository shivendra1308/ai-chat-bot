# services/groq_service.py
# All Groq AI logic lives here!

from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Groq client once!
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a helpful AI assistant
                called Shivendra's AI. You are
                friendly, concise and helpful.
                You help with coding, AI concepts
                and general questions."""

MODEL = "openai/gpt-oss-20b"

def get_groq_stream(messages_history: list):
    """
    Get streaming response from Groq
    messages_history: list of {role, content} dicts
    """
    stream = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            *messages_history
        ],
        max_tokens=1000,
        temperature=0.7,
        stream=True
    )
    return stream

def get_available_models():
    """Get list of available Groq models"""
    models = client.models.list()
    return [m.id for m in models.data]