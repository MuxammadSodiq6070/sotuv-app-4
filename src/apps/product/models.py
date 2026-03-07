from django.db import models
from apps.shop.models import Shop


# Create your models here.



class Category(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    products_count = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    



class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.Image 

     