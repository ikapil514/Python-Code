from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.product)
class productadmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    list_per_page = 50
    search_fields = ["name"]


@admin.register(models.shop)
class shopadmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "original_name",
        # "addresss",
    ]


@admin.register(models.customer)
class customeradmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "addresss",
    ]


@admin.register(models.order)
class orderadmin(admin.ModelAdmin):
    list_display = [
        "placed_at",
        "food_type",
        "delivery_type",
        "pay_type",
        "payment_status",
        "order_status",
    ]


@admin.register(models.address)
class addressadmin(admin.ModelAdmin):
    list_display = [
        "tittle",
        "city",
        "street",
        "landmark",
        "zip",
        # "location",
        "customer",
        # "shop",
    ]
