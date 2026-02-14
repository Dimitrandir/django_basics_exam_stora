from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, null=True)
    description = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Barcode(models.Model):
    code = models.CharField(max_length=13, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='barcode')

    def __str__(self):
       return f"{self.code}"


class Product(models.Model):
    internal_code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=90, unique=True, blank=False, null=False)
    delivery_price = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    sell_price = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='product')
    quantity = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return f"{self.internal_code} {self.name}"