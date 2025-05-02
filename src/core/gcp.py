from google.cloud import billing_v1
from google.auth import exceptions

# Billing

def get_billing_accounts():
    client = billing_v1.CloudBillingClient()
    try:
        return list(client.list_billing_accounts())
    except exceptions.GoogleAuthError as e:
        print(f"Authentication error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")