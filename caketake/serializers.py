from decimal import Decimal
from genericpath import exists
from django.db import transaction
from rest_framework import serializers

from caketake.models import (
    address,
    customer,
    fps,
    order,
    product,
    rating,
    seller,
    shop,
)


class fpsserial(serializers.ModelSerializer):
    class Meta:
        model = fps
        fields = [
            "product",
            "id",
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


class adminproductserial(serializers.ModelSerializer):
    fps = fpsserial(many=True, read_only=True)

    class Meta:
        model = product
        fields = [
            "id",
            "image",
            "more_images",
            "name",
            "description",
            "adult",
            "food_type",
            "active",
            "created_at",
            "fps",
        ]

    def create(self, validated_data):
        shop_id = self.context["product_id"]
        return product.objects.create(shop_id=shop_id, **validated_data)

    # def update(self, instance, validated_data):
    #     product.fps = validated_data.get("fps")
    #     product.save()
    #     return product


class shopserial(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = [
            "id",
            "shop_name",
            "original_name",
            "seller_id",
            "orders",
        ]

    def create(self, validated_data):
        seller_id = self.context["seller_id"]
        return shop.objects.create(seller_id=seller_id, **validated_data)

    # def validate(self, data):
    #     if data["shop_id"] is exists:
    #         return serializers.ValidationError("Shop Already Exists")
    #     return data


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
            "customer_id",
            "shop",
            "product",
            "fps",
            "any_request",
            "delivery_type",
            "pay_type",
            "payment_status",
            "order_status",
            "placed_at",
        ]

    def create(self, validated_data):
        customer_id = self.context["customer_id"]
        return order.objects.create(customer_id=customer_id, **validated_data)


class adminorderserial(serializers.ModelSerializer):
    any_request = serializers.CharField(read_only=True)
    delivery_type = serializers.CharField(read_only=True)
    pay_type = serializers.CharField(read_only=True)

    class Meta:
        model = order
        fields = [
            "id",
            "product_id",
            "customer_id",
            "fps_id",
            "shop_id",
            "any_request",
            "delivery_type",
            "pay_type",
            "payment_status",
            "order_status",
            "placed_at",
        ]


class sellerserial(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    # shops = serializers.CharField(read_only=True)

    class Meta:
        model = seller
        fields = [
            "id",
            "user_id",
            "profile",
            "first_name",
            "last_name",
            "email",
        ]
