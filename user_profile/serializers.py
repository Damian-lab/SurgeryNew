import datetime
from rest_framework import serializers
from .models import Post, UserProfile
from user_profile.forms import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_age(self, instance):
        return datetime.datetime.now().year - instance.dob.year