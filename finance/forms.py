from django import forms
from .models import MaintenancePayment
from accounts.models import User
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'month', 'bill']  # include bill for receipt

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['month'].widget.attrs.update({'class': 'form-control'})
        self.fields['bill'].widget.attrs.update({'class': 'form-control'})

class MaintenancePaymentForm(forms.ModelForm):
    class Meta:
        model = MaintenancePayment
        fields = ['member', 'amount', 'month', 'receipt']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Only show members (not admin) in dropdown
        self.fields['member'].queryset = User.objects.filter(role='member').order_by('flat_no')
        self.fields['month'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['member'].widget.attrs.update({'class': 'form-control'})
        self.fields['receipt'].widget.attrs.update({'class': 'form-control'})
