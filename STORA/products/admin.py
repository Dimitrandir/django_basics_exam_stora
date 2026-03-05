from django.contrib import admin

from STORA.products.models import Category, Product, Barcode, Suppliers

class BarcodeInProductsAdmin(admin.TabularInline):
    model = Barcode
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [BarcodeInProductsAdmin]
    list_display = ('internal_code', 'name', 'category', 'delivery_price', 'sell_price')
    search_fields = ('internal_code', 'name',)
    filter_horizontal = ('supplier',)

admin.site.register(Category)

admin.site.register(Suppliers)


