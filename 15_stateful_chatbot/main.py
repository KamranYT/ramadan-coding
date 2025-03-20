import os # environments variables ko access karne men help kare ga.
import chainlit as cl
import google.generativeai as genai 
from dotenv import load_dotenv
from typing import Optional, Dict

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash"
)

@cl.oauth_callback #user ko github ke madad se login karne men hamare madad kare ga
def oauth_callback(
    provider_id: str,
    token: str,
    row_user_data: Dict[str, str],
    default_user: cl.User,
) -> Optional[cl.User]:
    """
    Handle the OAuth callback from GitHub
    Returnth the user object if authentication is successfull, None otherwise.
    """

    print(f"Provider: {provider_id}")
    print(f"User data: {row_user_data}")

    return default_user

@cl.on_chat_start
async def handle_chat_start():

    cl.user_session.set("history", [])

    await cl.Message(content="Hello! How can I help you today?").send()
