
from rest_framework import serializers
from Farmers.models import Farmer

# Ad
class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = '__all__'





