from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField("Category Name", max_length=200)


class Product(models.Model):
    name = models.CharField("Product Name", max_length=200)
    description = models.CharField("Product Name", max_length=200)
    price = models.FloatField("Price", max_length=10, default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
