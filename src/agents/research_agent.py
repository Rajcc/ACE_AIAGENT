from .base_agent import base_agent
from src.llm.prompt.research_prompts import reseach_prompt

class research_agent(base_agent):
     def __init__(self,llm):
          super().__init__(llm,reseach_prompt)

          

