from django.contrib import admin
from .models import User, Expense, ExpensesCategory, BudgetsCategory, Budget

# Register your models here.

admin.site.register(User)
admin.site.register(Expense)
admin.site.register(Budget)
admin.site.register(ExpensesCategory)
admin.site.register(BudgetsCategory)

