from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from Orders.models import Order, OrderProducts, Transactions
from Orders.serializers import OrderSerializer, OrderProductsSerializer, TransactionsSerializer

@api_view(['GET'])
def order_by_pk(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(order)
    return Response(serializer.data)


@api_view(['GET'])
def orders(request):
    try:
        orders = Order.objects.all()
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def insert_order_one(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_order_by_pk(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_order_by_pk(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def insert_multiple_orders(request):
    serializer = OrderSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







#apis for order product model

@api_view(['GET'])
def order_products_by_pk(request, pk):
    try:
        order_product = OrderProducts.objects.get(pk=pk)
    except OrderProducts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrderProductsSerializer(order_product)
    return Response(serializer.data)

@api_view(['GET'])
def order_products(request):
    try:
        order_products = OrderProducts.objects.all()
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = OrderProductsSerializer(order_products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def insert_order_product_one(request):
    serializer = OrderProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def delete_order_product_by_pk(request, pk):
    try:
        order_product = OrderProducts.objects.get(pk=pk)
        order_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except OrderProducts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def update_order_product_by_pk(request, pk):
    try:
        order_product = OrderProducts.objects.get(pk=pk)
    except OrderProducts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OrderProductsSerializer(order_product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def insert_multiple_order_products(request):
    serializer = OrderProductsSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#apis for transaction

@api_view(['GET'])
def transaction_by_pk(request, pk):
    try:
        transaction = Transactions.objects.get(pk=pk)
    except Transactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TransactionsSerializer(transaction)
    return Response(serializer.data)

@api_view(['GET'])
def transactions(request):
    try:
        transactions = Transactions.objects.all()
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    serializer = TransactionsSerializer(transactions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def insert_transaction_one(request):
    serializer = TransactionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_transaction_by_pk(request, pk):
    try:
        transaction = Transactions.objects.get(pk=pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Transactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_transaction_by_pk(request, pk):
    try:
        transaction = Transactions.objects.get(pk=pk)
    except Transactions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TransactionsSerializer(transaction, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_multiple_transactions(request):
    serializer = TransactionsSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)