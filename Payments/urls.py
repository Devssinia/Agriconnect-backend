from django.urls import path
from . import views

urlpatterns = [
    path('', views.accept_payment),
    path('verify/', views.verifyPayment)
]