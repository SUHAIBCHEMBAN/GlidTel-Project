import random
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect(request,'home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        request.session['email'] = email
        username = request.POST.get('username')

        user = get_user_model().objects.filter(email=email).first()
        if user:
            otp = ''.join(random.choices('01234589',k=4))
            request.session['otp'] = otp
            mail_subject = 'Glide Tel Mobiles'
            message = f'Your OTP is {otp}, This Code Not Share!'
            send_mail(mail_subject,message,'your_email@example.com',[email])
        else:
            user = get_user_model().objects.create_user(username=username,email=email)
            return redirect(request,'otp_verify')
    return render(request,'login.html')

def otp_verify(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    return render(request,'otp.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    return redirect('login')