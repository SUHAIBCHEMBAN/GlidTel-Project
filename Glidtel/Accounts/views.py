from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    return render(request,'login.html')

def otp_verify(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    return render(request,'otp.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    return redirect('login')