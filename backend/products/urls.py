from django.urls import path

from .views import (
  ProductMixinView,

  ProductDetailAPIView,
  ProductUpdateAPIView,
  ProductDestroyAPIView,
  ProductListCreateAPIView
)


urlpatterns = [
  path('mixin/', ProductMixinView.as_view()),
  path('<int:pk>/mixin/', ProductMixinView.as_view()),

  path('', ProductListCreateAPIView.as_view(), name='product-list'),
  path('<int:pk>/update/', ProductUpdateAPIView.as_view()),
  path('<int:pk>/delete/', ProductDestroyAPIView.as_view()),
  path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-edit')
]