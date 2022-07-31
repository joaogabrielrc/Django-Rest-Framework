from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all().order_by('title')
  serializer_class = ProductSerializer
