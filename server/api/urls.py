from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
  api_home,
  HomeAPIView
)


urlpatterns = [  
  path('auth/', obtain_auth_token),
  path('', HomeAPIView.as_view())  
]
