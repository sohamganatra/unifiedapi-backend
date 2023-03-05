from django.db import models

# Create your models here.

# We will store the auth related fields in the following model
# Customer ID
# Access token
# Refresh token
# API Key
# API Secret 
# Platform type 

class Auth(models.Model):
    # unique ID via which we will identify the customer which has linked a platform.
    customer_id = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100, null=True, blank=True)
    refresh_token = models.CharField(max_length=100, null=True, blank=True)
    api_key = models.CharField(max_length=100, null=True, blank=True)
    api_secret = models.CharField(max_length=100, null=True, blank=True)
    
    # platform type can be "hubspot", "salesforce", "pipedrive", "zoho", "freshsales"
    platform_type = models.CharField(max_length=100, default="hubspot", null=True, blank=True,
                                     choices=(("hubspot","hubspot"), ("salesforce","salesforce"),("pipedrive","pipedrive")))

    def __str__(self):
        return self.customer_id + " " + self.platform_type
      
    def validate(self):
        # validate the connection by making a request to the platform
        pass