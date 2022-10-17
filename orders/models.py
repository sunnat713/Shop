from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from products.models import ProductModel


class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(ProductModel, related_name='order')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    country = models.CharField(max_length=30)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return f'{str(self.user.profile)}'
