import logging
from math import ceil
from multiprocessing import context
from re import L
from this import d
from unicodedata import name
from urllib import response
import django
from django.forms import CharField
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http import Http404, JsonResponse
import appointment
from appointment.serializers import AppointmentMethodSerializer
from edliz.models import Edliz
from paymentMethod.models import PaymentMethod
import user_profile
from .models import *
from .forms import *
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
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
import datetime


# from django.urls import re_path
# from .views import add_drug
# Create your views here.


class AppointmentsForAPatientView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)


class AppointmentsForADoctorView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user)


class PaymentListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Payment.objects.filter(patient=self.request.user)


class MedicalHistoryView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Prescription.objects.filter(patient=self.request.user)


class PrescriptionListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Prescription.objects.filter(doctor=self.request.user)


class AppointmentListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        date_days_before = datetime.datetime.now() + datetime.timedelta(days=2)
        return Appointment.objects.filter(doctor=self.request.user, status='Pending').all()
# doctor=self.request.user,


class RdashboardListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user)

#Function to create a bootstrapform
@login_required(login_url='/login/')
def PrescriptionCreateView(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)

        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user

            prescription.save()
        return redirect('appointment:doc-prescriptions')

    else:
        form = PrescriptionForm()

    return render(request, 'appointment/prescription_create.html', {'form': form})

def get_related_id(request):
    patient = request.GET.get('patient',None)
    data = {'NatID':Prescription.objects.get(patient=CharField(patient)).NatID.NatID}
    return JsonResponse(data)

#Jquery Function to create prescription
@login_required(login_url='/login/')
def PrescriptionViewJquery(request):
    if request.method == 'POST':
        prescription_form = PrescriptionForm(request.POST)
        if prescription_form.is_valid():
            prescription = prescription_form.save(commit=False)
            prescription.receptionist = request.user
            prescription.save()

            return redirect('appointment:doc-prescriptions')

     

    else:
        prescription_form = PrescriptionForm()

        args = {}
    args.update(csrf(request))
    args['prescription_form'] = prescription_form

  

    return render(request, "appointment/prescription_create.html", args)



@login_required(login_url='/login/')
def AppointmentCreateView(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)
            # appointment.doctor = request.user

            appointment.save()
            return redirect('appointment:doctor_app')

    else:

        form = AppointmentForm()
        return render(request, 'appointment/appointment_create.html', {'form': form})


@login_required(login_url='/login/')
def DocAppointmentCreateView(request):
    if request.method == 'POST':

        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)

            appointment.save()

            return redirect('appointment:receptionist_app')

    else:

        form = AppointmentForm()
        return render(request, 'appointment/appointment_create.html', {'form': form})


@login_required(login_url='/login/')
def PaymentCreateView(request):
    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save(commit=False)
            payment.receptionist = request.user
            payment.save()

            return redirect('appointment:bill_payments')

     

    else:
        payment_form = PaymentForm()

        args = {}
    args.update(csrf(request))
    args['payment_form'] = payment_form

    # rate_values = PaymentMethod.rate
    # args['rate_values'] = rate_values

    return render(request, "appointment/payment_create.html", args)


@login_required(login_url='/login/')
def rdashboard(request):
    if request.method == "GET" and request.user.user_type == "R":
        context = {
            "totalApp": len(Appointment.objects.all()),
            "compApp": len(Appointment.objects.filter(status="Completed")),
            "pendApp": len(Appointment.objects.filter(status="Pending")),
            "app_list": Appointment.objects.all()[:5],
            # "pat_list" : UserProfile.objects.filter(user__user_type="P")[:5],
            # "pay_list" : Payment.objects.all()[:5]
        }
        return render(request, 'appointment/r_dashboard.html', context=context)


@login_required(login_url='/login/')
def bills(request):

    if request.method == "GET":
        context = {
            "pay_list": Payment.objects.all(),
        }
    return render(request, 'appointment/payment_list.html', context=context)


@login_required(login_url='/login/')
def doctorappointment(request):
    if request.method == "GET" and request.user.user_type == "D":
        context = {

            "app_list": Appointment.objects.filter(doctor=request.user)[:5],
        }
    return render(request, 'appointment/appointed_doc.html', context=context)


@login_required(login_url='/login/')
def receptionistappointment(request):
    if request.method == "GET" and request.user.user_type == "R":
        date_days_before = datetime.datetime.now() + datetime.timedelta(days=1)
        # return Appointment.objects.filter(doctor=self.request.user, status='Pending').all()
        context = {
            "app_list": Appointment.objects.filter(status='Pending', date=date_days_before).all(),
        }
    return render(request, 'appointment/receptionist_app.html', context=context)

#view to print pdf for patient prescriptions
@login_required(login_url='/login/')
def prescription_details(request):
    if request.method == "GET" and request.user.user_type == "D":
       
       
        context = {
            "pres_list": Prescription.objects.filter(doctor=request.user).all(),
        }
    return render(request, 'appointment/my_trial.html', context=context)
# searching patient


def search_patients(request):
    if request.method == "POST":
        searched = request.POST['searched']
        patPrescription = Prescription.objects.filter(
            NatID__icontains=searched)

        return render(request,
                      'appointment/search_patients.html',
                      {'searched': searched,
                       'patPrescription': patPrescription})
    else:
        return render(request,
                      'appointment/search_patients.html',
                      {})


# searching profile


def search_profile(request):
    if request.method == "POST":
        searched = request.POST['searched']
        patProfile = UserProfile.objects.filter(name__icontains=searched)

        return render(request,
                      'appointment/search_profile.html',
                      {'searched': searched,
                       'patProfile': patProfile})
    else:
        return render(request,
                      'appointment/search_profile.html',
                      {})

# searching appointment


def search_appointment(request):
    if request.method == "POST":
        searched = request.POST['searched']
        patAppointment = Appointment.objects.filter(status__icontains=searched)

        return render(request,
                      'appointment/search_appointment.html',
                      {'searched': searched,
                       'patAppointment': patAppointment})
    else:
        return render(request,
                      'appointment/search_appointment.html',
                      {})
# searching payment


def search_payment(request):
    if request.method == "POST":
        searched = request.POST['searched']
        patPayment = Payment.objects.filter(paymentMethod__icontains=searched)

        return render(request,
                      'appointment/search_payment.html',
                      {'searched': searched,
                       'patPayment': patPayment})
    else:
        return render(request,
                      'appointment/search_payment.html',
                      {})


# querying an appointment


@login_required(login_url='/login/')
def AppointmentPk(request, pk):

    app = Appointment.objects.get(pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect('appointment:r_dashboard')
    else:
        form = AppointmentForm(instance=app)
    return render(request, 'appointment/appointment_review.html', {'form': form, 'appointment': appointment})

# querying payment


@login_required(login_url='/login/')
def PaymentPk(request, pk):

    pay = Payment.objects.get(pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=pay)
        if form.is_valid():
            form.save()
            return redirect('appointment:r_dashboard')
    else:
        form = PaymentForm(instance=pay)
    return render(request, 'appointment/appointment_review.html', {'form': form, 'appointment': appointment})


@login_required(login_url='/login/')
def patientView(request):
    if request.method == "GET":
        context = {


        }
    return render(request, 'appointment/patient_prescription.html', context=context)

# Code to generate pdf from info in dB


class MyPdfListView(ListView):
    model = Prescription
    #model = Appointment
    template_name = 'appointment/search_patients.html'


def my_pdf_view(request, *args, **kwargs):

    pk = kwargs.get('pk')
    mypdf = get_object_or_404(Prescription, pk=pk)
    template_path = 'appointment/my_pdf.html'
    context = {'mypdf': mypdf}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if downloads:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def prescription_pdf(request, *args, **kwargs):

    pk = kwargs.get('pk')
    prescription_value = get_object_or_404(Prescription, pk=pk)
    template_path = 'appointment/my_trial.html'
    context = {'prescription_value': prescription_value}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if downloads:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


@login_required(login_url='/login/')
def myPatient(request):

    if request.method == "GET" and request.user.user_type == "D":
        context = {

            "pat_list": UserProfile.objects.filter(user__user_type="P")[:5],
        }
    return render(request, 'user_profile/patient_list.html', context=context)


def index(request):
    # get presc_cost value from db
    presc_cost = 10

    if request.method == 'POST':
        payment_form = PaymentForm(request.POST)  # saving the instance

        if payment_form.is_valid():
            form = payment_form.save()
            return redirect('bill_payments')

    else:
        payment_form = PaymentForm()
    args = {}
    args.update(csrf(request))
    args['payment_form'] = payment_form
    args['presc_cost'] = presc_cost

    return render(request, "index.html", args)
#function to autocomplete drug
def autocomplete_drug(request):
    if 'term' in request.GET:
        qs = Edliz.objects.filter(
            name_of_drug__icontains=request.GET.get('term'))
        titles = list()
        for edliz in qs:
            titles.append(edliz.name_of_drug)

        return JsonResponse(titles, safe=False)







#function to do autocomplete
def autocomplete(request):
    if 'term' in request.GET:
        qs = Icd10.objects.filter(
            icd10_code__icontains=request.GET.get('term'))
        titles = list()
        for icd10 in qs:
            titles.append(icd10.icd10_code)

        return JsonResponse(titles, safe=False)
    # return render(request, 'appointment/prescription_create.html')#there was ajax.html

#function to autocomplete user/patient profile name
def autocomplete_name_of_patient(request):
    if 'term' in request.GET:
        qs = UserProfile.objects.filter(
            name__icontains=request.GET.get('term'))
        titles = list()
        for user_profile in qs:
            titles.append(user_profile.name)

        return JsonResponse(titles, safe=False)



def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    # , link_callback=fetch_resources)
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None







    
def getApproachingAppointments():
    '''
        get all app. wth status==pending and 1 days before
    '''
    date_days_before = datetime.datetime.now() + datetime.timedelta(days=1)

    queryset = Appointment.objects.filter(
        date=date_days_before, status='Pending').all()
    
    patient_numbers = []

    patients = []

    # loop thru whole list and get patient record > phone number > append to a list
    for record in queryset:
        patient = UserProfile.objects.filter(user__user_type="P", user__username=record.patient).first()
        patient_numbers.append(patient.phone)
        patients.append(patient)
        
      
    

    return patients

    