from django import forms
from .models import Rating
from .models import FlightOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating_value', 'comments']

class FlightOrderForm(forms.ModelForm):
    class Meta:
        model = FlightOrder
        fields = ['flight_number', 'customer_name']


