from django.http import JsonResponse
from django.forms.models import model_to_dict

from products.models import Product


def api_home(request):
  instance = Product.objects.all().order_by('?').first()
  data = {}
  if instance:
    data = model_to_dict(
      instance, 
      fields=['id','title','content','price']
    )
  return JsonResponse(data)
