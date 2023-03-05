from .platform import Platform
from .leads import Lead

class Hubspot(Platform):
  
  def authenticate(self, auth):
    pass
  
  def get_leads(self):
    pass
  
  def get_lead(self, id):
    properties = {}
    lead = Lead(id, properties, False, "Mr.", "John Doe", "Google")
    return lead
  
  def create_lead(self, lead):
    pass