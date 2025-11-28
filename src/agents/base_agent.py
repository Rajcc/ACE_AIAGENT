

class base_agent:

    def __init__(self,llm,prompt_template):
        self.llm=llm
        self.prompt_template=prompt_template
        
    def execute(self,query:str,memory_context):
        prompt=self.prompt_template.format(query=query,memory_context=memory_context if memory_context else ""
        )
        

        message=[]

        if memory_context:
            message.extend(memory_context)

        message.append({"role": "system", "content": "You are an expert AI agent."})
        
        # Add user query
        message.append({"role": "user", "content": prompt})
        
        return self.llm.chat([
            {"role":"system","content":" You are a an expert AI agent."},
        {"role":"user","content":prompt}
        ])
    
        