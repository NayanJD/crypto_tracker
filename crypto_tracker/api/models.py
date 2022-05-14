from django.db import models

# Create your models here.
class BaseModel(models.Model):
    '''
    Abstract Base model for adding basic auditing meta columns
    '''
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated at", auto_now=True)
    archived_at = models.DateTimeField("archived at", null=True, blank=True)

    class Meta:
        abstract = True

class Coin(BaseModel):
    '''
    Coin model represents Crypto Coins
    '''
    name = models.TextField()
    symbol = models.TextField()

    class Meta:
        db_table = "coin"
        constraints = [
            models.UniqueConstraint(
                fields=['symbol'],
                name="unique_coin_symbol"
            )
        ]

class Price(models.Model):
    '''
    Price model for Coin types. 
    At the moment all the prices are stored in USD
    '''
    coin = models.ForeignKey("Coin", related_name="prices", on_delete=models.RESTRICT)

    price = models.DecimalField(max_digits=20, decimal_places=6)

    created_at = models.DateTimeField("created at", auto_now_add=True)

    class Meta:
        db_table = "price"