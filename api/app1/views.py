import json

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


# REST API's
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "success"}, status=status.HTTP_200_OK)
        return Response({'message': "failure", 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# filtering and searching  api response
#http://127.0.0.2:9000/api/product?max_price=1000
#http://127.0.0.2:9000/api/product?order=price or name
#http://127.0.0.2:9000/api/product?name=abc
    if request.method == 'GET' :
        name  =  request.GET.get('name')
        min_price =  request.GET.get('min_price')
        max_price =  request.GET.get('max_price')
        order = request.GET.get('order')
        products =  Product.objects.all()
        if name  : # we can fetch the data by name or by charcater
            products = Product.filter(name__icontains=name)
        if min_price : #we can set the value for which we want to see the price
            products =  products.filter(price__gte = min_price)

        if max_price : #we can set the value for which we want to see the price
            products = products.filter(price__lte = max_price)

        if  order : # we can order it according to our needs
            products =  products.order_by(order)

        serializer  = ProductSerializer(products , many  = True)
        return Response(serializer.data , status = status.HTTP_200_OK)

@api_view(['GET'])
def product_detail(request,id):
    product=get_object_or_404(Product,id=id)
    serializer=ProductSerializer(product)
    return Response(serializer.data,status=status.HTTP_200_OK)
#update
@api_view(['PUT','PATCH'])
def product_update(request,id):
    product=get_object_or_404(Product,id=id)
    partial= True if request.method=='PATCH' else False
    serializer=ProductSerializer(product,data=request.data,partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Product updated successfully'},status=status.HTTP_200_OK)
    return Response({'message':'Product update failed'},status=status.HTTP_400_BAD_REQUEST)

#delete
@api_view(['DELETE'])
def product_delete(request,id):
    product=get_object_or_404(Product,id=id)
    product.delete()
    return Response({'message':'Product deleted Successfully'},status=status.HTTP_200_OK)