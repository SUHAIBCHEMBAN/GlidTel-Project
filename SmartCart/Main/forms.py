# forms.py
from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(label="Full Name", max_length=100)
    mobile_number = forms.CharField(label="Mobile Number", max_length=15)
    address = forms.CharField(label="Address", widget=forms.Textarea)
    message = forms.CharField(label="Additional Details", widget=forms.Textarea, required=False)
