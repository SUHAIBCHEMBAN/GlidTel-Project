from django.shortcuts import render,redirect
from .models import Products,Service

# Create your views here.

def home(request):
    return render(request,'home.html')

def shope(request):
    products = Products.objects.all()
    return render(request,'shope.html',{'Products':products})

def service(request):
    services = Service.objects.all()
    return render(request,'service.html',{'service':services})

def service_form(request):
    return render(request,'service-form.html')

def warrenty(request):

    return render(request,'warrenty.html')

def complaints(request):
    if request.user.is_authenticated:
        return redirect('complaints')
    

def about(request):
    return render(request,'about.html')

def cart(request):
    if request.user.is_authenticated:
        return redirect('cart')
    
