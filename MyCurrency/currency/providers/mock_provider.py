import random
from .base_provider import BaseProvider

class MockProvider(BaseProvider):
    def get_exchange_rate_data(self, source_currency, exchanged_currency, valuation_date):
        return {
            'source_currency': source_currency,
            'exchanged_currency': exchanged_currency,
            'valuation_date': valuation_date,
            'rate_value': random.uniform(0.5, 1.5)
        }