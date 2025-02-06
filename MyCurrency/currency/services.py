from .providers.currency_beacon import CurrencyBeaconProvider
from .providers.mock_provider import MockProvider

def get_exchange_rate_data(source_currency, exchanged_currency, valuation_date, provider='currencybeacon'):
    if provider == 'currencybeacon':
        provider = CurrencyBeaconProvider(api_key='YOUR_API_KEY')
    elif provider == 'mock':
        provider = MockProvider()
    else:
        raise ValueError("Invalid provider")

    return provider.get_exchange_rate_data(source_currency, exchanged_currency, valuation_date)