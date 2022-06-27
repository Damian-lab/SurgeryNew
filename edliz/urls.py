from django.contrib import admin
from django.urls import path
from edliz import views

app_name = "edliz"
urlpatterns = [
    path('admin/',admin.site.urls),
    path('edliz',views.simple_upload,name="simple-upload"),
    path('edliz', views.EdlizCreateView, name="my-filter"),
  
]
