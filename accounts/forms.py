from django.forms import ModelForm
from .models import *







class OrderFrom(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
