from django.apps import apps
import random
import string


class Generator:

    @staticmethod
    def generate_account_number():
        model = apps.get_model("bankaccount", "BankAccount")
        while True:
            unique_part = ''.join(random.choices(string.digits, k=12))
            account_number = f"EG{unique_part}"
            if not model.objects.filter(account_number=account_number).exists():
                return account_number
