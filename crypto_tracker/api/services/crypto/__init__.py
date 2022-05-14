import abc
from pycoingecko import CoinGeckoAPI
from crypto_tracker.api.constants.crypto import Coins, Currencies

class CryptoListing(metaclass=abc.ABCMeta):
    '''
    Abstract class for crypto API implementers.
    get_lister() should be used to get concrete 
    implementation of the listing service
    '''
    @abc.abstractmethod
    def get_price(self, coin: Coins, currency: Currencies) -> float:
        pass

    @abc.abstractmethod
    def get_prices(self, coins: list[Coins], currency: Currencies) -> list[float]:
        pass

    def get_lister():
        return CoinGeckoListing()


class CoinGeckoListing(CryptoListing):
    '''
    Implementation of CryptoListing using 
    Coin Gecko API
    '''
    def __init__(self):
        self.cg = CoinGeckoAPI()

    def get_prices(self, coins: list[Coins], currency: Currencies) -> list[float]:
        response = self.cg.get_price(ids=list(map(lambda x: x.value, coins)), vs_currencies=currency.value)

        prices = []
        for coin_str in response:
            prices.append(response[coin_str][currency.value])

        return prices

    def get_price(self, coin: Coins, currency: Currencies) -> float:
        prices = self.get_prices([coin], currency=currency)

        return prices[0]