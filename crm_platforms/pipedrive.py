import requests
from .platform import Platform
from .leads import Lead

PipedriveURL = "https://api.pipedrive.com/v1/"
# api key = f0bec7d5029c0a20c993a6fe414e5de8e6770ab0


class Pipedrive(Platform):
  
  def authenticate(self):
    apikey = self.auth.api_key
    print("APIKEY ", apikey)
    url = PipedriveURL + "organizations?api_token=" + apikey
    
    print("URL :",url)
    print("Authenticating with Pipedrive")
    
    # make a request to the url
    response = requests.get(url)
    # print response content
    print(response.content)
    
    # check if the response is 200
    if response.status_code == 200:
      return True
    else:
      print("Authentication failed", response.status_code)
      return False
    
  def get_leads(self):
    pass
  
  def get_lead(self, id):
    properties = {}
    lead = Lead(id, properties, False, "Mr.", "John Doe", "Google")
    return lead
  
  def create_lead(self, lead):
    pass