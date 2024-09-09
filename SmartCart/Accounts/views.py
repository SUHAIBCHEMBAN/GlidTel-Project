from constants import *
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import get_user_model,login as auth_login , logout
from .forms import UserProfileForm, ProfilePictureForm
# Create your views here.


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        request.session['email'] = email  # Store email in session for OTP resend
        username = request.POST.get('username')

        # Fetch user by email
        user = get_user_model().objects.filter(email=email).first()

        if user:
            # Generate OTP and store it in session
            otp = ''.join(random.choices('0123456789', k=4))
            request.session['otp'] = otp
            # Send OTP via email
            mail_subject = 'Smart Cart Mobile Solution OTP'
            message = f'Your OTP is {otp}. Do not share this code with anyone.'
            send_mail(mail_subject, message, 'your_email@example.com', [email])

            # Redirect to OTP verification page
            return redirect('otp_verify')
        else:
            # Create user if they don't exist, send OTP
            user = get_user_model().objects.create_user(username=username, email=email)
            otp = ''.join(random.choices('0123456789', k=4))
            request.session['otp'] = otp
            mail_subject = 'Smart Cart Mobile Solution OTP'
            message = f'Your OTP is {otp}. Do not share this code with anyone.'
            send_mail(mail_subject, message, 'your_email@example.com', [email])

            return redirect('otp_verify')

    return render(request, 'login.html')



def otp_verify(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if 'otp' not in request.session:
        return redirect('login')
    
    if request.method == 'POST':
        # Combine the four OTP input fields into a single OTP value
        entered_otp = ''.join([
            request.POST.get('otp1', ''),
            request.POST.get('otp2', ''),
            request.POST.get('otp3', ''),
            request.POST.get('otp4', '')
        ])
        
        stored_otp = request.session.get('otp')

        if entered_otp == stored_otp:
            del request.session['otp']
            email = request.session['email']

            if not email:
                messages.error(request,EMAIL_NOT_FOUND)
                return redirect('login')
            
            user = get_object_or_404(get_user_model(),email=email)
            auth_login(request,user)

            # success message for toast notification
            messages.success(request,LOGIN_SUCCESS)

            mail_subject = 'Smart Cart Mobiles'
            mail_message = 'Welcome, Smart Cart Mobiles, Your Login Successfully Completed'
            send_mail(mail_subject,mail_message,'your_email@example.com',[email])

            return redirect('home')
        else:
            messages.error(request,INVALID_OTP)


    return render(request,'otp.html')


def resend_otp(request):
    # Get the user's email from session
    email = request.session.get('email')
    
    if not email:
        # If email is not found in session, redirect to login page
        messages.error(request,UNABLE_RESEND_OTP)
        return redirect('login')

    # Generate a new OTP and store it in session
    otp = ''.join(random.choices('0123456789', k=4))
    request.session['otp'] = otp

    # Send the new OTP to the user's email
    mail_subject = 'Resend OTP - Smart Cart Mobile Solution'
    message = f'Your new OTP is {otp}. Do not share this code with anyone.'
    send_mail(mail_subject, message, 'your_email@example.com', [email])

    # Notify the user that OTP has been resent
    messages.success(request, NEW_OTP)

    # Redirect back to OTP verification page
    return redirect('otp_verify')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login_required')
    
    user = request.user
    profile = user.userprofile  # Access the user profile

    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)
        profile_form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, PROFLE_UPDATE)
            return redirect('profile')
    else:
        user_form = UserProfileForm(instance=user)
        profile_form = ProfilePictureForm(instance=profile)
    
    profile_picture_url = profile.profile_picture.url if profile.profile_picture else ''

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'profile_picture_url': profile_picture_url, 
    }
    return render(request, 'profile.html', context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')
