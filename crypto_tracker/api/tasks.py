from django.core.mail import send_mail
from django.conf import settings
from crypto_tracker.celery import app
from celery.utils.log import get_task_logger
from crypto_tracker.api.constants.crypto import Coins, Currencies, parseCoin
from crypto_tracker.api.services.crypto import CryptoListing
from crypto_tracker.api.models import Coin, Price
from enum import Enum

logger = get_task_logger(__name__)

max_price = settings.MAX_PRICE_THRESHOLD
min_price = settings.MIN_PRICE_THRESHOLD
alert_email = settings.ALERT_EMAIL


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(5, test.s('hello'), name='every 5')

    # Add fetching coin price task every 30s
    sender.add_periodic_task(30, fetch_and_store_coin_price.s(Coins.Bitcoin.value), name='every 30')


# @app.task(name='test')
# def test(arg):
#     print(arg)

@app.task(name="fetch_and_store_coin_price")
def fetch_and_store_coin_price(coin_str: str):
    lister = CryptoListing.get_lister()

    coin = parseCoin(coin_str)

    price = lister.get_price(coin, currency=Currencies.us_dollar)

    logger.info(price)

    if price > max_price:
        logger.info('Price increased from maximum threshold')

        subject = f'{coin.name} price increased'
        plain_message = f'{coin.name} increased maximum threshold of {max_price}. Current price is {price}'
        from_email = 'from@example.com'
        to = alert_email

        send_mail(subject, plain_message, from_email, [to])

    if price < min_price:
        logger.info('Price decreased from  maximum threshold')

    coin = Coin.objects.get(symbol=coin.value)

    Price.objects.create(coin=coin, price=price)

