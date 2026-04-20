from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from STORA.core.session_service import (
    clear_cashier_operation_state,
    extract_formset_state,
    get_cashier_operation_state,
    set_cashier_operation_state,
)
from STORA.core.utils import build_cashier_operation_state, build_restore_formset_data
from STORA.deliveries.forms import DeliveryForms, DeliveryItemFormSet
from STORA.deliveries.models import DeliveryAttributes
from STORA.products.models import Product, Barcode
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def deliveries_add(request):
    products_data = list(Product.objects.values('id', 'internal_code', 'name', 'delivery_price'))
    barcodes_data = list(Barcode.objects.values('code', 'product_id'))

    formset_prefix = 'items'
    state = get_cashier_operation_state(request)
    delivery_draft = None
    formset_initial = []

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

            clear_cashier_operation_state(request)
            return redirect('deliveries_list')

        extracted_state = extract_formset_state(request.POST, formset_prefix)
        delivery_draft = build_cashier_operation_state(
            operation_type='delivery',
            path=request.path,
            data={
                'receiver': request.POST.get('receiver', ''),
                'supplier': request.POST.get('supplier', ''),
                'time_of_delivery': request.POST.get('time_of_delivery', ''),
                'document_type': request.POST.get('document_type', ''),
                'document_number': request.POST.get('document_number', ''),
                'document_date': request.POST.get('document_date', ''),
            },
            formset_data=extracted_state,
            active=True,
        )
        set_cashier_operation_state(request, delivery_draft)

        form = DeliveryForms(request.POST, current_user=request.user)
        formset_initial = extracted_state.get('forms', [])
        formset = DeliveryItemFormSet(
            request.POST,
            prefix=formset_prefix,
            initial=formset_initial,
        )
    else:
        if state and state.get('type') == 'delivery' and state.get('active'):
            form = DeliveryForms(initial=state.get('data', {}), current_user=request.user)
            formset_initial = state.get('formset_data', {}).get('forms', []) or [{}]
            restore_post_data = build_restore_formset_data(formset_prefix, formset_initial)

            formset = DeliveryItemFormSet(
                data=restore_post_data,
                prefix=formset_prefix,
            )
            delivery_draft = state
        else:
            form = DeliveryForms(current_user=request.user)
            formset = DeliveryItemFormSet(prefix=formset_prefix)

    context = {
        'form': form,
        'formset': formset,
        'formset_prefix': formset_prefix,
        'products_data': products_data,
        'barcodes_data': barcodes_data,
        'delivery_draft': delivery_draft,
        'delivery_formset_initial_count': len(formset_initial) if formset_initial else 0,
    }
    return render(request, 'deliveries/delivery_add.html', context)


@require_POST
def delivery_draft_save(request):
    payload = json.loads(request.body.decode('utf-8'))
    form_data = payload.get('form_data', {})
    formset_data = payload.get('formset_data', {})

    draft = build_cashier_operation_state(
        operation_type='delivery',
        path='/deliveries/add/',
        data=form_data,
        formset_data=formset_data,
        active=True,
    )
    set_cashier_operation_state(request, draft)
    return JsonResponse({'status': 'ok'})


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


def delivery_edit(request, pk):
    delivery = get_object_or_404(DeliveryAttributes, pk=pk)

    products_data = list(Product.objects.values('id', 'internal_code', 'name', 'delivery_price'))
    barcodes_data = list(Barcode.objects.values('code', 'product_id'))

    formset_prefix = 'items'

    if request.method == "POST":
        form = DeliveryForms(request.POST, instance=delivery)
        formset = DeliveryItemFormSet(request.POST, instance=delivery, prefix=formset_prefix)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            delivery.save()
            return redirect('delivery_details', pk=delivery.pk)
    else:
        form = DeliveryForms(instance=delivery)
        formset = DeliveryItemFormSet(instance=delivery, prefix=formset_prefix)

    context = {
        'delivery': delivery,
        'form': form,
        'formset': formset,
        'formset_prefix': formset_prefix,
        'products_data': products_data,
        'barcodes_data': barcodes_data,
    }
    return render(request, 'deliveries/delivery_edit.html', context)


class DeliveryDeleteView(DeleteView):
    model = DeliveryAttributes
    template_name = 'deliveries/delivery_confirm_delete.html'
    context_object_name = 'delivery'
    success_url = reverse_lazy('deliveries_list')

