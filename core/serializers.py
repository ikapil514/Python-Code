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

    # def create(self, validated_data):

    #     return User.object.create_user(**validated_data)


class customserial(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = [
            "id",
            "phone",
            "first_name",
            "last_name",
            "profile",
        ]
