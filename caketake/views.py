from django.shortcuts import render
from django.db.models import F

from .permissions import AdminOrReadonly
from .models import (
    address,
    customer,
    fps,
    order,
    product,
    shop,
)
from .serializers import (
    addressserial,
    customerserial,
    fpsserial,
    orderserial,
    productserial,
    shopserial,
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class productViewSet(ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productserial
    permission_classes = [AdminOrReadonly]


class shopViewSet(ModelViewSet):
    queryset = shop.objects.all()
    serializer_class = shopserial
    permission_classes = [AdminOrReadonly]


class addressViewSet(ModelViewSet):
    queryset = address.objects.all()
    serializer_class = addressserial
    permission_classes = [IsAuthenticated]


class orderViewSet(ModelViewSet):
    queryset = order.objects.all()
    serializer_class = orderserial
    permission_classes = [IsAuthenticated]


class fpsViewSet(ModelViewSet):
    queryset = fps.objects.all()
    serializer_class = fpsserial
    permission_classes = [AdminOrReadonly]


class customerViewSet(ModelViewSet):
    queryset = customer.objects.all()
    serializer_class = customerserial
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAuthenticated])
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
