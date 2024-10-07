from django.contrib import admin
from .models import Products,Service,Booking

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','discription','quantity','image')
    list_filter = ['name','price']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','image','button')
    list_filter = ['title']

class BookinAdmin(admin.ModelAdmin):
    list_display = ('id','name','mobile_number','address','message')
    list_filter = ['mobile_number']



admin.site.register(Products,ProductsAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Booking,BookinAdmin)