from django.urls import path
from .views import monthly_dashboard

urlpatterns = [
    path('', monthly_dashboard, name='monthly_dashboard'),
]
