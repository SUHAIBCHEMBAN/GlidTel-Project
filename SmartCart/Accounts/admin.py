from django.contrib import admin
from .models import UserProfile

# Register your models here.

class Userprofile_Admin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile,Userprofile_Admin)
