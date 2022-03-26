
from django.shortcuts import redirect, render
import paymentMethod
from django.contrib.auth.mixins import LoginRequiredMixin
from paymentMethod.forms import PaymentMethodForm
from paymentMethod.models import PaymentMethod
from django.contrib.auth.decorators import login_required
import user_profile
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.viewsets import ModelViewSet
from paymentMethod.serializers import PaymentMethodSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.





def PaymentMethodCreateView(request):
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
      
        if form.is_valid():
            paymentMethod = form.save(commit=False)
         
          
            paymentMethod.save()
            return redirect('paymentMethod:payment-method')

    else:

        form = PaymentMethodForm()
        return render(request, 'paymentMethod/paymentMethod_create.html', {'form': form})

def payment_rates(request):

    if request.method == "GET":
        context = {
            "rates_list": PaymentMethod.objects.all(),
        }
    return render(request, 'paymentMethod/surgery_rates.html', context=context)


#endpoint
class PaymentMethodViewset(ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class =PaymentMethodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['currency_name',]

