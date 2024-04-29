from rest_framework import serializers
from .models import Farmer, FarmerProducts
# from Products.serializers import ProductSerializer


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'


class FarmerProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerProducts
        fields = '__all__'
