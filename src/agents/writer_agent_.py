from .base_agent import base_agent
from llm.prompt.writer_prompts import writer_prompt

class writer_agent(base_agent):
    def __init__(self,llm):
        super().__init__(llm,writer_prompt)