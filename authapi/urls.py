# URL to add a new connection 
# we can get either access token, refresh token, api key and api secret and platform type

from django.urls import path
from . import views
urlpatterns = [
    path("/connect", views.connect),
]
