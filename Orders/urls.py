from django.urls import path
import crud as crudApi
urlpatterns = [
    path('',crudApi.retrieve_object_by_pk),
    path('insert_objects_one/',crudApi.insert_objects_one),
    path('retrieve_object_by_pk/<int:pk>/',crudApi.retrieve_object_by_pk),
    path('delete_users_by_pk/<int:pk>/',crudApi.delete_object_by_pk),
    path('update_users_by_pk/<int:pk>/',crudApi.update_object_by_pk),
]
