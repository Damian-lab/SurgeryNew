from django.contrib import admin
from django.urls import path,include
from medaid import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pay-medaid',views.MedAidViewset)


app_name = "medaid"
urlpatterns = [
    path('api/', include(router.urls)),
    path("medaid", views.medaid_names, name="medaid_names"),
    path("",views.MedAidCreateView,name="view-medaid"),

  
  
]
