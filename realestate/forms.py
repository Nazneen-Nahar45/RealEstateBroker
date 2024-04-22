from django.forms import ModelForm, widgets
from django import forms
from .models import *

class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = '__all__'
        widgets = {
            'house_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px; width: 500px'}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
        }



class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = '__all__'
        widgets = {
            'house_code': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px; width: 500px'}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'style': 'width: 500px;'}),
        }        