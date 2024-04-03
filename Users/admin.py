from django.contrib import admin
from Users.models import Role
from Users.models import CustomUser
# Register your models here.
admin.site.register(Role)
# Register your models here.

admin.site.register(CustomUser)
