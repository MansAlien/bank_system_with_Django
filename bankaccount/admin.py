from django.contrib import admin
from .models import BankAccount, Transaction


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display= ["user", "account_number", "balance", "is_active", "created_at"]
    readonly_fields = ["account_number",]
    list_filter = ["is_active",]

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display= ["transaction_type", "transaction_number", "amount", "created_at"]
    readonly_fields = ["transaction_number",]
    list_filter = ["transaction_type",]
