from django.urls import path

from .views import (
  api_home,
  HomeAPIView
)


urlpatterns = [  
  path('', HomeAPIView.as_view())  
]
