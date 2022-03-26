from django.contrib import admin
from django.urls import path
from icd10 import views

app_name = "icd10"
urlpatterns = [
    path('admin/',admin.site.urls),
    path('icd10',views.simple_upload,name="simple-upload"),
    path('icd10', views.Icd10CreateView, name="my-filter"),
  
]
