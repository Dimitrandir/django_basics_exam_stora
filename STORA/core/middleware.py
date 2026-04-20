from STORA.core.utils import get_cashier_operation_session_key


class CashierOperationSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            session_key = get_cashier_operation_session_key()
            operation_state = request.session.get(session_key)

            if operation_state:
                request.session[session_key] = operation_state
                request.session.modified = True

        return response
