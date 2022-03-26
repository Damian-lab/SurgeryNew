from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import *
from appointment import models
# Register your models here.

class AppointmentFilter(admin.ModelAdmin):
    list_filter = ['id','patient']
    search_fields = ['id','patient']

class PrescriptionFilter(admin.ModelAdmin):
    list_filter = ['id','patient']
    search_fields = ['id','patient',]

class PaymentFilter(admin.ModelAdmin):
    list_filter = ['id','paymentType','paymentMethod']
    search_fields = ['id','paymentType','paymentMethod']

admin.site.register(models.Appointment,AppointmentFilter)
admin.site.register(models.Prescription,PrescriptionFilter)
admin.site.register(models.Payment,PaymentFilter)

