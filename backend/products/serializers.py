from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
  discount = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = Product
    fields = [
      'title',
      'content',
      'price',
      'sale_price',
      'discount'
    ]

  def get_discount(self, object):
      if not hasattr(object, 'id'):
        return None
      if not isinstance(object, Product):
        return None
      return object.get_discount() 
