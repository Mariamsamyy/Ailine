from django import forms
from .models import Rating
from .models import FlightOrder

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating_value']  


class FlightOrderForm(forms.ModelForm):
    class Meta:
        model = FlightOrder
        fields = ['flight_number', 'customer_name']

