from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExpensesSerializer
from appModel.models import Expense
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated



class UserPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        obj.user = request.user


class ExpensesList(APIView):
    """
    List all Expenses, or create a new expense.
    """
    permission_classes = [IsAuthenticated, UserPermissions]

    def perform_create(self, serializer):
        # Associate the user with the expense before saving
        serializer.save(user=self.request.user)

    def get(self, request, format=None):
        expenses = Expense.objects.all()
        serializer = ExpensesSerializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ExpensesDetails(APIView):
    """
    Retrieve, update or delete an expense instance.
    """
    permission_classes = [IsAuthenticated,  UserPermissions]

    def perform_create(self, serializer):
        # Associate the user with the expense before saving
        serializer.save(user=self.request.user)

    def get_object(self, pk):
        try:
            expenses = Expense.objects.get(pk=pk)
            return expenses
        except Expense.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        expense = self.get_object(pk)
        serializer = ExpensesSerializer(expense)
        return Response(serializer.data,  status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        expense = self.get_object(pk)
        serializer = ExpensesSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)