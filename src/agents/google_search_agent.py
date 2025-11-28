import os
import requests
import json

serper_api_key = os.getenv("serper_API_KEY")

class google_search_agent:
    def __init__(self):
        self.api_key = serper_api_key
        self.search_url = "https://google.serper.dev/search"

    def execute(self,query:str,memory_context=None):
        return self.search(query)
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