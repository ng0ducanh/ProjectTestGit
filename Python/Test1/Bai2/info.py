class Info:
    def __init__(self, ip, location, status, reliability):
        self.ip = ip
        self.location = location
        self.status = status
        self.reliability = reliability
        pass
    
    def __str__(self) -> str:
        return "ip: " + self.ip + " location: " + self.location + " status: " + self.status + " reliability: " + self.reliability
        pass

    def _get_ip(self):
        return self.ip
        
      
    def set_ip(self, x):
        self.ip = x
        