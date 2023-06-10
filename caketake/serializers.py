from decimal import Decimal
from django.db import transaction
from rest_framework import serializers

from caketake.models import (
    address,
    customer,
    fps,
    order,
    product,
    rating,
    shop,
)


class productserial(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)

    class Meta:
        model = product
        fields = [
            "id",
            "shop_id",
            "image",
            "more_images",
            "name",
            "description",
            "adult",
            "food_type",
            "active",
        ]


class adminproductserial(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = [
            "id",
            "shop",
            "image",
            "more_images",
            "name",
            "description",
            "adult",
            "food_type",
            "active",
            "created_at",
        ]


class shopserial(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = [
            "id",
            "shop_name",
            "original_name",
            "seller",
        ]


class addressserial(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = [
            # "id",
            "tittle",
            "zip",
            "street",
            "city",
            "landmark",
            "customer",
        ]


class customerserial(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    addresss = serializers.CharField(read_only=True)

    class Meta:
        model = customer
        fields = [
            "id",
            "user_id",
            "profile",
            "first_name",
            "last_name",
            "email",
            "addresss",
        ]


class orderserial(serializers.ModelSerializer):
    payment_status = serializers.CharField(read_only=True)
    order_status = serializers.CharField(read_only=True)

    class Meta:
        model = order
        fields = [
            "id",
            "product",
            "customer",
            "fps",
            "any_request",
            "delivery_type",
            "pay_type",
            "payment_status",
            "order_status",
            # "with_gst",
        ]


class adminorderserial(serializers.ModelSerializer):
    any_request = serializers.CharField(read_only=True)
    delivery_type = serializers.CharField(read_only=True)
    pay_type = serializers.CharField(read_only=True)

    class Meta:
        model = order
        fields = [
            "id",
            "product",
            "customer",
            "fps",
            "any_request",
            "delivery_type",
            "pay_type",
            "payment_status",
            "order_status",
        ]


class fpsserial(serializers.ModelSerializer):
    class Meta:
        model = fps
        fields = [
            "id",
            "product_id",
            "flavour",
            "price",
            "with_gst",
            "weight",
            "floor_size",
            "making_time",
        ]

    with_gst = serializers.SerializerMethodField(method_name="cal_gst")

    def cal_gst(self, fps: fps):
        return fps.price * Decimal(1.18)


class adminfpsserial(serializers.ModelSerializer):
    class Meta:
        model = fps
        fields = [
            "id",
            "product",
            "flavour",
            "price",
            "with_gst",
            "weight",
            "floor_size",
            "making_time",
        ]

    with_gst = serializers.SerializerMethodField(method_name="cal_gst")

    def cal_gst(self, fps: fps):
        return fps.price * Decimal(1.18)


class sellerserial(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = customer
        fields = [
            "id",
            "user_id",
            "profile",
            "first_name",
            "last_name",
            "email",
        ]
