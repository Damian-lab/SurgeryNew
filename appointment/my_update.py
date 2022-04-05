# def update_something():
#     print("This function runs every 10 seconds")
import datetime
from appointment.models import Appointment
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
        
      
    

    return patients