from django.shortcuts import render
from django.db.models import F

from core import serializers

from .permissions import AdminOrReadonly, Authonly, FullAdminUser
from .models import (
    address,
    customer,
    fps,
    order,
    product,
    seller,
    shop,
)
from .serializers import (
    addressserial,
    adminorderserial,
    adminproductserial,
    customerserial,
    fpsserial,
    orderserial,
    productserial,
    sellerserial,
    shopserial,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class productViewSet(ModelViewSet):
    permission_classes = [AdminOrReadonly]

    def get_queryset(self):
        return product.objects.filter(shop_id=self.kwargs["shop_pk"])

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return adminproductserial
        return productserial

    def get_serializer_context(self):
        return {"product_id": self.kwargs["shop_pk"]}


class shopViewSet(ModelViewSet):
    queryset = shop.objects.all()
    serializer_class = shopserial
    permission_classes = [AdminOrReadonly]


class addressViewSet(ModelViewSet):
    queryset = address.objects.all()
    serializer_class = addressserial
    # permission_classes = [IsAdminUser]

    # @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAuthenticated])
    # def me(self, request):
    #     (query_set, create) = address.objects.get_or_create(customer_id=request.user.id)
    #     if request.method == "GET":
    #         serializer = addressserial(query_set)
    #         return Response(serializer.data)
    #     elif request.method == "PUT":
    #         serializer = addressserial(query_set, data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         serializer.save()
    #         return Response(serializer.data)


class fpsViewSet(ModelViewSet):
    queryset = fps.objects.all()
    serializer_class = fpsserial
    permission_classes = [IsAdminUser]


class customerViewSet(ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = customerserial
    permission_classes = [FullAdminUser]

    @action(detail=False, methods=["GET", "PUT"], permission_classes=[Authonly])
    def me(self, request):
        (query_set, create) = customer.objects.get_or_create(user_id=request.user.id)
        if request.method == "GET":
            serializer = customerserial(query_set)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = customerserial(query_set, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class orderViewSet(ModelViewSet):
    queryset = order.objects.all()
    # serializer_class = orderserial
    permission_classes = [IsAuthenticated]

    # @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAuthenticated])
    # def me(self, request):
    # serializer = orderserial()
    # return Response(request.user.id)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return adminorderserial
        return orderserial


class sellerViewSet(ModelViewSet):
    queryset = seller.objects.all()
    serializer_class = sellerserial
    permission_classes = [FullAdminUser]

    @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAdminUser])
    def me(self, request):
        (query_set, create) = seller.objects.get_or_create(user_id=request.user.id)
        if request.method == "GET":
            serializer = sellerserial(query_set)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = sellerserial(query_set, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
