from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
  discount = serializers.SerializerMethodField(read_only=True)
  edit_url = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = Product
    fields = [      
      'edit_url',
      'pk',
      'title',
      'content',
      'price',
      'sale_price',
      'discount'
    ]

  def get_edit_url(self, object):
    # return f'/api/products/{object.pk}/'
    request = self.context.get('request')
    if request is None:
      return None
    return reverse('product-edit', kwargs={'pk': object.pk}, request=request)

  def get_discount(self, object):
      if not hasattr(object, 'id'):
        return None
      if not isinstance(object, Product):
        return None
      return object.get_discount() 
