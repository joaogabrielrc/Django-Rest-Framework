from django.urls import path

from .views import (
  ProductListCreateAPIView,
  ProductDetailAPIView,
  ProductUpdateAPIView,
  ProductDeleteAPIView,  
  ProductMixinView
)


urlpatterns = [
  path('', ProductMixinView.as_view()),
  path('<int:pk>/', ProductMixinView.as_view()),
  path('<int:pk>/update/', ProductMixinView.as_view()),
  path('<int:pk>/delete/', ProductMixinView.as_view())
]
