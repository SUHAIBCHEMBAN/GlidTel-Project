from django.contrib import admin
from .models import Products,Service

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','discription','quantity','image')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','image','button')



admin.site.register(Products,ProductsAdmin)
admin.site.register(Service,ServiceAdmin)