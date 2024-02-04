from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BudgetSerializer
from rest_framework import status
from appModel.models import Budget
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


class UserPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        obj.owner = request.user


class BudgetList(APIView):
    """
    List all Expenses, or create a new budgets.
    """
    permission_classes = [IsAuthenticated, UserPermissions]
    def get(self, request, format=None):
        budgets = Budget.objects.all()
        serializer = BudgetSerializer(budgets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = BudgetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BudgetDetails(APIView, UserPermissions):
    """
    Retrieve, update or delete a budgets instance.
    """
    permission_classes = [IsAuthenticated, UserPermissions]
    def get_object(self, pk):
        try:
            return Budget.objects.get(pk=pk)
        except Budget.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        budget = self.get_object(pk)
        serializer = BudgetSerializer(budget)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        budget = self.get_object(pk)
        serializer = BudgetSerializer(budget, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        budget = self.get_object(pk)
        budget.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)