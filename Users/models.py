from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.contrib.auth import get_user_model


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_no, full_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone_no:
            raise ValueError('Users must have a phone')

        user = self.model(
            phone_no=phone_no,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, phone_no, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            phone_no,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_no, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone_no,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Role(models.Model):
    role_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.role_name
    
class CustomUser(AbstractUser):
    username = None
    
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


    def __str__(self):
        return self.phone_no
    
   

