from django.shortcuts import render,redirect

# Create your views here.

def home(request):
    return render(request,'home.html')

def shope(request):
    return render(request,'shope.html')

def service(request):
    return render(request,'service.html')