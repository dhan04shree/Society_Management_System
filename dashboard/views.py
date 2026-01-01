from django.shortcuts import render
from finance.models import MaintenancePayment, Expense
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

@login_required
def monthly_dashboard(request):
    month = request.GET.get('month')

    payments = MaintenancePayment.objects.all()
    expenses = Expense.objects.all()

    if month:
        payments = payments.filter(month=month)
        expenses = expenses.filter(month=month)

    total_income = payments.aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    context = {
        'payments': payments,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    }

    return render(request, 'dashboard/monthly_dashboard.html', context)