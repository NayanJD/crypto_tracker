import abc
from pycoingecko import CoinGeckoAPI
from crypto_tracker.api.constants.cypto import Coins, Currencies

class CryptoListing(metaclass=abc.ABCMeta):
    '''
    Abstract class for crypto API implementers.
    get_lister() should be used to get concrete 
    implementation of the listing service
    '''
    @abc.abstractmethod
    def get_price(self, coins: list[Coins], currency: Currencies):
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

    def get_price(self, coins: list[Coins], currency: Currencies):
        return self.cg.get_price(ids=list(map(lambda x: x.value, coins)), vs_currencies=currency.value)