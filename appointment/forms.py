from phonenumbers import PhoneNumber
from .models import Payment
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()  # returns user model active at the project

exec_choice = [
    ('USD', 'USD'),
    ('ZWL', 'ZWL'),
    ('ZAR', 'ZAR'),
    ('MedAid', 'MedAid'),
]


  

class PrescriptionForm(forms.ModelForm):
 
    class Meta:
        model = Prescription
        fields = ('patient', 'NatID', 'drugs', 'dosage', 'frequency', 'duration', 'diagnosis',
                   'examination', 'plan', 'prescription',  'referrance')

       



        # widgets = {
           
        #     'diagnosis': forms.TextInput(attrs={'placeholder': 'Click to select the 1CD10', 'class': 'form-control'}),


        # }

    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['patient'].queryset = User.objects.filter(
                user_type="P")
            self.fields['NatID'].queryset = User.objects.filter(user_type="P")
        


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = Appointment
        fields = '__all__'
        forms.CharField(widget=forms.HiddenInput(), required=False)

    # method called when an object is created from the class and it allow the class to initialize the attributes of a class
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['patient'].queryset = User.objects.filter(
                user_type="P")
            self.fields['doctor'].queryset = User.objects.filter(user_type="D")
            self.fields["date"].label = "Date (YYYY-MM-DD)"
            self.fields["time"].label = "Time 24 hr (HH:MM)"
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['Bp'].widget.attrs['readonly'] = True
        if instance and instance.pk:
            self.fields['Pulse'].widget.attrs['readonly'] = True
        if instance and instance.pk:
            self.fields['Temp'].widget.attrs['readonly'] = True
        if instance and instance.pk:
            self.fields['Weight'].widget.attrs['readonly'] = True
        if instance and instance.pk:
            self.fields['SP02'].widget.attrs['readonly'] = True
        if instance and instance.pk:
            self.fields['Allergic'].widget.attrs['readonly'] = True
        if instance and instance.pk:
            self.fields['status'].widget.attrs['readonly'] = True

    def clean_bp(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.bp
        else:
            return self.cleaned_data['Bp']

    def clean_pulse(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.pulse
        else:
            return self.cleaned_data['Pulse']

    def clean_temp(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.temp
        else:
            return self.cleaned_data['Temp']

    def clean_weight(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.weight
        else:
            return self.cleaned_data['Weight']

    def clean_spo2(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.sp02
        else:
            return self.cleaned_data['SP02']

    def clean_allergic(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.allergic
        else:
            return self.cleaned_data['Allergic']

    def clean_status(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.status
        else:
            return self.cleaned_data['status']


class PaymentForm(forms.ModelForm):
    paymentMethod = forms.ChoiceField(
        choices=exec_choice, widget=forms.RadioSelect())

    class Meta:
        model = Payment
        fields = '__all__'

        # ecoNumber = forms.CharField(required=True,widget=forms.TextInput(
        #     attrs={
        #         'placeholder': 'Enter MedAid Name', 
        #         'class': 'basicAutoComplete',
        #         'data-url': "/appointment/complete/",
             
        #     }
        # ))

        widgets = {

            'paymentMethod': forms.RadioSelect(attrs={'class': 'form-control'}),
            'medaid': forms.TextInput(attrs={'placeholder': 'Enter MedAid Name', 'class': 'form-control'}),
          


        }

##trying something out
    def calculate_total(self):
        if exec_choice==PaymentMethod.currency_name :
            self.total = PaymentMethod.rate
            return self.total

    # def __init__(self, *args, **kwargs):
    #     super(PaymentForm, self).__init__(*args, **kwargs)
    #     if self.instance :
    #         self.fields['patient'].queryset = User.objects.filter(user_type="P")
      
    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['patient'].queryset = User.objects.filter(
                user_type="P")
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                self.fields['total'].widget.attrs['readonly'] = True
            if instance and instance.pk:
                self.fields['medaid'].widget.attrs['readonly'] = True
            if instance and instance.pk:
                self.fields['ecoNumber'].widget.attrs['readonly'] = True

        
    def clean_total(self):
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                return instance.total
            else:
                return self.cleaned_data['total']
    def clean_medaid(self):
        instance = getattr(self, 'instance',None)
        if instance and instance.pk:
            return instance.medaid
        else: 
            return self.cleaned_data['medaid']
    def clean_ecoNumber(self):
        instance = getattr(self, 'instance',None)
        if instance and instance.pk:
            return instance.ecoNumber
        else: 
            return self.cleaned_data['ecoNumber']
