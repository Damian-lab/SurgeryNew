from rest_framework.serializers import ModelSerializer
from appointment.models import Appointment
from appointment import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Appointment
from appointment.forms import Appointment


class AppointmentMethodSerializer(ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    appointment_status = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = '__all__'

 





class UserMethodSerializer(ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"
        
