
from core import gcp

def map_account(account):
    return {
        'name': account.name,
        'display_name': account.display_name,
        'open': account.open,
        'master_billing_account': account.master_billing_account,
    }

def list_accounts():
    billing_accounts = gcp.get_billing_accounts()
    accounts = [map_account(acc) for acc in billing_accounts]
    return accounts
