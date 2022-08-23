from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
  discount = serializers.SerializerMethodField(read_only=True)  

  class Meta:
    model = Product
    fields = [
      'id',
      'title',
      'content',
      'price',
      'sale_price',
      'discount'      
    ]

  def get_discount(self, object):    
    if not isinstance(object, Product):
      return None    
    discount = f"{int(object.get_discount() * 100)}%"    
    return discount  


class CreateProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = [
      'id',
      'title',
      'content',
      'price'         
    ]
