from django.contrib import admin
from django.urls import path,include
from paymentMethod import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'consutation-fee',views.ConsultationFeeViewset)

app_name = "consultation_fee"
urlpatterns = [
    # path('api/', include(router.urls)),
 
   
]
