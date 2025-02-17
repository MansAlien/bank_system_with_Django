from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction

@receiver(post_save, sender=Transaction)
def update_account_balance(sender, instance, created, **kwargs):
    if created and instance.transaction_type == Transaction.TransactionType.DEPOSIT:
        account = instance.account
        account.balance += instance.amount
        account.save()

    elif created and instance.transaction_type == Transaction.TransactionType.WITHDRAWAL:
        account = instance.account
        account.balance -= instance.amount
        account.save()
