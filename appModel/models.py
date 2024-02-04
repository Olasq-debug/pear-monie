from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import  RegexValidator

# Create your models here.

#Model for expenses category
class ExpensesCategory(models.Model):
    name = models.CharField(max_length = 100, blank=False)

    def __str__(self):
        return self.name

#Model for expenses
class Expense(models.Model):
    amount = models.IntegerField(default= 0)
    category = models.ForeignKey(ExpensesCategory, on_delete=models.PROTECT, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='map_expense')
    description = models.TextField(max_length = 255)
    createdAt = models.DateTimeField(default=timezone.now)


#Model for for budgets
class BudgetsCategory(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name
    
#Budgets Model
class Budget(models.Model):
    amount = models.IntegerField(default=0)
    category = models.ForeignKey(BudgetsCategory, on_delete=models.PROTECT, )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='map_budgets')

    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length= 255, unique=True)
    email = models.CharField(max_length= 255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'{self.username}'


