from django.contrib import admin

from edliz.apps import EdlizConfig
from .models import *
from.models import Edliz
from import_export.admin import ImportExportModelAdmin



# Register your models here.
@admin.register(Edliz)
class EdlizAdmin(ImportExportModelAdmin):
    list_display = ('name_of_drug',)