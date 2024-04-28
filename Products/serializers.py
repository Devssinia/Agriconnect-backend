from rest_framework import serializers
from Farmers.models import Farmer, FarmerProducts
from Products.models import Categories, Product, UOMs


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class FarmerSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(source='farmerproducts_set',many=True)
    class Meta:
        model = Farmer
        fields = '__all__'


class FarmerProductsSerializer(serializers.ModelSerializer):
    farmer_id = serializers.PrimaryKeyRelatedField(source='farmer', queryset=Farmer.objects.all())
    product_id = serializers.PrimaryKeyRelatedField(source='product', queryset=Product.objects.all())

    class Meta:
        model = FarmerProducts
        fields = ['id', 'rate', 'farmer_id', 'product_id', 'uom']


        
