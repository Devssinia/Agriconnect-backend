from django.db import models



class UOMs(models.Model):
    name = models.CharField(max_length=255)


class Categories(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    uom = models.ForeignKey(UOMs, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    last_added  = models.DateField(null=True)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    location_longtude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    image1 = models.ImageField(upload_to='uploads/products')
    image2 = models.ImageField(upload_to='uploads/products')
    image3 = models.ImageField(upload_to='uploads/products')
    product_description = models.CharField(null=True,max_length=255)
