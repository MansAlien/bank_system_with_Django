from rest_framework import serializers 
from .models import BankAccount, Transaction
from .services import ManageBankAccount

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'
        read_only_fields = ["account_number", "is_active", "balance"]

    def create(self, validated_data):
        return ManageBankAccount.create_bank_account(**validated_data)
