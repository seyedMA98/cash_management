from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Transaction
import logging
logger = logging.getLogger(__name__)

@receiver(pre_save, sender=Transaction)
@receiver(post_delete, sender=Transaction)
def update_user_balance(sender, instance, **kwargs):
    try:
        user = instance.user
        user.balance = user.transactions.aggregate(balance=models.Sum('amount'))['balance'] or 0
        logger.info(f"{user.balance}")
        user.save()
    except Exception as e:
        logger.error(f"{e}")
