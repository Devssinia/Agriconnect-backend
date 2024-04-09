
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('',include("Authentication.urls")),
    path("admin/", admin.site.urls),
    path('users/', include('Users.urls')),
    path('farmers/', include('Farmers.urls')),
    path('payments/', include('Payments.urls')),
    path('orders/', include('Orders.urls')),
    path('products/', include('Products.urls')),
]
