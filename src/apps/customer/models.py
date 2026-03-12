from django.db import models

# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, blank=True
    )
    comment = models.TextField(null=True, blank=True)
    wallet = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)