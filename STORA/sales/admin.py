from django.contrib import admin
from STORA.sales.models import SaleAttributes
from STORA.sales.models import SaleItems


class SaleItemsInAttributes(admin.TabularInline):
    model = SaleItems
    exclude = ['total_amount']
    extra = 1

@admin.register(SaleAttributes)
class SaleAttributes(admin.ModelAdmin):
    list_display = ('id', 'time_of_sale', 'cashier', 'total_amount')
    list_filter = ('id', 'time_of_sale', 'cashier', 'total_amount')
    inlines = [SaleItemsInAttributes]

@admin.register(SaleItems)
class SaleItems(admin.ModelAdmin):
    list_display = ('sale_item_id','sale_item', 'sale_quantity', 'price_at_sale', 'total_price_row')



