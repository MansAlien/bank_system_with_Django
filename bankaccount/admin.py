from django.contrib import admin
from .models import BankAccount


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display= ["user", "account_number", "balance", "is_active", "created_at"]
    readonly_fields = ["account_number",]
    list_filter = ["is_active",]

