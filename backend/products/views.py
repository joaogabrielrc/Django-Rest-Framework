from rest_framework import generics, mixins

from api.mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer


# ------- Generics API's juntas no Mixin -------

class ProductMixinView(  
  mixins.ListModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  mixins.CreateModelMixin,
  generics.GenericAPIView 
):
  queryset = Product.objects.all().order_by('id')
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def get(self, request, *args, **kwargs):        
    pk = kwargs.get('pk')
    if pk is not None:
      return self.retrieve(request)
    return self.list(request)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

  def post(self, request):
    return self.create(request)

  def perform_create(self, serializer):    
    content = serializer.validated_data.get('content')
    if content == None:
      content = 'this is a mixin content'
    serializer.save(content=content)


# ------- Generics API's separadas -------

class ProductUpdateAPIView(
  StaffEditorPermissionMixin,
  generics.UpdateAPIView
):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title


class ProductDestroyAPIView(
  StaffEditorPermissionMixin,
  generics.DestroyAPIView
):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'


class ProductListCreateAPIView(
  StaffEditorPermissionMixin,
  generics.ListCreateAPIView
):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer    

  def perform_create(self, serializer):
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content == None:
      content = title
    serializer.save(content=content)


class ProductDetailAPIView(
  StaffEditorPermissionMixin,
  generics.RetrieveAPIView
):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
