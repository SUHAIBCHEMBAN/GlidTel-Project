from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('otp_verify/',views.otp_verify,name='otp_verify'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('resend_otp/', views.resend_otp, name='resend_otp'),
]
