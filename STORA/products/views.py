from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Sum
from STORA.sales.models import SaleAttributes
from STORA.products.models import Product, Barcode, Category, Suppliers
from STORA.products.forms import ProductForms, CategoryForm, SuppliersForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class ProductListView(ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products_details.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForms
    template_name = 'products/product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForms
    template_name = 'products/product_edit.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

class BarcodeListView(ListView):
    model = Barcode
    template_name = 'products/barcodes_list.html'
    context_object_name = 'barcodes'

class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'products/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

class SuppliersListView(ListView):
    model = Suppliers
    template_name = 'products/suppliers_list.html'
    context_object_name = 'suppliers'

class SupplierCreateView(CreateView):
    model = Suppliers
    form_class = SuppliersForm
    template_name = 'products/suppliers_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Suppliers
    form_class = SuppliersForm
    template_name = 'products/suppliers_form.html'
    context_object_name = 'supplier'
    success_url = reverse_lazy('suppliers_list')

class SupplierDeleteView(DeleteView):
    model = Suppliers
    template_name = 'products/suppliers_confirm_delete.html'
    success_url = reverse_lazy('suppliers__list')

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

def custom_404(request, exception):
    return render(request, '404.html', status=404)