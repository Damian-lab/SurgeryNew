from .models import PaymentMethod
from django import forms
from django.forms import ModelForm
from .models import *




class PaymentMethodForm(forms.ModelForm):
    

    class Meta:
        model = PaymentMethod
        fields = '__all__'

   