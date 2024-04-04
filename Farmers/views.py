from Farmers.models import Farmer
from Farmers.serializers import FarmerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
@api_view(['GET'])
def farmers_by_pk(request,pk):
    try:
        farmer = Farmer.objects.get(pk=pk)
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data)
    except Farmer.DoesNotExist:
        return Response({'error': 'Farmer not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def farmers(request):
    try:
        users = Farmer.objects.all()  # Retrieve all users from the database
        serializer = FarmerSerializer(users, many=True)  # Serialize the queryset
        return Response(serializer.data)
    except Farmer.DoesNotExist:
        return Response({'error': 'Users not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def insert_farmers_one(request):
    serializer = FarmerSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
# @permission_classes((IsAuthenticated, ))
def update_farmers_by_pk(request, pk):
    try:
        user = Farmer.objects.get(pk=pk)
    except Farmer.DoesNotExist:
        print("excute this except in what ever case")
        return Response({"message":f"Farmer with { pk } does not exist"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = FarmerSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_farmers_by_pk(request, pk):
    # @permission_classes((IsAuthenticated, ))
    try:
        user = Farmer.objects.get(pk=pk)
        serilzer=FarmerSerializer(user)

    except Farmer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response(serilzer.data,status=status.HTTP_204_NO_CONTENT) 


