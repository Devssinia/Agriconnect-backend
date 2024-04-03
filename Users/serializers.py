import random
from rest_framework import serializers
from .models import CustomUser
from datetime import datetime, timedelta
from utils import send_sms  # Import your function for sending SMS

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "full_name", "phone_no", "role", "otp", "otp_expiry"]
        read_only_fields = ["id", "otp_expiry"]

    def create(self, validated_data):
        otp = random.randint(1000, 9999)
        otp_expiry = datetime.now() + timedelta(minutes = 10)
        user = CustomUser.objects.create(**validated_data)
        if otp:
            print("otp", otp)
            send_sms(user.phone_no, otp)
            user.otp = otp
            user.otp_expiry = otp_expiry
            user.save()
        return user

