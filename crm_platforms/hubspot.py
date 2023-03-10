import requests
from .platform import Platform
from .leads import Lead

HubspotURL = "https://api.hubapi.com/crm/v3/objects/"

class Hubspot(Platform):
  
  def authenticate(self):
    self.auth.access_token = "pat-na1-d016f754-2577-4c2f-aa42-ccd1f837bd9f"
  
  def get_leads(self):
    pass
  
  def get_lead(self, id):
    print("Getting lead with id: ", id)
    # call pipedrive api to get the lead
    url = HubspotURL + "contacts/" + str(id) + "?&properties=createdate,email,firstname,hs_object_id,lastmodifieddate,lastname,jobtitle"
    
    print("URL :",url)
    # call the url and get the response

    response = requests.get(url, headers={"Authorization": "Bearer " + self.auth.access_token})
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
    title = response["results"]["properties"]["jobtitle"]
    owner = response["results"]["properties"]["hubspot_owner_id"]
    leadsource = "" #response["results"]["properties"]["source_name"]
    id = response["results"]["id"]
    archived = response["results"]["archived"]
    createdate = response["results"]["createdAt"]
    email = response["results"]["properties"]["email"]
    lastmodifieddate  = response["results"]["properties"]["lastmodifieddate"]
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