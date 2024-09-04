from django.contrib import admin
from .models import Products

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','discription','quantity','image')



admin.site.register(Products,ProductsAdmin)