import email
from urllib import response
import requests
from .platform import Platform
from .leads import Lead

CloseURL = "https://api.close.com/api/v1/"
# APIKEY = "api_3BfxisiB6seHBum7PaQdIe.2gzTDQOM5ath9YHZUVkJBN"

class Close(Platform):
  
  def authenticate(self):
    apikey = self.auth.api_key
    print("APIKEY ", apikey)
    print("Authenticating with Close")
    
    # make a request to the url
    response = requests.get(f'{CloseURL}me/', auth=(self.auth.api_key, ''))
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
    print("Getting lead with id: ", id)
    # call pipedrive api to get the lead
    url = CloseURL + "contact/" + str(id)
    print("URL :",url)
    # call the url and get the response
    response = requests.get(url, auth=(self.auth.api_key, ''))
    
    # check if the response is 200
    if response.status_code == 200:
      json_response = response.json()
      # get the lead from the response
      lead = self.get_lead_from_response(json_response)
      return lead
    else:
      print("Getting a lead failed with status code: ", response.status_code)
      return None
  
  def get_lead_from_response(self, response):
    # extract all the attributes from the response
    title = response["title"]
    owner = response["created_by"]
    leadsource = response["lead_id"]
    id = response["data"]["id"]
    archived = False
    createdate = response["date_created"]
    email = response["emails"][0]["email"]
    lastmodifieddate  = response["date_updated"]
    # Clean this shit later.
    firstname = response["display_name"].split(" ")[0]
    lastname = response["display_name"].split(" ")[1]
    
    properties = {}
    properties["createdate"] = createdate
    properties["email"] = email
    properties["firstname"]= firstname
    properties["lastname"] = lastname
    properties["lastmodifieddate"] = lastmodifieddate
    
    # create a lead object 
    lead = Lead(id, properties, archived, title, owner, leadsource)
    return lead
    
  def create_lead(self, lead):
    pass
