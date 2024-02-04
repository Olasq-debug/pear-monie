from django.urls import path
from .views import BudgetList, BudgetDetails

urlpatterns = [
    path('list-create', BudgetList.as_view(), name="list-budgets-url"),  
    path('details/<int:pk>', BudgetDetails.as_view(), name="modify-budgets-url"),  
]