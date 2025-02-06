from django.contrib import admin
from .models import Currency, CurrencyExchangeRate
from django.urls import path
from django.shortcuts import render

# Register your models here.

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol')

@admin.register(CurrencyExchangeRate)
class CurrencyExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('source_currency', 'exchanged_currency', 'valuation_date', 'rate_value')


class CurrencyAdminSite(admin.AdminSite):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('currency-converter/', self.admin_view(self.currency_converter_view), name='currency-converter'),
        ]
        return custom_urls + urls

    def currency_converter_view(self, request):
        return render(request, 'admin/currency_converter.html')

admin_site = CurrencyAdminSite(name='mycurrency_admin')
admin_site.register(Currency)
admin_site.register(CurrencyExchangeRate)