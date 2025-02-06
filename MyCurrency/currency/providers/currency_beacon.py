import requests
from .base_provider import BaseProvider

class CurrencyBeaconProvider(BaseProvider):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.currencybeacon.com/v1/"

    def get_exchange_rate_data(self, source_currency, exchanged_currency, valuation_date):
        url = f"{self.base_url}historical"
        params = {
            'api_key': self.api_key,
            'base': source_currency,
            'symbols': exchanged_currency,
            'date': valuation_date
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        return None