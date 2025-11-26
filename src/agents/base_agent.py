class base_agent:

    def __init__(self,llm,prompt_template):
        self.llm=llm
        self.prompt_template=prompt_template
        
    def run(self,query:str):
        prompt=self.prompt_template.format(query=query)
        
        return self.llm.chat([
            {"role":"system","content":" You are a an expert AI agent."},
        {"role":"user","content":prompt}
        ])
    
        