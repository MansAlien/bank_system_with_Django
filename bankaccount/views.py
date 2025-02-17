from rest_framework import generics
from .serializers import BankAccountSerializer
from .services import ManageBankAccount



class BankAccountListView(generics.ListCreateAPIView):
    queryset = ManageBankAccount.get_all_bank_accounts()
    serializer_class = BankAccountSerializer
