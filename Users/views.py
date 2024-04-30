from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status,viewsets

import datetime
from datetime import timedelta

import random



import datetime
import random
from django.conf import settings
from django.utils import timezone
from utils import send_sms
from Users.models import CustomUser
from .serializers import UserSerializer
# Ad
@api_view(['GET'])
def users_by_pk(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def users(request):
    try:
        users = CustomUser.objects.all()  # Retrieve all users from the database
        serializer = CustomUserSerializer(users, many=True)  # Serialize the queryset
        return Response(serializer.data)
    except CustomUser.DoesNotExist:
        return Response({'error': 'Users not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def insert_users_one(request):
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register(request):
    # Extracting necessary data from request
    full_name = request.data.get('full_name')
    phone_no = request.data.get('phone_no')
    password = request.data.get('password')

    #creating otp
    # otp = random.randint(1000, 9999)
    # otp_expiry = datetime.now() + timedelta(minutes=10)
    
    # Validating data
    if not (full_name and phone_no and password):
        return Response({'error': 'Full name, phone number, and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    #validate and send the otp
    # if otp:
    #     print("otp", otp)
    #     send_sms(phone_no, otp)
    # else:
    #     print("the otp is not recieved by the phone")

    # Creating the user
    try:
        print("....................................11111")
        user = CustomUser.objects.create_user(phone_no=phone_no, full_name=full_name, password=password)

        print("....................................2222")

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer = CustomUserSerializer(user)
        print("....................................3333")

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT', 'PATCH'])
def update_users_by_pk(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CustomUserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_users_by_pk(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
        serilzer=CustomUserSerializer(user)

    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response(serilzer.data,status=status.HTTP_204_NO_CONTENT) 



# Sa

class UserViewSet(viewsets.ModelViewSet):
    """
    UserModel View.
    """

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


    @action(detail=True, methods=["PATCH"])
    def verify_otp(self, request, pk=None):
        instance = self.get_object()
        if (
            not instance.is_active
            and instance.otp == request.data.get("otp")
            and instance.otp_expiry
            and timezone.now() < instance.otp_expiry
        ):
            instance.is_active = True
            instance.otp_expiry = None
            instance.max_otp_try = settings.MAX_OTP_TRY
            instance.otp_max_out = None
            instance.save()
            return Response(
                "Successfully verified the user.", status=status.HTTP_200_OK
            )

        return Response(
            "User active or Please enter the correct OTP.",
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(detail=True, methods=["PATCH"])
    def regenerate_otp(self, request, pk=None):
        """
        Regenerate OTP for the given user and send it to the user.
        """
        instance = self.get_object()
        if int(instance.max_otp_try) == 0 and timezone.now() < instance.otp_max_out:
            return Response(
                "Max OTP try reached, try after an hour",
                status=status.HTTP_400_BAD_REQUEST,
            )

        otp = random.randint(1000, 9999)
        otp_expiry = timezone.now() + datetime.timedelta(minutes=10)
        max_otp_try = int(instance.max_otp_try) - 1

        instance.otp = otp
        instance.otp_expiry = otp_expiry
        instance.max_otp_try = max_otp_try
        if max_otp_try == 0:
            # Set cool down time
            otp_max_out = timezone.now() + datetime.timedelta(hours=1)
            instance.otp_max_out = otp_max_out
        elif max_otp_try == -1:
            instance.max_otp_try = settings.MAX_OTP_TRY
        else:
            instance.otp_max_out = None
            instance.max_otp_try = max_otp_try
        instance.save()
        send_sms(instance.phone_number, otp)
        return Response("Successfully generate new OTP.", status=status.HTTP_200_OK)
