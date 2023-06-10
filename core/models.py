from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import usermanager


class User(AbstractUser):
    phone = models.CharField(
        max_length=15,
        unique=True,
        help_text="Enter a valid number with country code",
    )
    # username = models.CharField(max_length=15, blank=True)
    OTP = models.CharField(max_length=6, blank=True)
    choice = [("customer", "customer"), ("seller", "seller")]
    profile = models.CharField(max_length=8, choices=choice, default="customer")
    username = models.CharField(max_length=50, blank=True)
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []
    object = usermanager()
