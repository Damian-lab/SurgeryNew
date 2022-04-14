from django.conf.urls import url                                                                                                                                                         
from . import views

app_name = "broadcast"
urlpatterns = [ 
   # url(r'broadcast$', views.broadcast_sms, name="default"),
    url(r'broadcast$', views.working_sms, name="default"),
]