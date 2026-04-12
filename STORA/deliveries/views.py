from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from STORA.deliveries.forms import DeliveryForms, DeliveryItemFormSet
from STORA.deliveries.models import DeliveryAttributes
from STORA.products.models import Product, Barcode

def deliveries_add(request):
    products_data = list(
        Product.objects.values('id', 'internal_code', 'name', 'sell_price')
    )
    barcodes_data = list(
        Barcode.objects.values('code', 'product_id')
    )

    formset_prefix = 'items'

    if request.method == "POST":
        form = DeliveryForms(request.POST, current_user=request.user)
        formset = DeliveryItemFormSet(request.POST, prefix=formset_prefix)

        if form.is_valid() and formset.is_valid():
            delivery = form.save(commit=False)
            delivery.receiver = request.user
            delivery.save()

            formset.instance = delivery
            formset.save()
            delivery.save()
            return redirect('deliveries_list')


    else:
        form = DeliveryForms(current_user=request.user)
        formset = DeliveryItemFormSet(prefix=formset_prefix)

    context = {
        'form': form,
        'formset': formset,
        'formset_prefix': formset_prefix,
        'products_data': products_data,
        'barcodes_data': barcodes_data,
    }
    return render(request, 'deliveries/delivery_add.html', context)

class DeliveryDetailView(DetailView):
    model = DeliveryAttributes
    template_name = 'deliveries/delivery_details.html'
    context_object_name = 'delivery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delivered_items'] = self.object.items.all()
        return context

class DeliveryListView(ListView):
    model = DeliveryAttributes
    template_name = 'deliveries/deliveries_list.html'
    context_object_name = 'deliveries'

class DeliveryDeleteView(DeleteView):
    model = DeliveryAttributes
    template_name = 'deliveries/delivery_confirm_delete.html'
    context_object_name = 'delivery'
    success_url = reverse_lazy('deliveries_list')
