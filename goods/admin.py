from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'in_stock', 'pet_type')
    list_filter = ('category', 'in_stock', 'pet_type')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}