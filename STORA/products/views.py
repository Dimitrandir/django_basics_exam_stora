from django.db.models import Sum, Count
from STORA.sales.models import SaleAttributes
from django.shortcuts import render, get_object_or_404, redirect
from STORA.products.models import Product, Barcode
from STORA.products.forms import ProductForms


def products_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products_list.html', context)

def product_details(request, pk):

    product = get_object_or_404(Product, pk=pk)

    context = {'product': product}
    return render(request, 'products/products_details.html', context)

def product_create(request):
    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForms()

    context = {'form': form}
    return render(request, 'products/product_create.html', context)

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForms(request.POST, instance= product)
        if form.is_valid():
            form.save()
            return redirect('product_details', pk=product.pk)
    else:
        form = ProductForms(instance=product)

    context = {'form':form, 'product':product}
    return render(request, 'products/product_edit.html', context)


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    else:
        context= {'product': product}
        return render(request, 'products/product_confirm_delete.html', context)


def barcode_list(request):
    barcodes = Barcode.objects.all()
    product_id = request.GET.get('product')
    product = None
    if product_id:
        barcodes = barcodes.filter(product_id=product_id)
        product = get_object_or_404(Product, pk=product_id)

    context = {'barcodes': barcodes, 'product': product}
    return render(request, 'products/barcodes_list.html', context)

from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def index(request):
    total_products = Product.objects.count()
    total_sales_count = SaleAttributes.objects.count()
    total_revenue = SaleAttributes.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    recent_sales = SaleAttributes.objects.order_by('-time_of_sale')[:5]

    context = {
        'total_products': total_products,
        'total_sales_count': total_sales_count,
        'total_revenue': total_revenue,
        'recent_sales': recent_sales,
    }
    return render(request, 'index.html', context)