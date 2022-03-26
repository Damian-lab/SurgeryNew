from django.shortcuts import render

from icd10.forms import Icd10Form
from .models import Icd10
from .resources import Icd10Resource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from math import ceil
from re import L
import django
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View


from .models import *

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from user_profile.models import UserProfile
from django.template.loader import render_to_string
from django.http import JsonResponse, request
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
from django.conf import settings
from django.contrib.staticfiles import finders
from django.template.context_processors import csrf


# Create your views here.
def simple_upload(request):
    if request.method == "POST":
        icd10_resource = Icd10Resource()
        dataset = Dataset()
        new_icd10 = request.FILES['myfile']

        if not new_icd10.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, "upload.html")

        imported_data = dataset.load(new_icd10.read(), format="xlsx")
        for data in imported_data:
            value = Icd10(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],

            )

            value.save()
    return render(request, "upload.html")


def Icd10CreateView(request):
    if request.method == 'POST':
        employee_form = Icd10Form(request.POST)
        if employee_form.is_valid():
            form = employee_form.save(commit=False)

            form.save()
            return redirect('icd10:my-filter')

    else:
        employee_form = Icd10Form()
        args = {}
    args.update(csrf(request))
    args['employee_form'] = employee_form
    return render(request, "icd10/my_file.html", args)

@login_required(login_url='/login/')
def myIcd10CreateView(request):
    if request.method == 'POST':

        form = Icd10Form(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)

            appointment.save()

            return redirect('appointment:receptionist_app')

    else:

        form = Icd10Form()
        return render(request, 'appointment/prescription_create.html', {'form': form})


# def Icd10View(request):
#     if request.method == 'POST':

#         return redirect('autocomplete')

#     else:

#       return render(request, "appointment/ajax.html")


