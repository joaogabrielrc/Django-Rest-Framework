from rest_framework import generics, mixins, permissions, authentication

from api.authentication import TokenAuthentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission


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

class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'


class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  authentication_classes = [
    authentication.SessionAuthentication,
    TokenAuthentication
  ]
  permission_classes = [
    permissions.IsAdminUser, 
    IsStaffEditorPermission
  ]

  def perform_create(self, serializer):
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content')
    if content == None:
      content = title
    serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
