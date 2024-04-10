from django.urls import path
import Products.views as farmerViews
import crud as crudApi
urlpatterns = [
    
    path('',crudApi.retrieve_object_by_pk),
    path('insert_objects_one/',crudApi.insert_objects_one),
    path('retrieve_object_by_pk/<int:pk>/',crudApi.retrieve_object_by_pk),
    path('delete_users_by_pk/<int:pk>/',crudApi.delete_object_by_pk),
    path('update_users_by_pk/<int:pk>/',crudApi.update_object_by_pk),
    
    path('', farmerViews.products, name='products'),
    path('product_by_pk/<int:pk>/', farmerViews.products_by_pk, name='product_by_pk'),
    path('insert_product_one/', farmerViews.insert_product_one, name='insert_product_one'),
    path('delete_product_by_pk/<int:pk>/', farmerViews.delete_product_by_pk, name='delete_product_by_pk'),
    path('update_product_by_pk/<int:pk>/', farmerViews.update_product_by_pk, name='update_product_by_pk'),
    path('insert_multiple_products/', farmerViews.insert_multiple_products, name='insert_multiple_products'),
]
