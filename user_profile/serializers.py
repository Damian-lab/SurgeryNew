import datetime
from rest_framework import serializers
from .models import UserProfile
from user_profile.forms import UserProfile
#recently added
from rest_framework.serializers import ModelSerializer



class UserProfileSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_age(self, instance):
        return datetime.datetime.now().year - instance.dob.year





class UserMethodSerializer(ModelSerializer):
    class Meta:
        model=UserProfile
        fields="__all__"



