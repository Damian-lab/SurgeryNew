from django.shortcuts import render

from edliz.forms import EdlizForm
from .models import Edliz
from .resources import EdlizResource
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
        edliz_resource = EdlizResource()
        dataset = Dataset()
        new_edliz = request.FILES['myfile']

        if not new_edliz.name.endswith('xlsx'):
            messages.info(request, 'wrong format')
            return render(request, "upload.html")

        imported_data = dataset.load(new_edliz.read(), format="xlsx")
        for data in imported_data:
            value = Edliz(
                data[0],
                data[1],
             

            )

            value.save()
    return render(request, "upload.html")


def EdlizCreateView(request):
    if request.method == 'POST':
        edliz_form = EdlizForm(request.POST)
        if edliz_form.is_valid():
            form = edliz_form.save(commit=False)

            form.save()
            return redirect('edliz:my-filter')

    else:
        edliz_form = EdlizForm()
        args = {}
    args.update(csrf(request))
    args['edliz_form'] = edliz_form
    return render(request, "edliz/my_file.html", args)

@login_required(login_url='/login/')
def myEdlizCreateView(request):
    if request.method == 'POST':

        form = EdlizForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)

            appointment.save()

            return redirect('appointment:receptionist_app')

    else:

        form = EdlizForm()
        return render(request, 'appointment/prescription_create.html', {'form': form})


