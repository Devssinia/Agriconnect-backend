from django.db import models

class PaymentTransaction(models.Model):
      full_name=models.CharField(max_length=255,null=True)
      first_name=models.CharField(max_length=255,null=True)
      last_name=models.CharField(max_length=255,null=True)
      email=models.EmailField(max_length=255,null=True)
      currency=models.CharField(max_length=255,null=False,default="ETB")
      amount=models.DecimalField(max_digits=9, decimal_places=6,null=False,default=0)
      phone_no=models.CharField(max_length=255,null=True)
      charge=models.CharField(max_length=255,null=True)
      mode=models.CharField(max_length=255,null=True)
      method=models.CharField(max_length=255,null=True)
      type=models.CharField(max_length=255,null=True)
      status=models.CharField(max_length=255,null=False,default="pending" )
      tx_ref=models.CharField(max_length=255,null=False)
      checkout_url=models.URLField(max_length=255,null=True)
      created_at=models.DateTimeField(auto_now_add=True,null=True)
      updated_at=models.DateTimeField(auto_now_add=True,null=True)
      


      
      
    
    