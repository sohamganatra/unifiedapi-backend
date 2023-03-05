class Platform:
    def __init__(self, platform_type, auth):
      self.platform_type = platform_type
      self.authenticate(auth)
      
    def authenticate(self, auth):
      pass
    
    def get_leads(self):
      pass
    
    def get_lead(self, id):
      pass
    
    def create_lead(self, lead):
      pass