from llm.llm_client import GroqLLM
from src.agents.research_agent import research_agent
from src.agents.analysis_agent import analysis_agent
from src.agents.writer_agent_ import writer_agent
from llm.prompt.router_prompts import Router_prompts
from src.orchestrator.router import router
from src.agents.google_search_agent import google_search_agent

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

    def run(self,user_query:str):
            agent_type=self.router.route(user_query)

            agent=self.agents.get(agent_type)
            
            if not agent:
                return "Sorry, I could not determine the appropriate agent for your request."
            return agent.run(user_query)

