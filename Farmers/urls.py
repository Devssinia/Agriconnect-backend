from django.urls import path
import Farmers.views as farmerViews

urlpatterns = [
    path('', farmerViews.farmers),
    path('farmers_by_pk/<int:pk>/',farmerViews.farmers_by_pk ),
    path('insert_farmers_one/',farmerViews.insert_farmers_one),
    path('update_farmers_by_pk/<int:pk>/',farmerViews.update_farmers_by_pk),
    path('delete_farmers_by_pk/<int:pk>/',farmerViews.delete_farmers_by_pk),
]



