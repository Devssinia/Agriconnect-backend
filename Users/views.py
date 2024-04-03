from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_user_one(request, pk):
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
def create_user_one(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['password']
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_user_one(request, pk):
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
def delete_user_one(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
        serilzer=CustomUserSerializer(user)

    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response(serilzer.data,status=status.HTTP_204_NO_CONTENT) 