from django.contrib import admin

from .form import ColorModelForm
from .models import *


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at', ]
    search_fields = ['title']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at', ]
    search_fields = ['title']


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at', ]
    search_fields = ['title']


@admin.register(ProductSizeModel)
class SizeModel(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at', ]
    search_fields = ['title']


@admin.register(ProductColorModel)
class ColorModel(admin.ModelAdmin):
    list_display = ['code', 'created_at']
    list_filter = ['created_at', ]
    search_fields = ['code']
    form = ColorModelForm


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'discount', 'short_description', 'created_at']
    list_filter = ['tags', 'brand', 'category', 'created_at']
    search_fields = ['title', 'short_description']
    autocomplete_fields = ['category', 'tags', 'brand', 'colors', 'sizes']
