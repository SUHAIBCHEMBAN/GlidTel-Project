from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('shope',views.shope,name='shope'),
    path('service',views.service,name='service'),
    path('complaints',views.complaints,name='complaints'),
    path('warrenty',views.warrenty,name='warrenty'),
    path('cart',views.cart,name='cart'),
    path('about',views.about,name='about'),
]