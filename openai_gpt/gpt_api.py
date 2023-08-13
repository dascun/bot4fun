import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key using os.getenv
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    print("API key not found in environment variables.")
    raise

# Load your API key from an environment variable or secret management service
openai.api_key = api_key

chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}]
)

print(chat_completion)
