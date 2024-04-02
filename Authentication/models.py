from django.db import models
from Users.models import CustomUser

# Create your models here.
class VerificationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        # Implement your logic to check if the code is still valid (e.g., not expired)
        return True