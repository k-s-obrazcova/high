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


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', decimal_places=2, max_digits=10)

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'date_create',
            'date_update',
            'photo',
            'is_exists',
            'category',
            'tag',
            'warehouse',
            'parametr'
        ]


class ProductSerializerSmall(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price'
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = [
            'date_supply',
            'supplier',
            'product'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'description'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name',
            'description'
        ]


class ParametrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametr
        fields = [
            'name'
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = [
            'owner_lastname',
            'owner_name',
            'owner_surname',
            'location',
            'capacity',
            'main_delivery_type'
        ]


class InventorySerializer(serializers.ModelSerializer):
    mass = serializers.DecimalField(label='Вес одного товара', decimal_places=2, max_digits=10)
    class Meta:
        model = Inventory
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'product',
            'user_name',
            'rating',
            'comment',
            'photo'
        ]


