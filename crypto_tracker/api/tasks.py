from crypto_tracker.celery import app
from celery.utils.log import get_task_logger
from crypto_tracker.api.constants.crypto import Coins, Currencies, parseCoin
from crypto_tracker.api.services.crypto import CryptoListing
from enum import Enum

logger = get_task_logger(__name__)

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(5, test.s('hello'), name='every 5')
    sender.add_periodic_task(5, fetch_and_store_coin_price.s(Coins.Bitcoin.value), name='every 5')


# @app.task(name='test')
# def test(arg):
#     print(arg)

@app.task(name="fetch_and_store_coin_price")
def fetch_and_store_coin_price(coin: str):
    lister = CryptoListing.get_lister()

    price = lister.get_price([parseCoin(coin)], currency=Currencies.us_dollar)

    logger.info(price)