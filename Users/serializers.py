# serializers.py
from datetime import datetime, timedelta
import random
from rest_framework import serializers
from utils import send_sms
from .models import CustomUser

# Ad
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password field is write-only

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Remove password from validated data
        instance = self.Meta.model(**validated_data)  # Create new user instance
        if password is not None:
            instance.set_password(password)  # Hash the password
        instance.save()  # Save the user instance
        return instance
    
# Sa
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "full_name", "phone_no", "role", "otp", "otp_expiry"]
        read_only_fields = ["id", "otp_expiry"]

    def create(self, validated_data):
        otp = random.randint(1000, 9999)
        otp_expiry = datetime.now() + timedelta(minutes=10)
        user = CustomUser.objects.create(**validated_data)
        if otp:
            print("otp", otp)
            send_sms(user.phone_no, otp)
            user.otp = otp
            user.otp_expiry = otp_expiry
            user.save()
        return user

