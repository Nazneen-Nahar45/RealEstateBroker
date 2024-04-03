from django.forms import ModelForm
from .models import *

class Sellform(ModelForm):
    class Meta:
        model = Sell
        fields = '__all__'