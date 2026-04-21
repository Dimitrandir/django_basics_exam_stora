from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from STORA.core.session_service import get_cashier_operation_state
from STORA.products.forms import ProductForms, CategoryForm, SuppliersForm, BarcodeFormSet
from STORA.products.models import Product, Barcode, Category, Suppliers
from STORA.sales.models import SaleAttributes

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/products_details.html'
    context_object_name = 'product'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForms
    template_name = 'products/product_create.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['barcode_formset'] = BarcodeFormSet(self.request.POST)
        else:
            context['barcode_formset'] = BarcodeFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        barcode_formset = context['barcode_formset']
        self.object = form.save()

        if barcode_formset.is_valid():
            barcode_formset.instance = self.object
            barcode_formset.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForms
    template_name = 'products/product_edit.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['barcode_formset'] = BarcodeFormSet(self.request.POST, instance=self.object)
        else:
            context['barcode_formset'] = BarcodeFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        barcode_formset = context['barcode_formset']
        self.object = form.save()

        if barcode_formset.is_valid():
            barcode_formset.instance = self.object
            barcode_formset.save()

        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'products/category_form.html'
    context_object_name = 'category'
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'products/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


class SuppliersListView(LoginRequiredMixin, ListView):
    model = Suppliers
    template_name = 'products/suppliers_list.html'
    context_object_name = 'suppliers'


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Suppliers
    form_class = SuppliersForm
    template_name = 'products/suppliers_form.html'
    success_url = reverse_lazy('suppliers_list')


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Suppliers
    form_class = SuppliersForm
    template_name = 'products/suppliers_form.html'
    context_object_name = 'supplier'
    success_url = reverse_lazy('suppliers_list')


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Suppliers
    template_name = 'products/suppliers_confirm_delete.html'
    success_url = reverse_lazy('suppliers_list')

def get_cashier_operation_from_session(request):
    return request.session.get('cashier_last_operation')


@login_required
def index(request):
    total_products = Product.objects.count()
    total_sales_count = SaleAttributes.objects.count()
    total_revenue = SaleAttributes.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0

    recent_sales = SaleAttributes.objects.order_by('-time_of_sale')[:5]
    last_operation = get_cashier_operation_state(request)

    context = {
        'total_products': total_products,
        'total_sales_count': total_sales_count,
        'total_revenue': total_revenue,
        'recent_sales': recent_sales,
        'last_operation': last_operation if last_operation and last_operation.get('active') else None,
    }
    return render(request, 'index.html', context)


def custom_404(request, exception):
    return render(request, '404.html', status=404)