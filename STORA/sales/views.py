from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from STORA.sales.forms import SaleForms, SaleItemFormSet
from STORA.sales.models import SaleAttributes
from STORA.products.models import Product, Barcode

def sales_add(request):
    products_data = list(
        Product.objects.values('id', 'internal_code', 'name', 'sell_price')
    )
    barcodes_data = list(
        Barcode.objects.values('code', 'product_id')
    )

    formset_prefix = 'items'

    if request.method == "POST":
        form = SaleForms(request.POST, current_user=request.user)
        formset = SaleItemFormSet(request.POST, prefix=formset_prefix)

        if form.is_valid() and formset.is_valid():
            sale = form.save(commit=False)
            sale.cashier = request.user
            sale.save()

            formset.instance = sale
            formset.save()
            sale.save()
            return redirect('sales_list')


    else:
        form = SaleForms(current_user=request.user)
        formset = SaleItemFormSet(prefix=formset_prefix)

    context = {
        'form': form,
        'formset': formset,
        'formset_prefix': formset_prefix,
        'products_data': products_data,
        'barcodes_data': barcodes_data,
    }
    return render(request, 'sales/sale_add.html', context)


class SalesDetailView(DetailView):
    model = SaleAttributes
    template_name = 'sales/sale_details.html'
    context_object_name = 'sale'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sold_items'] = self.object.items.all()
        return context

def sale_edit(request, pk):
    sale = get_object_or_404(SaleAttributes, pk=pk)
    if request.method == 'POST':
        form = SaleForms(request.POST, instance=sale, current_user=request.user)
        formset = SaleItemFormSet(request.POST, instance=sale)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('sales_list')
    else:
        form = SaleForms(instance=sale, current_user=request.user)
        formset = SaleItemFormSet(instance=sale)

    context = {'sale': sale, 'form': form, 'formset': formset}
    return render(request, 'sales/sale_edit.html', context)

class SalesListView(ListView):
    model = SaleAttributes
    template_name = 'sales/sales_list.html'
    context_object_name = 'sales'

class SalesDeleteView(DeleteView):
    model = SaleAttributes
    template_name = 'sales/sale_confirm_delete.html'
    context_object_name = 'sale'
    success_url = reverse_lazy('sales_list')
