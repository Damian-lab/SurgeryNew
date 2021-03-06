from django.shortcuts import render, redirect

from user_profile.serializers import UserMethodSerializer


#from appointment.views import getApproachingAppointments
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
import string
import random
from django.template.context_processors import csrf
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
import datetime

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your views here.
#@login_required is a decorator that checks if the user is logged in
@login_required(login_url='/login/')
def CreateUserProfile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # try:
            password = User.objects.make_random_password()
            username = profile.name.split()[0] + id_generator()
            user = User.objects.create(username=username, user_type="P")
            user.set_password(password)
            user.save_base(raw=True)
            profile.user = user
            profile.save()
            return redirect('appointment:r_dashboard')
         
          
    else:
        form = ProfileUpdateForm()
    return render(request, 'user_profile/profile_create.html', {'form': form})


@login_required(login_url='/login/')
def UpdatedUserProfile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile:profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'user_profile/profile.html', {'form': form, 'user':user})


@login_required(login_url='/login/')
def UpdatedUserProfilePk(request, pk):
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('appointment:r_dashboard')
    else:
        form = ProfileUpdateForm(instance=profile)
    return render(request, 'user_profile/profile.html', {'form': form, 'user':user})


@login_required(login_url='/login/')
def UpdatedDocProfilePk(request, pk):
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('appointment:hr_dashboard')
    else:
        form = DoctorProfileForm(instance=profile)
    return render(request, 'user_profile/profile.html', {'form': form, 'user':user})


@login_required(login_url='/login/')
def DeleteUserProfilePk(request, pk):
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        user.delete()
        return redirect('appointment:r_dashboard')
    else:
        return render(request, 'user_profile/profile_delete.html', {'user':user})


@login_required(login_url='/login/')
def DeleteDocProfilePk(request, pk):
    print("hello")
    user = User.objects.get(pk=pk)
    profile = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        user.delete()
        return redirect('appointment:hr_dashboard')
    else:
        return render(request, 'user_profile/profile_doc_delete.html', {'user':user})

@login_required(login_url='/login/')
def myPatient(request):

    if request.method == "GET" and request.user.user_type == "R":
        context = {
            "pat_list" : UserProfile.objects.filter(user__user_type="P")[:5],
            }
    return render(request, 'user_profile/patient_list.html', context=context)

@login_required(login_url='/login/')
def UserCreateView(request):
    if request.method == 'POST':
        user_form = ProfileUpdateForm(request.POST)
        if user_form.is_valid():
               profile = user_form.save(commit=False)
            # try:
               password = User.objects.make_random_password()
               username = profile.name.split()[0] + id_generator()
               user = User.objects.create(username=username, user_type="P")
               user.set_password(password)
               user.save_base(raw=True)
               profile.user = user
               profile.save()

               return redirect('appointment:r_dashboard')

     

    else:
        user_form = ProfileUpdateForm()

        args = {}
    args.update(csrf(request))
    args['user_form'] = user_form

  

    return render(request, "user_profile/profile_create.html", args)


class UserMethodViewset(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class =UserMethodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['NatID',]