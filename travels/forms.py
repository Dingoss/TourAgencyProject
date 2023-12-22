from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_name', 'user_lname', 'user_phone', 'user_email', 'user_travel_name']