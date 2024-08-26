import random
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import get_user_model,login as auth_login
# Create your views here.

def user_login(request):
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
            return redirect('otp_verify')
        else:
            user = get_user_model().objects.create_user(username=username,email=email)
            return redirect('otp_verify')
    return render(request,'login.html')

def otp_verify(request):
    if request.user.is_authenticated:
        return redirect(request,'home')
    
    if 'otp' not in request.session:
        return redirect('login')
    
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')

        if entered_otp == stored_otp:
            del request.session['otp']
            email = request.session['email']
            user = get_object_or_404(get_user_model(),email=email)
            auth_login(request,user)

            request.session['login_success'] = True

            message = 'Your Login Successfully Completed'
            mail_subject = 'Glide-Tel Mobiles'
            mail_message = 'Welcome, Glide-Tel Mobiles, Your Login Successfully Completed'
            send_mail(mail_subject,mail_message,'your_email@example.com',[email])
            return render(request,'otp.html',{'error':'Invalid OTP'})
    return render(request,'otp.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    return redirect('login')