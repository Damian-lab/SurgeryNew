from django.contrib import admin
from django.urls import path,include
from paymentMethod import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'payment-methods',views.PaymentMethodViewset)
router.register(r'consultation-fee',views.ConsultationFeeViewset)

app_name = "paymentMethod"
urlpatterns = [
    path('api/', include(router.urls)),
    path("paymentMethod/", views.payment_rates, name="payment_method"),
    path("",views.PaymentMethodCreateView,name="pay-rate"),

  
  
]
