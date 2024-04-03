from datetime import datetime, timedelta
import random
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator, validate_email
from django.conf import settings




class CustomUserManager(BaseUserManager):
    def create_user(self, phone_no, full_name=None, password=None, **extra_fields):
        if not phone_no:
            raise ValueError(_('The phone number must be set'))
        
        user = self.model(phone_no=phone_no, username=phone_no, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_no, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(phone_no, password, **extra_fields)

class Role(models.Model):
    role_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.role_name
    
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255,null=True)
    phone_no = models.CharField(max_length=20, unique=True)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    location_name = models.CharField(max_length=255,null=True)
    profile_image = models.CharField(max_length=255,null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE,null=True)

    otp = models.CharField(max_length=6, null=True)
    otp_expiry = models.DateTimeField(blank=True, null=True)
    max_otp_try = models.CharField(max_length=2, default=settings.MAX_OTP_TRY)
    otp_max_out = models.DateTimeField(blank=True, null=True)
    
    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()  # Set the custom manager here


    # Specify custom related_names to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return self.phone_no
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.phone_no
        super().save(*args, **kwargs)


