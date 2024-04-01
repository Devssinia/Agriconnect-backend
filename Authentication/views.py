from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class Good(APIView):
    def get(self, request):
        return Response({'message': 'HELLO WORLD'})

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successfully logged out'}, status=status.HTTP_205_RESET_CONTENT)          
        except Exception as e: 
            return Response({'message': 'Failed to log out'}, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(APIView):
    User = get_user_model()
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            phone_number = request.data.get('phone_no')
            user = User.objects.get(phone_no=phone_number)
            new_password = request.data.get('new_password')
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password Updated Successfully'}, status=status.HTTP_200_OK)        
        except Exception as e: 
            return Response({'message': 'Unable to update password'}, status=status.HTTP_400_BAD_REQUEST)