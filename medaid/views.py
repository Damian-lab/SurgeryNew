
from django.shortcuts import redirect, render
import medaid
from django.contrib.auth.mixins import LoginRequiredMixin
from medaid.forms import MedAidForm
from medaid.models import MedAid
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.viewsets import ModelViewSet
from medaid.serializers import MedAidSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.





def MedAidCreateView(request):
    if request.method == 'POST':
        form = MedAidForm(request.POST)
      
        if form.is_valid():
            medaid = form.save(commit=False)
         
          
            medaid.save()
            return redirect('medaid:pay-medaid')

    else:

        form = MedAidForm()
        return render(request, 'medaid/medaid_create.html', {'form': form})

def medaid_names(request):

    if request.method == "GET":
        context = {
            "medaid_list": MedAid.objects.all(),
        }
    return render(request, 'medaid/medaid_names.html', context=context)


#endpoint
class MedAidViewset(ModelViewSet):
    queryset = MedAid.objects.all()
    serializer_class =MedAidSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['medaid_name',]

