class Platform:
    def __init__(self, platform_type, auth):
      self.platform_type = platform_type
      self.auth = auth
      
    def authenticate(self):
      raise("Not implemented")
    
    def get_leads(self):
      raise("Not implemented")
    
    def get_lead(self, id):
      raise("Not implemented")
    
    def create_lead(self, lead):
      raise("Not implemented")