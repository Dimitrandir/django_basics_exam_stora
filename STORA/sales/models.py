from django.db import models
from django.core.validators import MinValueValidator


from STORA.accounts.models import Employee
from STORA.products.models import Product

class SaleAttributes(models.Model):
    cashier = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='sales',
                                verbose_name='Cashier')
    time_of_sale = models.DateTimeField(auto_now_add=True, verbose_name='Sale Time')
    total_amount = models.DecimalField(default=0.00, decimal_places=2, max_digits=12)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        total_sum = 0
        for item in self.items.all():
           total_sum += item.total_price_row or 0
        self.total_amount = total_sum
        super().save(update_fields=['total_amount'])


    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

    def __str__(self):
        return f"{self.cashier} {self.time_of_sale}"

class SaleItems(models.Model):
    sale = models.ForeignKey(SaleAttributes, on_delete=models.CASCADE, related_name='items',
                             verbose_name='Sale Reference')
    sale_item = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sold_items',
                                  verbose_name='Product')
    sale_quantity = models.PositiveIntegerField(default=1,validators=[MinValueValidator(1)] ,
                                                verbose_name='Quantity Sold')
    price_at_sale = models.DecimalField(blank=True, null= True, max_digits=9, decimal_places=2,
                                        verbose_name='Unit Price at Sale',
                                        help_text='Price of the product at the moment of sale')
    total_price_row = models.DecimalField(blank=True, null= True, max_digits=9, decimal_places=2,
                                        verbose_name='Total price',
                                        help_text='Total price of the current article')

    def save(self, *args, **kwargs):
        if not self.price_at_sale:
            self.price_at_sale = self.sale_item.sell_price
        tpr = self.sale_quantity * self.price_at_sale
        self.total_price_row = tpr
        self.sale_item.quantity -= self.sale_quantity
        self.sale_item.save()
        super().save(*args, **kwargs)



    class Meta:
        verbose_name = 'Sale Item'
        verbose_name_plural = 'Sales Items'

    def __str__(self):
        return f"{self.sale_item_id} {self.sale_item.name} {self.sale_quantity} {self.price_at_sale}"

