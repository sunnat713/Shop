from datetime import datetime

import pytz
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BrandModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ProductTagModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product tag'
        verbose_name_plural = 'product tags'


class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, related_name='products')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    short_description = models.TextField()
    long_description = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

