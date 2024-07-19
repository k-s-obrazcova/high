from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'buyer_lastname',
            'buyer_name',
            'buyer_surname',
            'comment',
            'delivery_address',
            'delivery_type',
            'date_create',
            'date_finish',
            'product',

        ]
