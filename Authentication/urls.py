from django.http import HttpResponse
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from Authentication import views


urlpatterns = [
     path("",views.Good.as_view(),),
     path('login/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='get_token'),
     path('refresh_token/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
     path("logout/", views.LogoutView.as_view(),),
     path("change_password/", views.ChangePasswordView.as_view(),)
]