
import uuid
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from Payments.serializers import TransactionSerializer
@api_view(['POST'])
def accept_payment(request):
    
    secret_key = settings.CHAPA_SECRET  # Retrieve secret key from Django settings
    tx_ref = generate_transaction_reference()  # Define your function to generate transaction reference
    print(f"transaction referenvcve is {tx_ref}")
    headers = {
        'Authorization': f'Bearer {secret_key}',
        'Content-Type': 'application/json',
    }

    payload = {
        'amount': request.data.get('amount'),
        'currency': 'ETB',
        'phone_number': request.data.get('phone_no'),
        'tx_ref': tx_ref,
        'return_url': 'https://www.google.com/',
    }

    try:
        # Make a request to external API
        response = requests.post('https://api.chapa.co/v1/transaction/initialize', headers=headers, json=payload)
        response_data = response.json()
        
        # Combine client data with response data
        combined_data = {
            'amount': request.data.get('amount'),
            'currency': 'ETB',
            'phone_no': request.data.get('phone_no'),
            'tx_ref': tx_ref,
            'checkout_url':response_data.get('data', {}).get('checkout_url'),
            'full_name':request.data.get('full_name'),  
        }
        
        # Serialize and save combined data
        serializer = TransactionSerializer(data=combined_data)
        if serializer.is_valid():
            print("until this valid")
            transaction = serializer.save()
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

def generate_transaction_reference():
        return str(uuid.uuid4())
