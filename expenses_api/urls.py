from django.urls import path
from .views import ExpensesList, ExpensesDetails

urlpatterns = [
    path('list-create', ExpensesList.as_view(), name="list-expenses-url"),  
    path('details/<int:pk>', ExpensesDetails.as_view(), name="modify-expenses-url"),  
]