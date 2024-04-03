# serializers.py
from rest_framework import serializers
from .models import CustomUser

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
