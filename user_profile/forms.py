from django.contrib.auth import get_user_model
from django import forms
from .models import *
from django.forms.widgets import NumberInput



class ProfileUpdateForm(forms.ModelForm):
    dob =forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.RadioSelect)
    class Meta:
        model = UserProfile
        fields = ('name', 'NatID','phone', 'gender','dob','address','medicalAid','membership','beneficiary','next_of_kin_name','next_of_kin_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['name'].widget.attrs['readonly'] = True
       
    
    def clean_name(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.name
        else:
            return self.cleaned_data['name']

  

@property
def age(self):
        return timezone.now().year - self.dob.year
        

class DoctorProfileForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=False, widget=forms.RadioSelect)
    class Meta:
        model = UserProfile
        fields = ('name', 'NatID','phone',  'gender', 'address', 'status')
        



    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)