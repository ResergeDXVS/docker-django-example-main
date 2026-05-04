from django.contrib import admin

from .models import Product, Sales, SalesDetail

# Register your models here.
admin.site.register(Product)
admin.site.register(Sales)
admin.site.register(SalesDetail)