from django.urls import path
from .views import add_payment,add_expense

urlpatterns = [
    path('add-payment/', add_payment, name='add_payment'),
    path('add-expense/', add_expense, name='add_expense'),
]
