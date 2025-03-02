from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .utils import Generator


class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bank_account")
    account_number = models.CharField(max_length=15, unique=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, validators=[MinValueValidator(0.00)])
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "BankAccount"
        constraints = [
            models.CheckConstraint(
                check= models.Q(balance__gte=0),
                name="check_account_balance_gte_zero"
            )
        ]

        indexes = [
            models.Index(fields=["balance"])
        ]

    def __str__(self):
        return f"{self.user.username} - {self.account_number} - {self.balance}"

    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = Generator.generate_account_number()
        super().save(*args, **kwargs)


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        DEPOSIT = 'dp', 'Deposit'
        WITHDRAWAL = 'wd', 'Withdrawal'

    transaction_number = models.CharField(max_length=12, unique=True, blank=True)
    transaction_type = models.CharField(max_length=2, choices=TransactionType.choices)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} - {self.account.account_number}"

    def clean(self):
        if self.transaction_type == Transaction.TransactionType.WITHDRAWAL and self.account.balance < self.amount:
            raise ValidationError("You don't have enouph balance to complete this transaction")

    def save(self, *args, **kwargs):
        self.clean()
        if not self.transaction_number:
            self.transaction_number = Generator.generate_transaction_number()
        super().save(*args, **kwargs)

    class Meta:
        db_table = "Transaction"
        ordering = ["-created_at"]

