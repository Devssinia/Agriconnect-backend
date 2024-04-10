from django.urls import path
import Orders.views as orderViews

urlpatterns = [
    # URLs for Order model
    path('', orderViews.orders, name='orders'),
    path('order_by_pk/<int:pk>/', orderViews.order_by_pk, name='order_by_pk'),
    path('insert_order_one/', orderViews.insert_order_one, name='insert_order_one'),
    path('delete_order_by_pk/<int:pk>/', orderViews.delete_order_by_pk, name='delete_order_by_pk'),
    path('update_order_by_pk/<int:pk>/', orderViews.update_order_by_pk, name='update_order_by_pk'),
    path('insert_multiple_orders/', orderViews.insert_multiple_orders, name='insert_multiple_orders'),
    
    # URLs for OrderProducts model
    path('order-products/', orderViews.order_products, name='order_products'),
    path('order-products/order_products_by_pk/<int:pk>/', orderViews.order_products_by_pk, name='order_products_by_pk'),
    path('order-products/insert_order_product_one/', orderViews.insert_order_product_one, name='insert_order_product_one'),
    path('order-products/delete_order_product_by_pk/<int:pk>/', orderViews.delete_order_product_by_pk, name='delete_order_product_by_pk'),
    path('order-products/update_order_product_by_pk/<int:pk>/', orderViews.update_order_product_by_pk, name='update_order_product_by_pk'),
    path('order-products/insert_multiple_order_products/', orderViews.insert_multiple_order_products, name='insert_multiple_order_products'),
    
    # URLs for Transactions model
    path('transactions/', orderViews.transactions, name='transactions'),
    path('transaction/transaction_by_pk/<int:pk>/', orderViews.transaction_by_pk, name='transaction_by_pk'),
    path('transactions/insert_transaction_one/', orderViews.insert_transaction_one, name='insert_transaction_one'),
    path('transactions/delete_transaction_by_pk/<int:pk>/', orderViews.delete_transaction_by_pk, name='delete_transaction_by_pk'),
    path('transactions/update_transaction_by_pk/<int:pk>/', orderViews.update_transaction_by_pk, name='update_transaction_by_pk'),
    path('transactions/insert_multiple_transactions/', orderViews.insert_multiple_transactions, name='insert_multiple_transactions'),
]
