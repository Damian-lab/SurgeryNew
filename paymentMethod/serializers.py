from rest_framework.serializers import ModelSerializer
from consultation_fee.models import ConsultationFee
from paymentMethod.models import PaymentMethod

class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model=PaymentMethod
        fields="__all__"
class ConsultSerializer(ModelSerializer):
    class Meta:
        model=ConsultationFee
        fields="__all__"
        