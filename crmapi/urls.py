# 2 URLS according to our spec. 
# 1. /leads/ - GET, POST
# 2. /leads/<int:pk> - GET

from django.urls import path
from . import views
urlpatterns = [
    path("leads/",views.lead_list),
    path("leads/<int:id>",views.lead_detail),
]
