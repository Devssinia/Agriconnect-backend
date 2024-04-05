from django.db import models

# Create your models here.
class Transaction(models.Model):
      full_name=models.CharField(max_length=255,null=True),
      email=models.EmailField(max_length=255,null=True),
      currency=models.CharField(max_length=255,null=False),
      amount=models.DecimalField(max_digits=9, decimal_places=6,null=False),
      phone_no=models.CharField(max_length=255,null=True)
      charge=models.CharField(max_length=255,null=True),
      mode=models.CharField(max_length=255,null=True),
      type=models.CharField(max_length=255,null=True),
      status=models.CharField(max_length=255,null=True),
      tx_rf=models.CharField(max_length=255,null=False),
      checkout_url=models.URLField(max_length=255,null=True)
      created_at=models.DateTimeField(auto_now_add=True,null=True)
      updated_at=models.DateTimeField(auto_now_add=True,null=True)
      


      
      
    
    