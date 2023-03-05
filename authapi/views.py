from platform import platform
from django.http import HttpResponse
from django.shortcuts import render
from .models import Auth
# Create your views here.

# 1 path to service according to our spec.
def connect(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        platform_type = request.POST.get("platform_type")
        refresh_token = request.POST.get("refresh_token")
        access_token = request.POST.get("access_token")
        api_key = request.POST.get("api_key")
        api_secret = request.POST.get("api_secret")
        
        auth = Auth.objects.create(customer_id=customer_id, platform_type=platform_type,
                                   refresh_token=refresh_token, access_token=access_token,
                                   api_key=api_key, api_secret=api_secret)
        
        auth.save()
        # check if the connection is successful 
        if auth.validate():
          # return 200
          return HttpResponse(status=200)
        else:
          # return 400
          return HttpResponse(status=400)