from django.db import models


from STORA.accounts.models import Employee
from STORA.products.models import Product

class SaleAttributes(models.Model):
    cacher = models.ForeignKey(Employee,on_delete=models.PROTECT,related_name='sales')
    time_of_sale = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cacher} {self.time_of_sale}"

class SaleItems(models.Model):
    sale = models.ForeignKey(SaleAttributes, on_delete=models.CASCADE, related_name='items')
    sale_item = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='sold_items')
    sale_quantity = models.PositiveIntegerField(default=1)
    price_at_sale = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2)


    def __str__(self):
        return f"{self.sale_item_id} {self.sale_item.name} {self.sale_quantity} {self.price_at_sale}"

