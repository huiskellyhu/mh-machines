class Washer:
    def __init__(self):
        self.status = "FREE" # IN USE // DONE 
        self.time_start = None
        self.time_end = None
    
    def set_status(self, new_stat):
        self.status = new_stat
    
    def set_time_start(self, start):
        self.time_start = start
    
    def set_time_end(self,end):
        self.time_end = end

class Autoclave:
    def __init__(self):
        self.status = "FREE" # IN USE // DONE 
        self.time_start = None
        self.time_end = None
    
    def set_status(self, new_stat):
        self.status = new_stat
    
    def set_time_start(self, start):
        self.time_start = start
    
    def set_time_end(self,end):
        self.time_end = end