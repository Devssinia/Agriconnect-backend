from rest_framework import serializers
from Farmers.models import Farmer, FarmerProducts
from Products.models import Categories, Product, UOMs


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UOMsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOMs
        fields = '__all__'



class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'



        
