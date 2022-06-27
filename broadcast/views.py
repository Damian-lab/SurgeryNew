import datetime
from django.conf import settings                                                                                                                                                       
from django.http import HttpResponse
from twilio.rest import Client
from apscheduler.schedulers.background import BackgroundScheduler
from appointment.models import Appointment
# from hospital.settings import SMS_BROADCAST_TO_NUMBERS
from user_profile.models import UserProfile

def getApproachingAppointments():
    '''
        get all app. wth status==pending and 2 days before
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
        
      
    

    return patient_numbers
def broadcast_sms():
    message_to_broadcast = ("Your appointment scheduled with the surgery is on tomorrow!")
    client = Client("AC4ca11b35c9c491bc720dfcced11beb64", "9d56639677aab59c8a38d6eda8fe587e")
    for recipient in getApproachingAppointments():
        if recipient:
            client.messages.create(to=recipient,
                                   from_="+18504937780",
                                   body=message_to_broadcast)
    return HttpResponse("messages sent to patient!", 200)

def working_sms(request):
  
    scheduler= BackgroundScheduler()
    scheduler.add_job(broadcast_sms,'interval',seconds=20)
    scheduler.start()
    Appointment.notification = True
    return HttpResponse("messages sent to patient!", 200)

