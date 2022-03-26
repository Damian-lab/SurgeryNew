import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.forms.widgets import NumberInput
from django.utils import timezone

## return user model active in this project
User = get_user_model()

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]



class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True)
    dob = models.DateField(verbose_name='Date of birth',null =True)
    NatID = models.CharField(max_length=200,null =True,verbose_name="National ID")
    
    #age = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True)
    medicalAid = models.CharField(max_length=500, blank=True,verbose_name="Medical aid")
    membership = models.CharField(max_length=500, blank=True)
    beneficiary = models.CharField(max_length=500, blank=True)
    next_of_kin_name  = models.CharField(max_length=500, blank=True)
    next_of_kin_number = models.CharField(max_length=500, blank=True)
    
    
   
    
    status = models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], null=True, blank=True, max_length=8)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Profile for {}".format(self.user)

    @property
    def age(self):
        return timezone.now().year - self.dob.year

