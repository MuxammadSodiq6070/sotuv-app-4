from django.db import models
from apps.users.models import User

# Create your models here.


class Shop(models.Model):
    admin = models.ForeignKey(User, on_delete=models.RESTRICT)
    branch = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(blank=True, null=True, upload_to="shop_logo/")
    phone_number = models.CharField(blank=True, max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"