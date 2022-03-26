from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import *
from paymentMethod import models
# Register your models here.




class PaymentMethodFilter(admin.ModelAdmin):
    list_filter = ['id','rate','currency_name']
    search_fields = ['id','rate','currency_name']
admin.site.register(models.PaymentMethod,PaymentMethodFilter)

