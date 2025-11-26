class Sessionservice:
    def __init__(self,max_history=10):
        self.max_history=max_history
        self.history=[]

    def add_message(self,role:str,content:str):
        self.history.append({"role":role,"content":content})
        self.history=self.history[-self.max_history:]
    
    def get_history(self):
        return self.history
    
    def clear_history(self):
        self.history=[]

