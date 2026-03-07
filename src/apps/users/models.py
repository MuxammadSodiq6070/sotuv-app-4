from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)

    REQUIRED_FIELDS = ["phone_number"]

    def __str__(self):
        return f"{self.phone_number}, {self.get_full_name()}"





class Role(models.TextChoices):
    SELLER = 'seller', "Sotuvchi"
    ADMIN = 'admin', "Admin"
    MANAGER = 'manager', "Manager"

class Stuff(models.Model):
    shop = models.ForeignKey("shop.Shop", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    role = models.CharField(max_length=50, choices=Role.choices)
    avatar = models.ImageField(blank=True, null=True)
    todays_income = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user}, {self.role}"
