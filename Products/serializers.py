
from rest_framework import serializers
from Products.models import Product

# Ad
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'





