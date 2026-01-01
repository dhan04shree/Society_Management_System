from django.shortcuts import render, redirect
from .forms import MaintenancePaymentForm,ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required
def add_payment(request):
    # temporarily allow all users
    if request.user.role != 'ADMIN':  # only admin can add
        return redirect('/')
    if request.method == 'POST':
        form = MaintenancePaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('monthly_dashboard')
    else:
        form = MaintenancePaymentForm()

    return render(request, 'finance/add_payment.html', {'form': form})

@login_required
def add_expense(request):
    if request.user.role != 'ADMIN':  # only admin can add
        return redirect('/')  

    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)  # include request.FILES
        if form.is_valid():
            expense = form.save(commit=False)
            expense.added_by = request.user
            expense.save()
            return redirect('monthly_dashboard')
    else:
        form = ExpenseForm()

    return render(request, 'finance/add_expense.html', {'form': form})
