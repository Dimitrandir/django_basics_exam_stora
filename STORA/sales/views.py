from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from STORA.sales.forms import SaleForms, saleItemFormset
from STORA.sales.models import SaleAttributes

def sales_add(request):
    if request.method == "POST":
        form = SaleForms(request.POST)
        formset = saleItemFormset(request.POST)

        if form.is_valid() and formset.is_valid():
            sale = form.save()
            formset.instance = sale
            formset.save()
            return redirect('sale_add')
    else:

        form = SaleForms()
        formset = saleItemFormset()

    context = {'form': form, 'formset': formset}
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
        form = SaleForms(request.POST, instance=sale)
        formset = saleItemFormset(request.POST, instance=sale)
        if form.is_valid() and formset.is_valid():
            formset.save()
            form.save()
            return redirect('sales_list')
    else:
        form = SaleForms(instance=sale)
        formset = saleItemFormset(instance=sale)
    context = {'sale':sale,'form':form, 'formset': formset}
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
