from .models import ConsultationFee
from django import forms
from django.forms import ModelForm
from .models import *




class ConsultationFeeForm(forms.ModelForm):
    

    class Meta:
        model = ConsultationFee
        fields = '__all__'

   