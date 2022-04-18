from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user-profile',views.UserMethodViewset)

app_name = "user_profile"

urlpatterns = [
    path('api/', include(router.urls)),
    path("profile/", views.UpdatedUserProfile, name="profile"),
    path("profile/create/", views.CreateUserProfile, name="profile-create"),
    path("create/profile", views.UserCreateView, name="create-profile"),
    path("profile/<int:pk>/", views.UpdatedUserProfilePk, name="profile-pk"),
    path("profile/doc/<int:pk>/", views.UpdatedDocProfilePk, name="doc-profile-pk"),
    path("profile/<int:pk>/delete/", views.DeleteUserProfilePk, name="profile-delete"),
    path("profile/doc/<int:pk>/delete/", views.DeleteDocProfilePk, name="doc-profile-delete"),
    path("patients", views.myPatient,name="patient_list"),
 
]
