from azure.storage.blob import BlobServiceClient
import os

account_name = os.environ.get("AZURE_SA_NAME")
account_key = os.environ.get("AZURE_SA_KEY")

try:
    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)
    # List containers to verify access
    containers = blob_service_client.list_containers()
    for container in containers:
        print(container.name)
    print("Connection successful")
except Exception as e:
    print(f"Error: {e}")
