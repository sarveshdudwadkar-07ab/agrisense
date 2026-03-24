from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=255)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    image = models.URLField(blank=True, null=True)   # NEW FIELD

    recommended_for = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity


class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"