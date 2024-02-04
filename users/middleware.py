from rest_framework.exceptions import PermissionDenied
from appModel.models import Expense, Budget

class UserAssociationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # If the user is authenticated, associate expenses and budgets with the user
            Expense.objects.filter(user=request.user).update(user=request.user)
            Budget.objects.filter(user=request.user).update(user=request.user)

        response = self.get_response(request)
        return response