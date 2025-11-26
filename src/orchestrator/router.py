from llm.llm_client import GroqLLM
from llm.prompt.router_prompts import Router_prompts

class router:
    def __init__(self,):
        self.llm=GroqLLM()

    def route(self,query:str):
        prompt=Router_prompts.format(query=query)
        
        result=self.llm.chat([
            {"role":"system","content":" You are a routing AI."},
            {"role":"user","content":prompt}
        ])

        return result.strip().lower()
        
        