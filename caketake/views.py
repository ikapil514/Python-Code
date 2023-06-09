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
    adminfpsserial,
    adminorderserial,
    adminproductserial,
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
    permission_classes = [AdminOrReadonly]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return adminproductserial
        return productserial


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
    permission_classes = [AdminOrReadonly]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return adminfpsserial
        return fpsserial


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


# from django.utils import timezone


class orderViewSet(ModelViewSet):
    queryset = order.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return adminorderserial
        return orderserial

    # def get_queryset(self,*args,**kwargs):
    #     start_time = self.request.GET.get("start_time",None)
    #     end_time = self.request.GET.get("end_time",None)
    #     if start_time and end_time :
    #         # convert timestamps to timezone objects
    #         start_time_instance = timezone.datetime.fromtimestamp(start_time)
    #         end_time_instance = timezone.datetime.fromtimestamp(end_time)
    #         return self.queryset.filter(start_time=start_time_instance,end_time_instance=end_time_instance)
    #     return self.queryset
