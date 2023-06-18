from djoser.serializers import UserCreateSerializer, UserSerializer
from core.models import User
from rest_framework import serializers


class userserial(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = [
            "id",
            "username",
            "phone",
            "OTP",
            "password",
            "first_name",
            "last_name",
            "profile",
        ]

    # lesson 16,17 part2
    def create(self, validated_data):
        return super().create(validated_data)


class customserial(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = [
            "id",
            "phone",
            "first_name",
            "last_name",
            "profile",
        ]
