from django.core.validators import MinValueValidator, RegexValidator
from django.db import models



class Suppliers(models.Model):
    name = models.CharField(max_length=60, unique=True)
    bulstat = models.CharField(max_length=12,validators=[RegexValidator(regex='^\d+$',
                                                                          message='VAT must contain only digits',
                                                                          code='invalid_vat')], unique=True,
                               verbose_name='BULSTAT')

    vat_n = models.CharField(blank= True, max_length=14, validators=[RegexValidator(regex='^BG\d+$',
                                                                          message='VAT must contain only digits',
                                                                          code='invalid_vat')], verbose_name='VAT:',
                             help_text='Only if the company is VAT registered!')

    phone = models.CharField(max_length=10, blank=True, verbose_name='Phone number')
    email = models.EmailField(blank=True, verbose_name='Email address')

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, null=True)
    description = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Barcode(models.Model):
    code = models.CharField(max_length=13, null=True, blank=True, verbose_name='Barcode number',
                            help_text='Scan the barcode or enter the EAN-13 number')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='barcode',
                                verbose_name='Linked Product')

    class Meta:
        verbose_name = "Barcode"
        verbose_name_plural = "Barcodes"

    def __str__(self):
       return f"{self.code}"


class Product(models.Model):
    internal_code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=90, unique=True, blank=False, null=False, verbose_name='product name')
    delivery_price = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2,
                                         verbose_name='delivery price')
    sell_price = models.DecimalField(blank=True, validators=[MinValueValidator(0.01)],null=True, max_digits=9,
                                     decimal_places=2, verbose_name='sale price', help_text="Selling price per unit")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='product')
    quantity = models.IntegerField(default=0, blank=True, verbose_name='stock quantity',
                                   help_text='Can be negative if items are sold before delivery is recorded')
    supplier = models.ManyToManyField(Suppliers, blank=True, related_name='products')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['internal_code']

    def __str__(self):
        return self.name