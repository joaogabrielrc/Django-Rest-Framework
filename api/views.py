# Django Rest Framework API

from rest_framework.views import APIView, status
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


class HomeAPIView(APIView): 

  def get(self, request) -> Response:
    queryset = Product.objects.all().order_by("?")    

    if queryset.exists():
      instance = queryset.first()
      data = ProductSerializer(instance).data
      return Response(data, status=status.HTTP_200_OK)
    
    return Response({}, status=status.HTTP_404_NOT_FOUND)
  
  def post(self, request) -> Response:
    serializer = ProductSerializer(data=request.data)        

    if serializer.is_valid(raise_exception=True):      
      # serializer.save()      
      data = serializer.data      
      return Response(data, status=status.HTTP_201_CREATED)  

    return Response({}, status=status.HTTP_400_BAD_REQUEST)




# Django Rest Framework function API without serializers

from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product


@api_view(["GET"])
def api_home(request):
  queryset = Product.objects.all().order_by("?")
  data = {}

  if queryset.exists:
    instance = queryset.first()
    data = model_to_dict(instance, fields=["id", "title", "price"])

  return Response(data)




# Django API

from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product
  

def api_home_2(request):
  queryset = Product.objects.all().order_by("?")  
  data = {}  

  if queryset.exists():
    instance = queryset.first()
    data = model_to_dict(instance, fields=["id", "title", "price"])
    
  return JsonResponse(data)
