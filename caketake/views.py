from django.shortcuts import render
from django.db.models import F
from core import serializers
from .permissions import AdminOrReadonly, Authonly, FullAdminUser, SuperOrReadonly
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
    sellerserial,
    shopserial,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action, api_view, APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, RetrieveModelMixin

# Create your views here.


class cshopViewSet(ModelViewSet):
    queryset = shop.objects.all()
    serializer_class = shopserial
    permission_classes = [SuperOrReadonly]


class productViewSet(ModelViewSet):
    permission_classes = [AdminOrReadonly]

    def get_queryset(self):
        return product.objects.filter(shop_id=self.kwargs["shop_pk"])

    serializer_class = adminproductserial

    def get_serializer_context(self):
        return {"product_id": self.kwargs["shop_pk"]}


class ShopList(APIView):
    def get(self, request):
        shp = shop.objects.get(seller_id=request.user.seller.id)
        serializer = shopserial(shp)
        return Response(serializer.data)

    def post(self, request):
        serializer = shopserial(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    permission_classes = [IsAdminUser]


class productList(APIView):
    def get(self, request):
        shp = shop.objects.only("id").get(seller_id=request.user.seller.id).id

        pro = product.objects.filter(shop=shp)
        serializer = adminproductserial(pro, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = adminproductserial(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    permission_classes = [IsAdminUser]


class fpsViewSet(ModelViewSet):
    queryset = fps.objects.all()
    serializer_class = fpsserial
    permission_classes = [IsAdminUser]

    # def get_queryset(self):
    #     return fps.objects.filter(product_id=self.kwargs["product_pk"])


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


class orderViewSet(
    CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return order.objects.all()
        cust_id = customer.objects.only("id").get(user_id=self.request.user)
        return order.objects.filter(customer_id=cust_id)

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return adminorderserial
        return orderserial

    # @action(detail=True, permission_classes=[IsAdminUser])
    # def cancel(self, request, pk):
    #     return Response("ok")


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


class addressViewSet(ModelViewSet):
    queryset = address.objects.all()
    serializer_class = addressserial
    # permission_classes = [IsAdminUser]
