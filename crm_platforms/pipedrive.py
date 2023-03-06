import email
from urllib import response
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
    print("Getting lead with id: ", id)
    # call pipedrive api to get the lead
    url = PipedriveURL + "leads/" + str(id) + "?api_token=" + self.auth.api_key
    print("URL :",url)
    # call the url and get the response
    response = requests.get(url)
    
    # check if the response is 200
    if response.status_code == 200:
      json_response = response.json()
      # check success parameter of response 
      success = json_response["success"]
      if success:
        # get the lead from the response
        lead = self.get_lead_from_response(json_response)
        return lead
    else:
      print("Getting a lead failed with status code: ", response.status_code)
      return None
  
  def get_lead_from_response(self, response):
    # extract all the attributes from the response
    title = response["data"]["title"]
    owner = response["data"]["owner_id"]
    leadsource = response["data"]["source_name"]
    id = response["data"]["id"]
    archived = response["data"]["is_archived"]
    createdate = response["data"]["add_time"]
    email = response["data"]["cc_email"]
    lastmodifieddate  = response["data"]["update_time"]
    firstname = "" #response["data"]["first_name"]
    lastname = "" #response["data"]["last_name"]
    
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