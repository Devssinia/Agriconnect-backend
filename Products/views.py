from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from Farmers.models import Farmer, FarmerProducts
from Products.models import Categories, Product, UOMs
from Products.serializers import  CategoriesSerializer, ProductSerializer, UOMsSerializer

@api_view(['GET'])
def products_by_pk(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def products(request):
    try:
        products = Product.objects.all()
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def insert_product_one(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_product_by_pk(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_product_by_pk(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def insert_multiple_products(request):
    serializer = ProductSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def farmers_with_products(request):
    try:
        farmer_products = FarmerProducts.objects.all()
        data = []
        for farmer_product in farmer_products:
            farmer_product_data = {
                'farmerproduct_id': farmer_product.id,
                'rate': str(farmer_product.rate),  # Convert DecimalField to string for serialization
                'farmer': {
                    'id': farmer_product.farmer_id.id,
                    'full_name': farmer_product.farmer_id.full_name,
                    'phone_no': farmer_product.farmer_id.phone_no,
                    'location_latitude': str(farmer_product.farmer_id.location_latitude),
                    'location_longitude': str(farmer_product.farmer_id.location_longitude),
                    'location_name': farmer_product.farmer_id.location_name,
                    'profile_image': farmer_product.farmer_id.profile_image,
                    # Add other farmer fields as needed
                },
                'product': {
                    'id': farmer_product.product_id.id,
                    'uom': {
                        'id': farmer_product.product_id.uom.id,
                        'name': farmer_product.product_id.uom.name,
                    },
                    'category': {
                        'id': farmer_product.product_id.category.id,
                        'name': farmer_product.product_id.category.name,
                    },
                    'last_added': str(farmer_product.product_id.last_added),
                    'location_latitude': str(farmer_product.product_id.location_latitude),
                    'location_longitude': str(farmer_product.product_id.location_longtude),
                    'image1': farmer_product.product_id.image1.url if farmer_product.product_id.image1 else None,
                    'image2': farmer_product.product_id.image2.url if farmer_product.product_id.image2 else None,
                    'image3': farmer_product.product_id.image3.url if farmer_product.product_id.image3 else None,
                    'product_description': farmer_product.product_id.product_description,
                    # Add other product fields as needed
                },
                'uom': {
                    'id': farmer_product.uom.id,
                    'name': farmer_product.uom.name,
                },
            }
            data.append(farmer_product_data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(data)














#uom views

@api_view(['GET'])
def uoms(request):
    try:
        uoms = UOMs.objects.all()
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = UOMsSerializer(uoms, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def insert_uoms_one(request):
    serializer = UOMsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










#categories
#uom views

@api_view(['GET'])
def categories(request):
    try:
        uoms = Categories.objects.all()
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = CategoriesSerializer(uoms, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def insert_categories_one(request):
    serializer = CategoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)