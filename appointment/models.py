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
shortfall_payment_method = [
    ('ZWL', "ZWL"),
    ('RTGS', "RTGS"),
    ('ZAR', "ZAR"),
    ('USD', "USD"),
    ('None','None'),
   
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
    Bp = models.IntegerField()
    Pulse = models.IntegerField(null=True)
    Temp = models.FloatField(null=True)
    Weight = models.IntegerField(null=True)
    SP02 = models.FloatField(null=True)
    notification= models.BooleanField.default=False

# meta and ordering wasnzt there
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Patient - {}  status - {}    - At   - {} " .format(self.patient, self.status, self.date)

    @property
    def appointment_status(self):

        if float(self.Temp )> 37 or float(self.Temp)<35 or int(self.Pulse)>110 or int(self.Pulse)<60 or float(self.SP02)<90 or int(self.Bp)>130 or int(self.Bp)<100:
            status_selected = "Urgent"
            return status_selected#status selected
        else:
            status_selected = "Priority"
            return status_selected



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
    drugs = models.CharField( max_length=100, blank=True, null=True, verbose_name="Drugs")
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

MED_AID = [
    
    ('Minerva',' Minerva'),
    ('PSMI', 'PSMI'),
    ('CIMAS','CIMAS'),
  

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
        choices= MED_AID,null=True, max_length=200)

    ecoNumber = models.CharField(
        null=True, max_length=200, verbose_name="Ecocash number",default='None')
    shortfall = models.IntegerField(null=True,default= 0)
    add_payment = models.CharField(choices= shortfall_payment_method, null=True,max_length=200, verbose_name="Add Payment")
    total = models.IntegerField(null=True)
    
  
    class Meta:
        ordering = ('-id',)  # unique identifier

    def __str__(self):
        # declaring an object
        return "Patient-{} status-{}".format(self.patient, self.status)

      
    


  


 


    
