from django.urls import path
from .views import RegisterUsers

urlpatterns = [
    path('register', RegisterUsers.as_view(), name="register-url"),  
]