
from rest_framework import serializers
from Payments.models import Transaction

# Ad
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'