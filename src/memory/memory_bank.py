import json 
import os

class Memory_bank:
    def __init__(self,memory_file="memory_bank.json"):
        self.memory_file=memory_file
        self.memory=self.load_memory()

    def load_memory(self):
        if not os.path.exists(self.memory_file):
            self.save_memory_to_file=[]
            return[]
        with open(self.memory_file,"r") as f:
            content=f.read().strip()
            if not content:
                return[]
            return json.loads(content)
        
    def save_memory(self,memory:str):
        if memory not in self.memory:
            self.memory.append(memory)
            with open(self.memory_file,"w") as f:
                json.dump(self.memory,f,indent=4)

    def search_memory(self,query:str):
        return [m for m in self.memory if query.lower() in m.lower()]
    
    def list_all(self):
        return self.memory
