from django.contrib import admin
from .models import Products,Service,Booking

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','discription','quantity','image')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','image','button')

class BookinAdmin(admin.ModelAdmin):
    list_display = ('id','name','mobile_number','address','message')



admin.site.register(Products,ProductsAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(Booking,BookinAdmin)