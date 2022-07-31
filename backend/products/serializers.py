from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
  discount = serializers.SerializerMethodField(read_only=True)
  url = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = Product
    fields = [
      'id',
      'title',
      'content',
      'price',
      'sale_price',
      'discount',
      'url'
    ]

  def get_discount(self, object):    
    if not isinstance(object, Product):
      return None
    return object.get_discount()    

  def get_url(self, object):
    return f'/api/products/{object.id}/'    
