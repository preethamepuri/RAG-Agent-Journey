import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

Model_NAME = "gemini-2.5-flash"

def generate_answer(prompt):

    response = client.models.generate_content(
        model = Model_NAME,
        contents = prompt
    )

    return response.text