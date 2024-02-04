from rest_framework import serializers
from appModel.models import Expense


class ExpensesSerializer(serializers.ModelSerializer):
    # map_expense = serializers.PrimaryKeyRelatedField(many=True, queryset=Expense.objects.all())
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'user', 'category',]