from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_no, full_name, password=None, **extra_fields):
        if not phone_no:
            raise ValueError('The phone number must be set')
        user = self.model(phone_no=phone_no, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_no,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_no, password, **extra_fields)

class Role(models.Model):
    role_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.role_name
    
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=20, unique=True)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_name = models.CharField(max_length=255)
    profile_image = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    USERNAME_FIELD = "phone_no"
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


