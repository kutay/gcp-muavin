from tabulate import tabulate

from services import list_billing_accounts


print(tabulate(list_billing_accounts.list_accounts(), headers="keys"))
