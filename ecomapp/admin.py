from django.contrib import admin
from ecomapp.models import Product

# Register your models here.
# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','cat','price','is_active']
    list_filter=['cat','is_active']

admin.site.register(Product,ProductAdmin)