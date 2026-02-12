from django.db import models
from django import forms
from .models import Booking, TravelService
from django.core.exceptions import ValidationError
from django.utils import timezone

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['travel_date']
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
    def clean_travel_date(self):
        date = self.cleaned_data.get('travel_date')
        if date < timezone.now().date():
            raise ValidationError("You cannot book a trip for a past date!")
        return date
    
class TravelServiceForm(forms.ModelForm):
    class Meta:
        model = TravelService
        fields = ['category', 'title', 'destination', 'price']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            #'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }