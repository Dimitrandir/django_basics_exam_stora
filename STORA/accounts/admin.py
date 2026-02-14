from django.contrib import admin
from STORA.accounts.models import Employee
from STORA.products.models import Category, Product, Barcode

admin.site.register(Employee)

class BarcodeInProductsAdmin(admin.TabularInline):
    model = Barcode
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [BarcodeInProductsAdmin]
    list_display = ('internal_code', 'name', 'category', 'delivery_price', 'sell_price')
    search_fields = ('internal_code', 'name',)

admin.site.register(Category)


