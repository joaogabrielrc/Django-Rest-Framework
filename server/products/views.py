from rest_framework import generics

from api.mixins import StaffEditorPermissionMixin
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView
  ):
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

  def get_serializer_class(self):    
    return super().get_serializer_class()


class ProductGenericAPIView(  
    StaffEditorPermissionMixin,      
    generics.RetrieveAPIView,    
    generics.UpdateAPIView,
    generics.DestroyAPIView
  ):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer   

  def perform_update(self, serializer):
    return super().perform_update(serializer)
  
  def perform_destroy(self, instance):
    return super().perform_destroy(instance)

  def get_serializer_class(self):
    return super().get_serializer_class()




# Mixin API Views

from rest_framework import mixins


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

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)  
