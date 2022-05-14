from rest_framework import serializers
from crypto_tracker.api.models import Price
from crypto_tracker.api.constants.crypto import coin_to_symbol_map

class PriceSerializer(serializers.Serializer):

    coin = serializers.SerializerMethodField()
    timestamp = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()



    def get_coin(self, instance):
        return coin_to_symbol_map.get(instance.coin.symbol, None)

    def get_timestamp(self, instance):
        return instance.created_at

    def get_price(self, instance):
        return instance.price

    class Meta:
        model = Price
        fields = ['coin', 'timestamp', 'price']