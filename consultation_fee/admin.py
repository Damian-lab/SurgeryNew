from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import *
#from the app name,import models
from consultation_fee import models
# Register your models here.




class ConsultationFeeFilter(admin.ModelAdmin):
    list_filter = ['id','fee']
    search_fields = ['id','fee']
admin.site.register(models.ConsultationFee,ConsultationFeeFilter)

