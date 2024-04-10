from rest_framework import serializers
from .models import OrderProducts, Transactions, Order

class OrderProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProducts
        fields = '__all__'

class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
