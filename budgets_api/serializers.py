from rest_framework import serializers
from appModel.models import Budget


class BudgetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Budget
        fields = ['id', 'amount', 'user', 'category']