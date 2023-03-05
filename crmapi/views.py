from distutils.command.build_scripts import first_line_re
from platform import platform
from django.http import JsonResponse
from django.shortcuts import render

from authapi.models import Auth
from crm_platforms.factory import create_platform

# Create your views here.

def get_crm(request):
    # get customer id from request by fetching it from headers 
    customerid = request.headers.get("customerid")
    
    # for the customer id get the auth object from the database
    auth = Auth.objects.get(customer_id=customerid)
    
    # get the platform type from the auth object
    platform_type = auth.platform_type
    
    # get the platform object from the platform type
    crm = create_platform(platform_type, auth)
    
    return crm

# 2 paths to service according to our spec.
# /leads/ 
def lead_list(request):
    if request.method == "GET":
        # get the crm object
        crm = get_crm(request)
        
        # get the leads from the platform object
        leads = crm.get_leads()
        
        # return the leads in json array within a results key
        leads_json = {"results": leads}
        
        # return 200 with the leads
        return JsonResponse(leads_json, status=200)
    
    if request.method == "POST":
        # get the crm object
        crm = get_crm(request)
        
        # get owner, leadsource, title, company, firstname, lastname from request
        owner = request.POST.get("owner")
        leadsource = request.POST.get("leadsource")
        title = request.POST.get("title")
        company = request.POST.get("company")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        
        # create a lead object
        lead = crm.create_lead(owner, leadsource, title, company, firstname, lastname)
        
        # return 200 with the lead
        return JsonResponse(lead, status=200)
      
          

# /leads/<int:id>
def lead_detail(request, id):
    if request.method == "GET":
      crm = get_crm(request)

      # get id from request
      id = request.GET.get("id")
      
      # get the lead from the platform object
      lead = crm.get_lead(id)
      
      # return 200 with the lead
      return JsonResponse(lead.__dict__, status=200)