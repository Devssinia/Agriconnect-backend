import uuid
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from Payments.models import PaymentTransaction
from Payments.serializers import TransactionSerializer
@api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
def accept_payment(request):
    global tx_ref
    secret_key = settings.CHAPA_SECRET  # Retrieve secret key from Django settings
    print(".........secret key", settings.CHAPA_SECRET)  # Retrieve secret key from Django settings
    tx_ref= generate_transaction_reference()  # Define your function to generate transaction reference
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
        'return_url':f"http://{settings.PORT}:8000/payments/verify/",
    }

    try:
        # Make a request to external API
        response = requests.post('https://api.chapa.co/v1/transaction/initialize', headers=headers, json=payload)
        response_data = response.json()
        print("response from..................", response_data)
        # verify_data=verifyPayment(tx_ref,secret_key)
        # print(f"verified data is {verify_data}")
        # Combine client data with response data
        combined_data = {
            'amount': request.data.get('amount'),
            'currency': 'ETB',
            'phone_no': request.data.get('phone_no'),
            'tx_ref': tx_ref,
            'checkout_url':response_data.get('data', {}).get('checkout_url'),
            'full_name':request.data.get('full_name'),  
            'email': request.data.get('email'),
            
        }
        
        # Serialize and save combined data
        print(".....................1")
        serializer = TransactionSerializer(data=combined_data)
        print(".....................2")

        # if serializer.is_valid():
        print("until this valid")
        # transaction = serializer.save()
        print("until this validddddddddddddddddd")

        return Response(response_data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

def generate_transaction_reference():
        return str(uuid.uuid4())

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def verifyPayment(request):
    print("at least this is excuted")
    
    url = f"https://api.chapa.co/v1/transaction/verify/{tx_ref}"
    payload = ''
    headers = {
      'Authorization': f'Bearer {settings.CHAPA_SECRET}'
    }
    response = requests.get(url, headers=headers, data=payload)
    
     # Extract the data from the response
    response_data = response.json()
    payment_data = response_data.get('data', {})
    
    # Modify the data as needed
    try:
        user = PaymentTransaction.objects.get(tx_ref=tx_ref)
    except PaymentTransaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TransactionSerializer(user, data=payment_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)