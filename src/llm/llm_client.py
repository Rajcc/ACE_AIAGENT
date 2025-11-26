from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

class GroqLLM:
    def __init__(self,model="llama-3.1-70b-versatile"):
        self.client=Groq(api_key=os.getenv("Groq_API_KEY"))
        self.model=model

        def chat(self,messages):
            response=self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.3,
            )
            return response.choices[0].message.content
            