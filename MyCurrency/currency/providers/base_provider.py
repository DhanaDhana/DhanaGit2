from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def get_exchange_rate_data(self, source_currency, exchanged_currency, valuation_date):
        pass