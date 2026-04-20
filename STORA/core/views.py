from django.shortcuts import redirect

from STORA.core.session_service import clear_cashier_operation_state


def clear_cashier_operation(request):
    clear_cashier_operation_state(request)
    return redirect('sales_list')