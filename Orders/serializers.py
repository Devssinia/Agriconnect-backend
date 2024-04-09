
from rest_framework import serializers
from Orders.models import Order

# Ad
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'





