import zoneinfo
from django.shortcuts import render
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from crypto_tracker.api.models import Price
from crypto_tracker.api.serializer import PriceSerializer
from crypto_tracker.api.constants.crypto import symbol_to_coin_map
from dateutil.parser import parse


class PriceView(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = Price.objects.all()

    # pagination_class = PageNumberPagination

    serializer_class = PriceSerializer

    def get_queryset(self):
        now = timezone.now()

        date = self.request.GET.get('date', None)
        if date:
            day = parse(date, dayfirst=True)
        else:
            day = datetime(year=now.year, month=now.month, day=now.day, tzinfo=now.tzinfo)

        queryset = Price.objects.filter(created_at__gte=day, created_at__lt=day + timedelta(days=1))

        coin_str = self.kwargs.get('symbol', None)

        if coin_str:
            coin_symbol = symbol_to_coin_map.get(coin_str, None)

            queryset = queryset.filter(coin__symbol=coin_symbol)
        
        return queryset

    # def list(self, request, symbol=None):
    #     return Response('success')
