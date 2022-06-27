from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import *
from medaid import models
# Register your models here.




class MedAidFilter(admin.ModelAdmin):
    list_filter = ['id','threshold_amount','medaid_name']
    search_fields = ['id','threshold_amount','medaid_name']
admin.site.register(models.MedAid,MedAidFilter)
