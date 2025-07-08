import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


# Create your views here.



# REST API's
@api_view(['GET' , 'POST'])
def products(request) :
    if request.method  ==  "POST" :
        serializer  = ProductSerializer(data  = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response({'message' :  "success"}  ,  status  = status.HTTP_200_OK)
        return Response({'message': "Failure"} , status = status.HTTP_400_BAD_REQUEST)

    # filtering and searching  api response
    if request.method == 'GET' :
        name  =  request.GET.get('name')
        min_price =  request.GET.get('min_price')
        max_price =  request.GET.get('max_price')
        order = request.GET.get('order')
        products =  Product.objects.all()
        if name  :
            products = Product.filter(name__icontains=name)
        if min_price :
            products =  products.filter(price__gte = min_price)

        if max_price :
            products = products.filter(price__lte = max_price)

        if  order :
            products =  products.order_by(order)

        serializer  = ProductSerializer(products , many  = True)
        return Response(serializer.data , status = status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request , id) :
    product  = get_object_or_404(Product ,  id = id)
    serializer  = ProductSerializer(product)
    return Response(serializer.data  , status =  status.HTTP_200_OK)

    # update method
@api_view(['PUT'])
def 
    # delete method