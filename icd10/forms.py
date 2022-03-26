from .models import Icd10
from django import forms
from django.forms import ModelForm
from .models import *




class Icd10Form(forms.ModelForm):
    

    class Meta:
        model = Icd10
        fields = '__all__'

   