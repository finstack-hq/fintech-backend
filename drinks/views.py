from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink, Currency
from .serializers import DrinkSerializer, CurrencySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse

# Create your views here.

@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        # return JsonResponse({"drinks": serializer.data}, safe=False)
        # return JsonResponse({"drinks": serializer.data})
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
       drink.delete()
       return Response(status=status.HTTP_204_NO_CONTENT) 
    
    # Currency Conversion API
@api_view(['GET', 'POST'])
def Currency_list(request, format=None):

    if request.method == 'GET':
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        # return JsonResponse({"drinks": serializer.data}, safe=False)
        # return JsonResponse({"rates": serializer.data})
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def Currency_detail(request, id, format=None):

    try:
        currency = Currency.objects.get(pk=id)
    except Currency.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CurrencySerializer(currency)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CurrencySerializer(currency, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
       currency.delete()
       return Response(status=status.HTTP_204_NO_CONTENT) 
