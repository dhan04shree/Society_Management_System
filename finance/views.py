from django.shortcuts import render, redirect
from .forms import MaintenancePaymentForm,ExpenseForm
from django.contrib.auth.decorators import login_required
import cloudinary
@login_required
def add_payment(request):
    if request.user.role != 'ADMIN':
        return redirect('/')
    if request.method == 'POST':
        form = MaintenancePaymentForm(request.POST, request.FILES)
        if form.is_valid():
            receipt_file = request.FILES['receipt']

            upload = cloudinary.uploader.upload(
                receipt_file,
                folder="payment"
            )

            payment = form.save(commit=False)
            payment.receipt_url = upload['secure_url']
            payment.added_by = request.user
            payment.save()
            return redirect('monthly_dashboard')
    else:
        form = MaintenancePaymentForm()

    return render(request, 'finance/add_payment.html', {'form': form})

@login_required
def add_expense(request):
    if request.user.role != 'ADMIN': 
        return redirect('/')  

    if request.method == 'POST': 
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            bill_file = request.FILES['bill']

            upload = cloudinary.uploader.upload(
                bill_file,
                folder="expenses"
            )

            expense = form.save(commit=False)
            expense.bill_url = upload['secure_url']
            expense.added_by = request.user
            expense.save()
            return redirect('monthly_dashboard')
    else:
        form = ExpenseForm()

    return render(request, 'finance/add_expense.html', {'form': form})
