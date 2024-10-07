from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('shope/',views.shope,name='shope'),
    path('buynow/<int:product_id>/', views.buynow, name='buynow'),
    path('confirm/<int:product_id>/',views.order_confirm,name='confirm'),
    path('service/',views.service,name='service'),
    path('service_form/',views.service_form,name='service_form'),
    path('warrenty/',views.warrenty,name='warrenty'),
    path('cart/',views.cart,name='cart'),
    path('about/',views.about,name='about'),
]