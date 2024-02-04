# middleware.py
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponseForbidden
from rest_framework.authtoken.models import Token
from appModel.models import Expense, Budget

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request has a token in the Authorization header
        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Token '):
            token_key = auth_header.split(' ')[1]
            
            try:
                # Get the user associated with the token
                token = Token.objects.get(key=token_key)
                request.user = token.user
            except Token.DoesNotExist:
                # If token is invalid, set user to AnonymousUser
                request.user = AnonymousUser()
        else:
            # If no token provided, set user to AnonymousUser
            request.user = AnonymousUser()

        # Process the request
        response = self.get_response(request)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Associate expenses and budgets with the authenticated user
        if request.user.is_authenticated:
            Expense.objects.filter(user=None).update(user=request.user)
            Budget.objects.filter(user=None).update(user=request.user)
        else:
            # If the user is not authenticated, deny access
            return HttpResponseForbidden("Unauthorized access")

        return None
