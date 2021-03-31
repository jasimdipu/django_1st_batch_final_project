from django.contrib import admin
from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    list_filter = ['category_name']
    search_fields = ['category_name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name']
    list_filter = ['brand_name']
    search_fields = ['brand_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_cat', 'product_brand', 'slug']
    list_filter = ['created_at', 'ratings', 'num_reviews', 'created_at']
    search_fields = ['product_name', 'product_cat', 'product_brand', 'slug']

    prepopulated_fields = {'slug': ('product_cat', 'product_name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
