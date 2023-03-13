import requests
from .platform import Platform
from .leads import Lead

HubspotURL = "https://api.hubapi.com/crm/v3/objects/"

class Hubspot(Platform):
  
  def authenticate(self):
    access_token = self.auth.access_token
    print("ACCESS_TOKEN ", access_token)
    url = HubspotURL + "companies/"
    response = requests.get(url, headers={"Authorization": "Bearer " + self.auth.access_token})
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
    url = HubspotURL + "contacts/" + str(id) + "?&properties=createdate,email,firstname,hs_object_id,lastmodifieddate,lastname,jobtitle"
    
    print("URL :",url)
    # call the url and get the response

    response = requests.get(url, headers={"Authorization": "Bearer " + self.auth.access_token})
    # check if the response is 200
    if response.status_code == 200:
      json_response = response.json()
      # check success parameter of response 
      print("json_response: ", json_response)
      success = json_response["id"]
      if success:
        # get the lead from the response
        lead = self.get_lead_from_response(json_response)
        return lead
    else:
      print("Getting a lead failed with status code: ", response.status_code)
      return None

  def get_lead_from_response(self, response):
    # extract all the attributes from the response
    title = response["properties"]["jobtitle"]
    owner = response["properties"]["hs_object_id"]
    leadsource = "" #response["results"]["properties"]["source_name"]
    id = response["id"]
    archived = response["archived"]
    createdate = response["createdAt"]
    email = response["properties"]["email"]
    lastmodifieddate  = response["properties"]["lastmodifieddate"]
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