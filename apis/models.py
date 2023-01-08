from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField
    product_category = models.CharField(max_length=255, default='none')


class Category(models.Model):
    name = models.CharField(max_length=255)
