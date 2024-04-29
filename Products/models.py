from django.db import models



class UOMs(models.Model):
    name = models.CharField(max_length=255)


class Categories(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    product_description = models.CharField(null=True,max_length=255)
