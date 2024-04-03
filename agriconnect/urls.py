
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('',include("Authentication.urls")),
    path('users/', include('Users.urls')),
    # path('farmers/', include('Farmers.urls')),
]
