from Farmers.models import Farmer, FarmerProducts
from Farmers.serializers import FarmerProductsSerializer, FarmerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
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

@api_view(['GET'])
def farmers_with_products(request):
    try:
        farmers = Farmer.objects.all()
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = FarmerSerializer(farmers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
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
@permission_classes((IsAuthenticated))
def delete_farmers_by_pk(request, pk):
    # @permission_classes((IsAuthenticated, ))
    try:
        user = Farmer.objects.get(pk=pk)
        serilzer=FarmerSerializer(user)

    except Farmer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response(serilzer.data,status=status.HTTP_204_NO_CONTENT) 








# view for farmerProducts
@api_view(['GET'])
def farmerProducts_by_pk(request,pk):
    try:
        farmer = FarmerProducts.objects.get(pk=pk)
        serializer = FarmerProductsSerializer(farmer)
        return Response(serializer.data)
    except Farmer.DoesNotExist:
        return Response({'error': 'Farmer product not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def farmerProducts(request):
    try:
        users = FarmerProducts.objects.all()  # Retrieve all users from the database
        serializer = FarmerProductsSerializer(users, many=True)  # Serialize the queryset
        return Response(serializer.data)
    except Farmer.DoesNotExist:
        return Response({'error': 'farmer products not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
def insert_farmerProducts_one(request):

    serializer = FarmerProductsSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT', 'PATCH'])
# @permission_classes((IsAuthenticated, ))
def update_farmerProducts_by_pk(request, pk):
    try:
        user = FarmerProducts.objects.get(pk=pk)
    except Farmer.DoesNotExist:
        print("excute this except in what ever case")
        return Response({"message":f"Farmer product with { pk } does not exist"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = FarmerProductsSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
# @permission_classes((IsAuthenticated))
def delete_farmerProducts_by_pk(request, pk):
    try:
        farmerProduct = FarmerProducts.objects.get(pk=pk)
        serilzer=FarmerProductsSerializer(farmerProduct)

    except FarmerProducts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    farmerProduct.delete()
    return Response(serilzer.data,status=status.HTTP_204_NO_CONTENT) 

    

