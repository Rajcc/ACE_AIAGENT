from .base_agent import base_agent
from llm.prompt.analysis_prompts import analysis_prompt

class analysis_agent(base_agent):
    def __init__(self,llm):
        super().__init__(llm,analysis_prompt)

    