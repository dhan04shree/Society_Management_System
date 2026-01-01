from django.contrib import admin
from .models import MaintenancePayment, Expense


@admin.register(MaintenancePayment)
class MaintenancePaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount', 'month', 'payment_mode', 'paid_on')
    list_filter = ('month', 'payment_mode')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'month', 'added_by', 'created_at')
    list_filter = ('month', 'category')
