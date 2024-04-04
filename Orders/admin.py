from django.contrib import admin

from Farmers.models import Farmer
from Users.models import CustomUser

# Register your models here.
admin.site.register(Farmer)