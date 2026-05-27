import requests
from send_email import send_email
from langchain .chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

url = "https://newsapi.org/v2//top-headlines?" \
    "category=business&" \
    "pageSize=8&" \
    "sortBy=publishedAt&" \
    f"apiKey={NEWS_API_KEY}&" \
    "language=en"

request = requests.get(url)
content = request.json()
articles = content['articles']

prompt = f"""
You are a news summarizer.
Write a short paragraph on those news.
Another paragraph should include how they affect the stocks.
Here are the articles:
{articles}
"""

model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key = GOOGLE_API_KEY
)

response = model.invoke(prompt)
response_str = response.content

body = "Subject: Today's News\n\n"+ response_str+"\n\n"

body = body.encode('utf-8')    
send_email(body)



