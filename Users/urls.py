from django.urls import path
import Users.views as  userViews
urlpatterns = [
    path('',userViews.users),
    path('register/',userViews.register),
    path('insert_users_one/',userViews.insert_users_one),
    path('users_by_pk/<int:pk>/',userViews.users_by_pk),
    path('delete_users_by_pk/<int:pk>/',userViews.delete_users_by_pk),
    path('update_users_by_pk/<int:pk>/',userViews.update_users_by_pk),
    path('register/', userViews.UserViewSet.as_view({'post': 'create'}), name='register'),
]
