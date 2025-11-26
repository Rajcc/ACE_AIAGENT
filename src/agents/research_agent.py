from .base_agent import base_agent
from llm.prompt.research_prompts import research_prompt

class research_agent(base_agent):
     def __init__(self,llm):
          super().__init__(llm,research_prompt)

          

