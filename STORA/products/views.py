from django.db.models import Sum, Count
from STORA.sales.models import SaleAttributes
from django.shortcuts import render, get_object_or_404, redirect
from STORA.products.models import Product, Barcode, Category, Suppliers
from STORA.products.forms import ProductForms, CategoryForm, SuppliersForm


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


def category_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'products/category_list.html', context)


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    context = {'form': form}
    return render(request, 'products/category_form.html', context)


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    context = {'form': form, 'category': category}
    return render(request, 'products/category_form.html', context)


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    context = {'category': category}
    return render(request, 'products/category_confirm_delete.html', context)


def suppliers_list(request):
    suppliers = Suppliers.objects.all()
    context = {'suppliers': suppliers}
    return render(request, 'products/suppliers_list.html', context)


def suppliers_create(request):
    if request.method == 'POST':
        form = SuppliersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suppliers_list')
    else:
        form = SuppliersForm()

    context = {'form': form}
    return render(request, 'products/suppliers_form.html', context)


def suppliers_edit(request, pk):
    supplier = get_object_or_404(Suppliers, pk=pk)

    if request.method == 'POST':
        form = SuppliersForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('suppliers_list')
    else:
        form = SuppliersForm(instance=supplier)

    context = {'form': form, 'supplier': supplier}
    return render(request, 'products/suppliers_form.html', context)


def suppliers_delete(request, pk):
    supplier = get_object_or_404(Suppliers, pk=pk)

    if request.method == 'POST':
        supplier.delete()
        return redirect('suppliers_list')

    context = {'supplier': supplier}
    return render(request, 'products/suppliers_confirm_delete.html', context)


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