from llm.llm_client import GroqLLM
from src.agents.research_agent import research_agent
from src.agents.analysis_agent import analysis_agent
from src.agents.writer_agent_ import writer_agent
from src.llm.prompt.research_prompts import reseach_prompt
from src.orchestrator.router import router
from src.agents.google_search_agent import google_search_agent
from src.memory.memory_bank import Memory_bank
from src.memory.session_service import Sessionservice
class orchestrator:
    def __init__(self):
        self.llm=GroqLLM()
        self.router=router()
        self.agents={
            "research":research_agent(self.llm),
            "analysis":analysis_agent(self.llm),
            "writing":writer_agent(self.llm),
            "google_search":google_search_agent()
        }
        self.memory=Memory_bank()
        self.session_service=Sessionservice()

    def message_to_text(self,message):
        self.message=message
        return "/n".join([f"{m['role']}:{m['content']}" for m in message])
    
    def run(self,user_query:str):
           

            agent_type=self.router.route(user_query)

            agent=self.agents.get(agent_type)
            
            
            if not agent:
                response= "Sorry, I could not determine the appropriate agent for your request."
                
            else: 
                long_term_memory=[{'role':"system","content":m}for m in self.memory.list_all()]
                short_term_memory=self.session_service.get_history()
                memory_context=long_term_memory+short_term_memory 

                response=agent.execute(user_query,memory_context)
    
            self.session_service.add_message("user", user_query)
            self.session_service.add_message("assistant", response)

            self.store_important_memory(user_query,response)

            return response
    
    def store_important_memory(self,user_query:str,response:str):
         important_keywords=["I like", "my name is", "I prefer", "I am working on", "I plan to", "remember"]
         text=user_query.lower() 

         if any (k in text for k in important_keywords):
                self.memory.save_memory(f"User said: {user_query}")
                
    

