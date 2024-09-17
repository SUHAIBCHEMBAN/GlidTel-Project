from django.shortcuts import render,redirect
from .models import Products,Service,Booking
from .forms import BookingForm

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
    success = False  # Success flag for Toastify notification
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
            success = True  # Set success to True when booking is successful
            form = BookingForm()  # Reset form after submission
    else:
        form = BookingForm()
    
    return render(request, 'service-form.html', {'form': form, 'success': success})

def warrenty(request):
    return render(request,'warrenty.html')
    
def about(request):
    return render(request,'about.html')

def cart(request):
    if request.user.is_authenticated:
        return redirect('cart')
    
