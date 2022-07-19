from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def api_home(request):
  if request.method == 'GET':
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
      data = ProductSerializer(instance).data

    return Response(data)
  
  elif request.method == 'POST':    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      instance = serializer.save()      
      return Response(serializer.data)
      
    return Response({'Bad request': 'Ivalid data'}, status=400)



# ---------- Django View -----------

from django.http import JsonResponse
from django.forms.models import model_to_dict


def api_home_old(request):
  instance = Product.objects.all().order_by('?').first()
  data = {}
  if instance:
    data = model_to_dict(
      instance, 
      fields=['id','title','content','price']
    )
  return JsonResponse(data)
