from django.db import models

from Users.models import CustomUser
from Products.models import Product, UOMs


class Farmer(models.Model):
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
    farmer_id = models.ForeignKey(Farmer, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    uom = models.ForeignKey(UOMs, on_delete=models.SET_NULL, null=True)
    rate = models.DecimalField(max_digits=9, decimal_places=6)
    quantity = models.DecimalField(max_digits=9, decimal_places=6)
    last_added  = models.DateField(null=True)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    location_longtude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    location_name = models.CharField(max_length=255, default="Unknown")
    image1 = models.CharField(max_length=255, null=True)
    image2 = models.CharField(max_length=255, null=True)
    image3 = models.CharField(max_length=255, null=True)