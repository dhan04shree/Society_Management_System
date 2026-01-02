from django import forms
from .models import MaintenancePayment, Expense
from accounts.models import User

class ExpenseForm(forms.ModelForm):

    bill = forms.ImageField(required=True)

    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'month']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['month'].widget.attrs.update({'class': 'form-control'})
        self.fields['bill'].widget.attrs.update({'class': 'form-control'})

class MaintenancePaymentForm(forms.ModelForm):
    receipt = forms.ImageField(required=True)

    class Meta:
        model = MaintenancePayment
        fields = ['member', 'amount', 'month']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['member'].queryset = User.objects.filter(role='MEMBER').order_by('flat_no')
        self.fields['member'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['month'].widget.attrs.update({'class': 'form-control'})
        self.fields['receipt'].widget.attrs.update({'class': 'form-control'})
