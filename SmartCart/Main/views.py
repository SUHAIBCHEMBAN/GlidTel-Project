from django.shortcuts import render, get_object_or_404
from django.shortcuts import render,redirect
from .models import Products,Service,Booking
from .forms import BookingForm
from constants import *

# Create your views here.

def home(request):
    return render(request,'home.html')

def shope(request):
    products = Products.objects.all()
    return render(request,'shope.html',{'Products':products})

def buynow(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    return render(request, 'buynow.html', {'product': product})

def order_confirm(request):
    return render(request,'confirm.html')

def service(request):
    services = Service.objects.all()
    return render(request,'service.html',{'service':services})

from django.contrib import messages  # Import messages

def service_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Save the form data into the database
            Booking.objects.create(
                name=form.cleaned_data['name'],
                mobile_number=form.cleaned_data['mobile_number'],
                address=form.cleaned_data['address'],
                message=form.cleaned_data['message'],
            )
            # Add success message using Django's messages framework
            messages.success(request, BOOKING_SUCCESS)
            form = BookingForm()  # Reset form after submission
        else:
            # Add error message if the form is not valid
            messages.error(request, SUBMITION_ERROR)
    else:
        form = BookingForm()

    return render(request, 'service-form.html', {'form': form})


def warrenty(request):
    return render(request,'warrenty.html')
    
def about(request):
    return render(request,'about.html')

def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'cart.html')
    
