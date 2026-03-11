from django.db import models
from apps.product.models import Product

class Order(models.Model):
    PAYMENT_METHODS = [('cash', 'Naqd'), ('card', 'Karta')]
    
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_METHODS, default='cash')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.total_price} UZS"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2) # Sotilgan paytdagi narxi

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"