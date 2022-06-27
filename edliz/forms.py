from .models import Edliz
from django import forms
from django.forms import ModelForm
from .models import *




class EdlizForm(forms.ModelForm):
    

    class Meta:
        model = Edliz
        fields = '__all__'

   