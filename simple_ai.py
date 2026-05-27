from langchain .chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key = GOOGLE_API_KEY
)

response = model.invoke("Is a pen better than a pencil?")


response_str = response.content
print(response_str)