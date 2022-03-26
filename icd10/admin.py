from django.contrib import admin

from icd10.apps import Icd10Config
from .models import *
from.models import Icd10
from import_export.admin import ImportExportModelAdmin



# Register your models here.
@admin.register(Icd10)
class Icd10Admin(ImportExportModelAdmin):
    list_display = ('chapter_description','group_code','group_description','icd10_3_code','icd10_3_code_description','icd10_code','who_full_description')