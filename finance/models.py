from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

MONTH_CHOICES = [
    ('January 2026', 'January 2026'),
    ('February 2026', 'February 2026'),
    ('March 2026', 'March 2026'),
    ('April 2026', 'April 2026'),
    ('May 2026', 'May 2026'),
    ('June 2026', 'June 2026'),
    ('July 2026', 'July 2026'),
    ('August 2026', 'August 2026'),
    ('September 2026', 'September 2026'),
    ('October 2026', 'October 2026'),
    ('November 2026', 'November 2026'),
    ('December 2026', 'December 2026'),
]
class MaintenancePayment(models.Model):
    PAYMENT_MODES = (
        ('CASH', 'Cash'),
        ('UPI', 'UPI'),
        ('BANK', 'Bank Transfer'),
    )

    member = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODES)
    receipt = models.ImageField(upload_to='payments/')
    paid_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"+₹{self.amount} - Flat {self.member.flat_no} ({self.month})"
    
class Expense(models.Model):
    CATEGORY_CHOICES = (
        ('LIFT', 'Lift Repair'),
        ('CLEANING', 'Cleaning'),
        ('SECURITY', 'Security'),
        ('ELECTRICITY', 'Electricity'),
        ('OTHER', 'Other'),
    )

    title = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    month = models.CharField(max_length=20, choices=MONTH_CHOICES)
    bill = models.ImageField(upload_to='expenses/')
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"-₹{self.amount} {self.title} ({self.month})"
