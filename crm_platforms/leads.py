# lead object will be used and returned in the response. 
import json


class Lead:
    # lead object will have the following fields
    # id - unique ID of the lead
    # properties - a dictionary of properties of the lead
    # properties will be createdate, email, firstname,lastname, lastmodifieddate,
    # archieved - boolean value indicating if the lead is archived or not
    # title - title of the lead
    # owner - owner of the lead
    # leadsource - lead source of the lead
    def __init__(self, id, properties, archived, title, owner, leadsource):
        self.id = id
        self.properties = properties
        self.archived = archived
        self.title = title
        self.owner = owner
        self.leadsource = leadsource

    def __str__(self):
        return json.dumps(self.__dict__)
    