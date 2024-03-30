from django.db import models

from Users.models import CustomUser
from Products.models import Prodcuts, UOMs


class Farmers(models.Model):
    full_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=20)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_name = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=255)
    agent_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    
class FarmerProducts(models.Model):
    farmer_id = models.ForeignKey(Farmers, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Prodcuts, on_delete=models.SET_NULL, null=True)
    uom = models.ForeignKey(UOMs, on_delete=models.SET_NULL, null=True)
    rate = models.DecimalField(max_digits=9, decimal_places=6)