from django.shortcuts import render
from rest_framework import viewsets
from .models import Currency, CurrencyExchangeRate
from .serializers import CurrencySerializer, CurrencyExchangeRateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import get_exchange_rate_data

# Create your views here.

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class CurrencyExchangeRateViewSet(viewsets.ModelViewSet):
    queryset = CurrencyExchangeRate.objects.all()
    serializer_class = CurrencyExchangeRateSerializer

class CurrencyRatesList(APIView):
    def get(self, request, source_currency, date_from, date_to):
        # Implement logic to retrieve rates for the given period
        pass

class ConvertAmount(APIView):
    def get(self, request, source_currency, amount, exchanged_currency):
        rate_data = get_exchange_rate_data(source_currency, exchanged_currency, valuation_date='latest')
        converted_amount = amount * rate_data['rate_value']
        return Response({
            'source_currency': source_currency,
            'exchanged_currency': exchanged_currency,
            'rate_value': rate_data['rate_value'],
            'converted_amount': converted_amount
        })
    
