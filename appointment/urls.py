from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import  MyPdfListView




app_name = "appointment"

urlpatterns = [
    path("appointments/p/", views.AppointmentsForAPatientView.as_view(), name="patient-appointments"),
    path("appointment", views.PaymentListView.as_view(), name="patient_payment"),
    path("appointment", views.AppointmentsForADoctorView.as_view(), name="doctor-appointments"),
    path("medHistory/", views.MedicalHistoryView.as_view(), name="med-history"),
    path("prescriptions/", views.PrescriptionListView.as_view(), name="doc-prescriptions"),
    path("prescription/create", views.PrescriptionCreateView, name="doc-prescriptions-create"),
    path("appointment", views.AppointmentCreateView, name="appointment-create"),
    path("r_dashboard", views.rdashboard, name="r_dashboard"),
    path("appointment/", views.bills, name="bill_payments"),
    path("createAppointment/", views.receptionistappointment,name="receptionist_app"),
    path("doctorAppointment", views.doctorappointment,name="appointed_doc"),
    path("appointments",views.DocAppointmentCreateView,name="doc-appointments-create"),
    path("appointment",views.AppointmentListView.as_view(),name="doc-appoint"),
    path("payment",views.PaymentCreateView,name="rec-payment"),
    path("search_patients",views.search_patients,name="search-patients"),
    path("search_appointment",views.search_appointment,name="search-appointment"),
    path("search_payment",views.search_payment,name="search-payment"),
    path("search_profile",views.search_profile,name="search-profile"),
    path("ViewPrescription/", views.patientView,name="patient_prescription"),
    path("appointment/<int:pk>/", views.AppointmentPk, name="appointment-pk"),
    path("appointment/<int:pk>/", views.PaymentPk, name="payment-pk"),
    path('appointment', views.MyPdfListView.as_view(),name ='mypdf-list-view'),
    path('appointments/<pk>/',views.my_pdf_view,name ='pdf-view'),
    path("patients", views.myPatient,name="patient_list"),
    path('appointment', views.index, name='index'),
    path('icd10', views.autocomplete, name='autocomplete'),
    
 

    

   
    
]
