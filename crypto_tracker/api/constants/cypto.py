import enum

class Coins(enum.Enum):
    '''
    Supported crypto coins
    '''
    Bitcoin = 'bitcoin'

class Currencies(enum.Enum):
    '''
    Supported currencies
    '''
    us_dollar = 'usd'
    euro = 'eur'