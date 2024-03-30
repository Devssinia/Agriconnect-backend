from django.contrib.auth.models import AbstractUser
from django.db import models

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
    REQUIRED_FIELDS = ['full_name']

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
        return self.full_name
