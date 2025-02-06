from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrencyViewSet, CurrencyExchangeRateViewSet, CurrencyRatesList, ConvertAmount

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'exchange-rates', CurrencyExchangeRateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('currency-rates/<str:source_currency>/<str:date_from>/<str:date_to>/', CurrencyRatesList.as_view()),
    path('convert/<str:source_currency>/<str:amount>/<str:exchanged_currency>/', ConvertAmount.as_view()),
]