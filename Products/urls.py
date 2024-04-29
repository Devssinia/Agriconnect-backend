from django.urls import path
import Products.views as productViews
import crud as crudApi
urlpatterns = [
    # path('',crudApi.retrieve_object_by_pk),
    # path('insert_objects_one/',crudApi.insert_objects_one),
    # path('retrieve_object_by_pk/<int:pk>/',crudApi.retrieve_object_by_pk),
    # path('delete_users_by_pk/<int:pk>/',crudApi.delete_object_by_pk),
    # path('update_users_by_pk/<int:pk>/',crudApi.update_object_by_pk),
    
    path('', productViews.products, name='products'),
    path('farmerproducts', productViews.farmers_with_products, name='products_and_farmers'),
    path('product_by_pk/<int:pk>/', productViews.products_by_pk, name='product_by_pk'),
    path('insert_product_one/', productViews.insert_product_one, name='insert_product_one'),
    path('delete_product_by_pk/<int:pk>/', productViews.delete_product_by_pk, name='delete_product_by_pk'),
    path('update_product_by_pk/<int:pk>/', productViews.update_product_by_pk, name='update_product_by_pk'),
    path('insert_multiple_products/', productViews.insert_multiple_products, name='insert_multiple_products'),


    path('uoms/', productViews.uoms),
    path('uoms/insert_uoms_one/', productViews.insert_uoms_one),
    path('categories/', productViews.categories, name='insert_multiple_products'),
    path('/categories/insert_categories_one', productViews.insert_categories_one),



]
