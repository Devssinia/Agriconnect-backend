from django.urls import path
import Products.views as farmerViews

urlpatterns = [
    path('', farmerViews.products, name='products'),
    path('product_by_pk/<int:pk>/', farmerViews.products_by_pk, name='product_by_pk'),
    path('insert_product_one/', farmerViews.insert_product_one, name='insert_product_one'),
    path('delete_product_by_pk/<int:pk>/', farmerViews.delete_product_by_pk, name='delete_product_by_pk'),
    path('update_product_by_pk/<int:pk>/', farmerViews.update_product_by_pk, name='update_product_by_pk'),
    path('insert_multiple_products/', farmerViews.insert_multiple_products, name='insert_multiple_products'),
]
