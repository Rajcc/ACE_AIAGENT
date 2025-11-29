import os
import requests
import json
from llm.prompt.google_search_prompt import google_search_prompt
from llm.llm_client import GroqLLM

serper_api_key = os.getenv("serper_API_KEY")

class google_search_agent:
    def __init__(self):
        self.api_key = serper_api_key
        self.search_url = "https://google.serper.dev/search"
        self.llm=GroqLLM()
        self.prompt_google=google_search_prompt


    def execute(self,query:str,memory_context=None):
        raw_results= self.search(query)

        prompt=self.prompt_google.format(query=query,search_results=raw_results,memory_context=memory_context if memory_context else "no prevoius context")

        message=[]   

        if memory_context:
           message.extend(memory_context)

        message.append({"role": "system", "content": "You are an expert Google Search AI agent."})

        message.append({"role": "user", "content": prompt})

        response=self.llm.chat(message)

        return response
    def search(self,query:str):
        try:
            params={
                "engine":"google",
                "q":query,
                "api_key":self.api_key
            }
            response=requests.get(self.search_url,params=params)
            data=response.json()

            results=data.get("organic",[])
            if not results:
                return "No results found."
            
            summary=""
            for i in results[:5]:
                summary+=f"Title: {i.get('title')}\nSnippet: {i.get('snippet')}\nLink: {i.get('link')}\n\n"

            return f"top 5 Google Search Results:\n\n{summary}"
        except Exception as e:
            return f"An error occurred during the search: {str(e)}"