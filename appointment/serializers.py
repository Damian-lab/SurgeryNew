from rest_framework.serializers import ModelSerializer
from appointment.models import Appointment

class AppointmentMethodSerializer(ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"



