from django.db import models

from Farmers.models import FarmerProducts
from Users.models import CustomUser
from Products.models import Categories

class OrderProducts(models.Model):
    farm_product_id = models.ForeignKey(FarmerProducts, on_delete=models.SET_NULL, null=True)
    qty = models.DecimalField(max_digits=9, decimal_places=6)


class Transactions(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    currency= models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=9, decimal_places=6)
    status = models.CharField(max_length=255)

class Orders(models.Model):
    merchant_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    # agent_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    total_amount = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    delivery_duration = models.DecimalField(max_digits=9, decimal_places=6)
    deliver_distance = models.DecimalField(max_digits=9, decimal_places=6)
    is_delivered = models.BooleanField(default=False)
    date_of_delivery = models.DateTimeField()
    expected_delivery_date = models.DateTimeField()
    signiture = models.CharField(max_length=255)
    delivery_address_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    delivery_address_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    delivery_address_name = models.CharField(max_length=255)

