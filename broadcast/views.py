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
    message_to_broadcast = ("Your appointment scheduled with Damian's Surgery is ready tomorrow!")
    client = Client("AC25fe8e2dc16ea5d862c3e6d2d9470f63", "783ed8bb8d1eac7fb15b9ae87cb68085")
    for recipient in getApproachingAppointments():
        if recipient:
            client.messages.create(to=recipient,
                                   from_="+19123781433",
                                   body=message_to_broadcast)
    return HttpResponse("messages sent to patient!", 200)

def working_sms(request):
  
    scheduler= BackgroundScheduler()
    scheduler.add_job(broadcast_sms,'interval',seconds=5)
    scheduler.start()
    Appointment.notification = True
  

