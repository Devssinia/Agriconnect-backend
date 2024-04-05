
from rest_framework import serializers
from Payments.models import PaymentTransaction

# Ad
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = '__all__'