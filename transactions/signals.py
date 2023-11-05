from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaction

@receiver(post_save, sender=Transaction)
@receiver(post_delete, sender=Transaction)
def update_user_balance(sender, instance, **kwargs):
    user = instance.user
    user.balance = user.transactions.aggregate(balance=models.Sum('amount'))['balance'] or 0
    user.save()
