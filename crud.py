from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from Farmers.models import Farmer
from Farmers.serializers import FarmerSerializer
from Orders.models import Order
from Orders.serializers import OrderSerializer
from Products.models import Product
from Products.serializers import ProductSerializer
from Users.models import CustomUser
from Users.serializers import CustomUserSerializer
# Retrieve an object by primary key
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def retrieve_object_by_pk(request,pk):
    model_name = request.query_params.get('model_name')

    model_class, serializer_class = get_model_and_serializer(model_name)
    # Retrieve the object by its primary key
    obj = get_object_or_404(model_class, pk=pk)
    serializer = serializer_class(obj)
    return Response(serializer.data)

# List all objects of a model
@api_view(['GET'])
def list_objects(request):
    model_name = request.query_params.get('model_name')
    model_class, serializer_class = get_model_and_serializer(model_name)
    # Retrieve all objects of the specified model
    objects = model_class.objects.all()
    serializer = serializer_class(objects, many=True)
    return Response(serializer.data)

# Insert a new object
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def insert_objects_one(request):
    model_name = request.query_params.get('model_name')
    print(f"model name  fron backend is {model_name}")
    model_class, serializer_class = get_model_and_serializer(model_name)
    serializer = serializer_class(data=request.data)
    if serializer.is_valid():
        obj = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update an existing object by primary key
@api_view(['PUT', 'PATCH'])
@permission_classes((IsAuthenticated,))
def update_object_by_pk(request,pk):
    model_name = request.query_params.get('model_name')
    model_class, serializer_class = get_model_and_serializer(model_name)
    
    try:
        obj = model_class.objects.get(pk=pk)
    except model_class.DoesNotExist:
        return Response({"message": f"{model_name.capitalize()} with pk={pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = serializer_class(obj, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete an object by primary key
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_object_by_pk(request, pk):
    model_name = request.query_params.get('model_name')
    model_class, serializer_class = get_model_and_serializer(model_name)
    try:
        obj = model_class.objects.get(pk=pk)
    except model_class.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Get model class and serializer class based on model name
def get_model_and_serializer(model_name):
    if model_name == 'Farmer':
        return Farmer, FarmerSerializer
    elif model_name == 'Product':
        return Product, ProductSerializer
    elif model_name == 'User':
        return CustomUser,CustomUserSerializer,
    elif model_name=="Order":
        return Order,OrderSerializer
    else:
        return None, None
