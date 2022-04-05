
from django.shortcuts import redirect, render
import consultation_fee
from django.contrib.auth.mixins import LoginRequiredMixin
from consultation_fee.forms import ConsultationFeeForm
from consultation_fee.models import ConsultationFee
from django.contrib.auth.decorators import login_required
import user_profile
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.viewsets import ModelViewSet
from consultation_fee.serializers import ConsultationFeeSerializer
from django_filters.rest_framework import DjangoFilterBackend


# class ConsultationFeeViewset(ModelViewSet):
#     queryset = ConsultationFee.objects.all()
#     serializer_class =ConsultationFeeSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['fee',]

