from rest_framework import serializers
from drinks.models import Drink, Currency

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Drink
        fields = ['id', 'name', 'description']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Currency
        fields = ['id', 'result', 'base_code', 'EUR', 'GBP', 'USD']



