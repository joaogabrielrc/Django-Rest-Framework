# Django Rest Framework API
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET', 'POST'])  
def api_home(request): 

  if request.method == 'POST':    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()      
      return Response(serializer.data)

  if request.method == 'GET':
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
      data = ProductSerializer(instance).data
    return Response(data)




# Without serializers Django Rest Framework API
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product


@api_view(['GET'])
def api_home_2(request):
  instance = Product.objects.all().order_by('?').first()
  data = {}
  if instance:
    data = model_to_dict(instance, fields=['id', 'title', 'price'])
  return Response(data)




# Django API
from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product


def api_home_3(request):
  instance = Product.objects.all().order_by('?').first()
  data = {}
  if instance:
    data = model_to_dict(instance, fields=['id', 'title', 'price'])
  return JsonResponse(data)
