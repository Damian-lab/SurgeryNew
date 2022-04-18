import datetime
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from tomlkit import comment, value
import icd10
from icd10.models import Icd10
from paymentMethod.models import PaymentMethod

User = get_user_model()
dos_choice = [
    ('ml', 'ml'),
    ('mg', 'mg'),
    ('g', 'g'),
    ('drops', 'drops'),
    ('tablet', 'tablet'),
    ('spray', 'spray'),
    ('puff', 'puff'),
    ('mcg', 'mcg'),
    ('iu', 'iu'),
]
payment_choice = [
    ('ZWL', "ZWL"),
    ('RTGS', "RTGS"),
    ('ZAR', "ZAR"),
    ('USD', "USD"),
    ('MedAid', "MedAid"),
]

freq_choice = [
    ('od', 'od'),
    ('bd', 'bd'),
    ('tds', 'tds'),
    ('qids', 'qids'),
    ('weekly', 'weekly'),
    ('2 weekly', '2 weekly'),
    ('monthly', 'monthly'),
    ('stat', 'stat'),
]

drugs = [
    ('ampicillin iv', 'ampicillin iv'),
    (' gentamicin iv ', ' gentamicin iv '),
    ('chloramphenicol iv ', 'chloramphenicol iv '),
    ('ceftriaxone iv', 'ceftriaxone iv'),
    ('ciprofloxacin po', 'ciprofloxacin po'),
    ('metronidazole po', 'metronidazole po'),
    ('chloramphenicol iv', 'chloramphenicol iv'),
    ('tetracycline eye oint. 1%', 'tetracycline eye oint. 1%'),
    ('benzylpenicillin im/iv', 'benzylpenicillin im/iv'),
    ('Other(Specify)', 'Other(Specify)'),

]


# Create your models here.


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField(default=datetime.time)
    status = models.CharField(
        choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctor')
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receptionist')
  
    Allergic = models.CharField(max_length=200)
    Bp = models.CharField(max_length=200)
    Pulse = models.CharField(max_length=200)
    Temp = models.CharField(max_length=200)
    Weight = models.CharField(max_length=200)
    SP02 = models.CharField(max_length=200)
    notification= models.BooleanField.default=False

# meta and ordering wasnt there
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Patient - {}  status - {}    - At   - {} " .format(self.patient, self.status, self.date)


class Prescription(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
     

    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='doctor_prescription')
    # patient = models.ForeignKey(
    #     User, on_delete=models.CASCADE, related_name='patient_prescription', null=True)
    patient = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    NatID = models.CharField(max_length=200, null=True,
                             verbose_name="National ID")
    drugs = models.CharField(
        choices=drugs, max_length=100, blank=True, null=True, verbose_name="Drugs")
    dosage = models.CharField(max_length=200, verbose_name="Dosage")
    frequency = models.CharField(max_length=200, verbose_name="Frequency")
    duration = models.CharField(max_length=200, verbose_name="Duration")
    diagnosis = models.CharField(max_length=200)
    comment   = models.TextField(null=True,verbose_name="Add a comment on ICD10")
    examination = models.TextField(null=True, verbose_name="Examination")
    plan = models.TextField(null=True, verbose_name="Plan")
    prescription = models.TextField(null=True, verbose_name="Prescription")
    
    #TODO: include comment section on diagnosis
   
    referrance = models.CharField(
        max_length=200, null=True, verbose_name="Referrance")


   

    class Meta:
        ordering = ('-id',)
       

    def __str__(self):
        return "Presciption Doc-{} Patient-{}".format(self.doctor, self.patient)
   

PAYMENT_TYPES = [

    ('C', 'Consulting')
]

status = [
    ('Pending', 'Pending'),
    ('Paid', 'Paid'),


]


class Payment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="patient_payments", verbose_name="Patient")
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        null=True, choices=status, max_length=200, verbose_name="Status Of Payment")
    paymentType = models.CharField(
        choices=PAYMENT_TYPES,default="Consulting", max_length=1,  verbose_name="Type Of payment")
    paymentMethod = models.CharField(null=True, max_length=200, verbose_name="Method Of Payment")
    medaid = models.CharField(
        null=True, max_length=200,default='None')

    ecoNumber = models.CharField(
        null=True, max_length=200, verbose_name="Ecocash number",default='None')
    total = models.IntegerField(null=True)
  
    class Meta:
        ordering = ('-id',)  # unique identifier

    def __str__(self):
        # declaring an object
        return "Patient-{} status-{}".format(self.patient, self.status)

      
    


  


 


    
