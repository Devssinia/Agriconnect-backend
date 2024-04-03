from django.urls import path,include
import Users.views as  userViews



urlpatterns = [
    path('',userViews.users),
    path('create_user_one/',userViews.create_user_one),
    path('get_user_one/<int:pk>/',userViews.get_user_one),
    path('delete_user_one/<int:pk>/',userViews.delete_user_one),
    path('update_user_one/<int:pk>/',userViews.update_user_one)
]
