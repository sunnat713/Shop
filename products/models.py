from datetime import datetime
from django.utils.translation import gettext_lazy as _
import pytz
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class BrandModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class ProductTagModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('product tag')
        verbose_name_plural = _('product tags')


class ProductSizeModel(models.Model):
    title = models.CharField(max_length=3, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class ProductColorModel(models.Model):
    code = models.CharField(max_length=10, verbose_name=_('code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, related_name='products',
                                 verbose_name=_('category'))
    brand = models.ForeignKey(BrandModel, on_delete=models.PROTECT, related_name='products', verbose_name=_('brand'))
    tags = models.ManyToManyField(ProductTagModel, related_name='products', verbose_name=_('tags'))
    title = models.CharField(max_length=255, verbose_name=_('title'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(verbose_name=_("real price"), default=0)
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)],
                                           verbose_name=_('discount'))
    sizes = models.ManyToManyField(ProductSizeModel, related_name='products')
    colors = models.ManyToManyField(ProductColorModel, related_name='products')
    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = RichTextUploadingField(verbose_name=_('long_description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_related_products(self):
        # return self.category.products.exclude(pk=self.pk)
        return ProductModel.objects.filter(category_id=self.category_id).exclude(pk=self.pk)

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0

    def is_new(self):
        diff = datetime.now(pytz.timezone('Asia/Tashkent')) - self.created_at
        return diff.days <= 3

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images', verbose_name=_('product'))
    image = models.ImageField(upload_to='products', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')

