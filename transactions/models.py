from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Sum

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=100)
    date = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        income_balance = Transaction.objects.filter(user=self.user, type='income').aggregate(income_balance=Sum('amount'))['income_balance'] or 0
        expense_balance = Transaction.objects.filter(user=self.user, type='expense').aggregate(expense_balance=Sum('amount'))['expense_balance'] or 0

        # Update the user's balance
        self.user.balance = income_balance-expense_balance
        self.user.save()

    def __str__(self):
        return f"{self.type} - {self.amount} ({self.date})"
