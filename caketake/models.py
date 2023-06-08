from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.conf import settings

# from django.contrib.gis.db import models as gmodel


class fps(models.Model):
    price = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(1)]
    )
    flavour = models.CharField(max_length=50)
    weight = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="* in pounds",
    )
    floor_size = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    making_time = models.TimeField(default="01:30")
    product = models.ForeignKey("product", on_delete=models.CASCADE)
    # order = models.ForeignKey("order", on_delete=models.CASCADE, related_name="fsf")


class product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="cake/image.img", default="")
    more_images = models.ImageField(upload_to="morecake/image.img", default="")
    adult = models.BooleanField(verbose_name=("Adult"), default=False)
    food_veg = "V"
    food_nonveg = "NV"
    food_both = "V&N"
    food_choice = [
        (food_veg, "Veg"),
        (food_nonveg, "Non-veg"),
        (food_both, "Veg&Non-veg"),
    ]
    food_type = models.CharField(max_length=3, choices=food_choice)
    active = models.BooleanField(verbose_name=("active"), default=False)
    created_at = models.DateField(auto_now=True)
    shop = models.ForeignKey("shop", on_delete=models.PROTECT, related_name="products")

    def __str__(self):
        return self.name

    # shop class = shops
    # order class = orders


class shop(models.Model):
    shop_name = models.CharField(max_length=250)
    original_name = models.CharField(max_length=250)

    def __str__(self):
        return self.shop_name

    # address class = addresss
    # product class = products


class customer(models.Model):
    email = models.EmailField(unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # address class = addresss
    # order class = orders

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name


class order(models.Model):
    placed_at = models.DateField(auto_now_add=True)
    any_request = models.TextField(null=True, blank=True)
    food_choice = [("Veg", "Veg"), ("Non-Veg", "Non-Veg")]
    food_type = models.CharField(max_length=8, choices=food_choice)
    delivery_choice = [("Self Pickup", "Self Pickup"), ("DP", "DP")]
    delivery_type = models.CharField(
        max_length=15, choices=delivery_choice, default="Self Pickup"
    )
    pay_choice = [("Cash", "Cash"), ("Online", "Online")]
    pay_type = models.CharField(max_length=8, choices=pay_choice, default="Cash")
    payment_pending = "P"
    payment_complete = "C"
    payment_choice = [
        (payment_pending, "Pending"),
        (payment_complete, "Complete"),
    ]
    payment_status = models.CharField(
        max_length=1, choices=payment_choice, default=payment_pending
    )
    order_not_confirmed = "NC"
    order_confirmed = "C"
    order_reject = "R"
    order_failed = "F"
    order_abendant = "AB"
    order_choice = [
        (order_not_confirmed, "Not_Confirmed"),
        (order_confirmed, "Confirmed"),
        (order_reject, "Rejected"),
        (order_failed, "Failed"),
        (order_abendant, "Abendant"),
    ]
    order_status = models.CharField(
        max_length=2, choices=order_choice, default=order_not_confirmed
    )
    customer = models.ForeignKey(
        customer, on_delete=models.PROTECT, related_name="orders"
    )
    product = models.ForeignKey(
        product, on_delete=models.PROTECT, related_name="orders"
    )

    # fps = models.ForeignKey(fps, on_delete=models.PROTECT, related_name="orders")``
    class Meta:
        permissions = [("cancel_order", "Can cancel order")]


class address(models.Model):
    tittle = models.CharField(max_length=250, null=True)
    zip = models.PositiveIntegerField(default="223344")
    street = models.CharField(max_length=250, default="Sector")
    city = models.CharField(max_length=250, default="HMH")
    landmark = models.CharField(max_length=250, default="")

    customer = models.OneToOneField(
        customer, on_delete=models.CASCADE, related_name="addresss", primary_key=True
    )


class rating(models.Model):
    description = models.TextField()
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(
        product, on_delete=models.CASCADE, related_name="ratings"
    )
