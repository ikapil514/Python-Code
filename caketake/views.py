from django.shortcuts import render
from .permissions import AuthExceptAdmin, SuperAdminUser, SuperOrReadonly
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
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
)

# Create your views here.


class cshopViewSet(ModelViewSet):
    queryset = shop.objects.all()
    serializer_class = shopserial
    permission_classes = [SuperOrReadonly]


class productViewSet(ModelViewSet):
    permission_classes = [SuperOrReadonly]

    def get_queryset(self):
        return product.objects.filter(shop_id=self.kwargs["shop_pk"])

    serializer_class = adminproductserial


class sellershopViewSet(
    CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = shopserial
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        sellerid = seller.objects.get(id=self.request.user.seller.id)
        return shop.objects.filter(seller_id=sellerid)

    def get_serializer_context(self):
        return {"seller_id": self.request.user.seller.id}


class sellerproductViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return product.objects.filter(shop_id=self.kwargs["shop_pk"])

    serializer_class = adminproductserial

    def get_serializer_context(self):
        return {"product_id": self.kwargs["shop_pk"]}


class fpsViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = fps.objects.all()
    serializer_class = fpsserial
    permission_classes = [IsAdminUser]


class customerViewSet(ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = customerserial
    permission_classes = [SuperAdminUser]

    @action(detail=False, methods=["GET", "PUT"], permission_classes=[AuthExceptAdmin])
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
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    permission_classes = [AuthExceptAdmin]

    def get_queryset(self):
        cust_id = customer.objects.only("id").get(user_id=self.request.user)
        return order.objects.filter(customer_id=cust_id)

    def get_serializer_class(self):
        return orderserial

    def get_serializer_context(self):
        return {"customer_id": self.request.user.customer.id}


class sellerorderViewSet(ModelViewSet):
    serializer_class = adminorderserial

    def get_queryset(self):
        shp = shop.objects.only("id").get(seller_id=self.request.user.seller.id)
        return order.objects.filter(shop_id=shp)

    permission_classes = [IsAdminUser]


class sellerViewSet(ModelViewSet):
    queryset = seller.objects.all()
    serializer_class = sellerserial
    permission_classes = [SuperAdminUser]

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
