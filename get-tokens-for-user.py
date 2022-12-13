# Given the client ID and tenant ID for an app registered in Azure,
# along with an Azure username and password,
# provide an Azure AD access token and a refresh token.

# If the caller is not already signed in to Azure, the caller's
# web browser will prompt the caller to sign in first.

# pip install msal
from msal import PublicClientApplication
import sys

# You can hard-code the registered app's client ID and tenant ID here,
# along with the Azure username and password,
# or you can provide them as command-line arguments to this script.
client_id = '<client-id>'
tenant_id = '<tenant-id>'
username = '<username>'
password = '<password>'

# Do not modify this variable. It represents the programmatic ID for
# Azure Databricks along with the default scope of '/.default'.
scope = [ '2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default' ]

# Check for too few or too many command-line arguments.
if (len(sys.argv) > 1) and (len(sys.argv) != 5):
  print("Usage: get-tokens-for-user.py <client ID> <tenant ID> <username> <password>")
  exit(1)

# If the registered app's client ID and tenant ID along with the
# Azure username and password are provided as command-line variables,
# set them here.
if len(sys.argv) > 1:
  client_id = sys.argv[1]
  tenant_id = sys.argv[2]
  username = sys.argv[3]
  password = sys.argv[4]

app = PublicClientApplication(
  client_id = client_id,
  authority = "https://login.microsoftonline.com/" + tenant_id
)

acquire_tokens_result = app.acquire_token_by_username_password(
  username = username,
  password = password,
  scopes = scope
)

if 'error' in acquire_tokens_result:
  print("Error: " + acquire_tokens_result['error'])
  print("Description: " + acquire_tokens_result['error_description'])
else:
  print("Access token:\n")
  print(acquire_tokens_result['access_token'])
  print("\nRefresh token:\n")
  print(acquire_tokens_result['refresh_token'])