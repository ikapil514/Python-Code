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
    seller,
    shop,
)


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


class adminproductserial(serializers.ModelSerializer):
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
            # "fps",
        ]

    def create(self, validated_data):
        shop_id = self.context["product_id"]
        return product.objects.create(shop_id=shop_id, **validated_data)

    # def update(self, instance, validated_data):
    #     instance.fps = validated_data.get("fps")
    #     instance.save()
    #     return instance


class shopserial(serializers.ModelSerializer):
    class Meta:
        model = shop
        fields = [
            "id",
            "shop_name",
            "original_name",
            "seller_id",
        ]

    def create(self, validated_data):
        seller_id = self.context["seller_id"]
        return shop.objects.create(seller_id=seller_id, **validated_data)


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
            "customer_id",
            "fps",
            "any_request",
            "delivery_type",
            "pay_type",
            "payment_status",
            "order_status",
            "placed_at",
        ]


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
            # "shops",
            "profile",
            "first_name",
            "last_name",
            "email",
        ]
