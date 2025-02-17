from django.urls import path
from .views import BankAccountListView

app_name = "bank_account"

urlpatterns = [
    path("bank_account/", BankAccountListView.as_view(), name="list_create_bank_accont"),
]
