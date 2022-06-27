from rest_framework.serializers import ModelSerializer
from medaid.models import MedAid

class MedAidSerializer(ModelSerializer):
    class Meta:
        model=MedAid
        fields="__all__"
