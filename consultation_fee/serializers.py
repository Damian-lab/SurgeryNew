from rest_framework.serializers import ModelSerializer
from consultation_fee.models import ConsultationFee

class ConsultationFeeSerializer(ModelSerializer):
    class Meta:
        model=ConsultationFee
        fields="__all__"
 