import enum

class Coins(enum.Enum):
    '''
    Supported crypto coins
    '''
    Bitcoin = 'bitcoin'

def parseCoin(coin_str: str):
    for coin in Coins:
        if coin.value == coin_str:
            return coin
    
    raise ValueError("Could not parse string as Coins enum")

symbol_to_coin_map = {
    'btc': Coins.Bitcoin.value
}

coin_to_symbol_map = {
    Coins.Bitcoin.value: 'btc'
}

class Currencies(enum.Enum):
    '''
    Supported currencies
    '''
    us_dollar = 'usd'
    euro = 'eur'