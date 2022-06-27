from .models import MedAid
from django import forms
from django.forms import ModelForm
from .models import *




class MedAidForm(forms.ModelForm):
    

    class Meta:
        model = MedAid
        fields = '__all__'

   