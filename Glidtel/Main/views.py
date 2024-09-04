from django.shortcuts import render,redirect
from .models import Products

# Create your views here.

def home(request):
    return render(request,'home.html')

def shope(request):
    products = Products.objects.all()
    return render(request,'shope.html',{'Products':products})

def service(request):
    return render(request,'service.html')

def warrenty(request):
    return render(request,'warrenty.html')

def complaints(request):
    return render(request,'complaints.html')

def about(request):
    return render(request,'about.html')

def cart(request):
    if request.user.is_authenticated:
        return render(request,'cart.html')
    else:
        return redirect('login')
