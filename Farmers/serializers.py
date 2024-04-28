from rest_framework import serializers
from .models import Farmer, FarmerProducts
# from Products.serializers import ProductSerializer


class FarmerSerializer(serializers.ModelSerializer):
    # products = ProductSerializer(source='farmerproducts_set', many=True)
    class Meta:
        model = Farmer
        fields = ['id', 'full_name', 'phone_no', 'location_latitude', 'location_longitude', 
                  'location_name', 'profile_image', 'products']


# class FarmerProductsSerializer(serializers.ModelSerializer):
#     uom = serializers.StringRelatedField()

#     class Meta:
#         model = FarmerProducts
#         fields = ['product', 'uom', 'rate']
