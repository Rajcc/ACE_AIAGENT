import json 
import os

class Memory_bank:
    def __init__(self,memory_file="memory_bank.json"):
        self.memory_file=memory_file
        self.memory=self.load_memory()

    def load_memory(self):
        if not os.path.exists(self.memory_file):
            return[]
        with open(self.memory_file,"r") as f:
            return json.load(f)
        
    def save_memory(self,memory:str):
        self.memory.append(memory)
        with open(self.memory_file,"w") as f:
            json.dump(self.memory,f,indent=4)

    def search_memory(self,query:str):
        return [m for m in self.memory if query.lower() in m.lower()]
    
    def list_all(self):
        return self.memory
