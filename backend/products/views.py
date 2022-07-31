from rest_framework import generics, mixins

from .models import Product
from .serializers import ProductSerializer  


# Separate APIs View

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_create(self, serializer):
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = title
    serializer.save(content=content)    

  def get_queryset(self):
    return self.queryset.order_by('title')


class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class ProductDeleteAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_destroy(self, instance):
    instance.is_active = False
    instance.save()    




# Mixin API View

class ProductMixinView(
    mixins.ListModelMixin,    
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
  ):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  def get(self, request, *args, **kwargs):
    pk = kwargs.get('pk')
    if pk is not None:
      return self.retrieve(request, *args, **kwargs)
    return self.list(request, *args, **kwargs)

  def perform_create(self, serializer):
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content is None:
      content = title
    serializer.save(content=content)    

  def get_queryset(self):
    return self.queryset.order_by('title')

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
  
  def perform_destroy(self, instance):
    instance.is_active = False
    instance.save()    

