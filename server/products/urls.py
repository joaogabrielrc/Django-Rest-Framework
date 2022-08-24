from django.urls import path

from .views import (
  ProductGenericAPIView,  
  ProductListCreateAPIView,
)


urlpatterns = [
  path('', ProductListCreateAPIView.as_view()),
  path('<int:pk>/', ProductGenericAPIView.as_view())
]