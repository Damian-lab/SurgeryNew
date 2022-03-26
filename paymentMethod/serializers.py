from rest_framework.serializers import ModelSerializer
from paymentMethod.models import PaymentMethod

class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model=PaymentMethod
        fields="__all__"
 