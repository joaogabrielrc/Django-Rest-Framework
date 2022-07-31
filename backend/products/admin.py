from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'is_active']
  list_display_links = ['title']
