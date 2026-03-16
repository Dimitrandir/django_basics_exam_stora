from django.shortcuts import render, redirect, get_object_or_404
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

def sale_details(request, pk):
    sale = get_object_or_404(SaleAttributes, pk=pk)
    sold_items = sale.items.all()
    context = {'sale': sale,'sold_items': sold_items}
    return render(request, 'sales/sale_details.html', context)

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

def sales_list(request):
    sales = SaleAttributes.objects.all()
    context = {'sales': sales}
    return render(request, 'sales/sales_list.html', context)

def sale_delete(request, pk):
    sale = get_object_or_404(SaleAttributes, pk=pk)
    if request.method == 'POST':
        sale.delete()
        return redirect('sales_list')
    else:
        context = {'sale': sale}
        return render(request, 'sales/sale_confirm_delete.html', context)
