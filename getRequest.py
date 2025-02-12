import json
import requests
from requests_aws4auth import AWS4Auth

# Replace these with your AWS credentials and details
aws_access_key_id = ""
aws_secret_access_key = ""
region = "us-east-1"
datastore_id = ""

# HealthLake endpoint for Patient creation
url = f"https://healthlake.{region}.amazonaws.com/datastore/{datastore_id}/r4/Patient/"

# AWS4Auth for signing requests
auth = AWS4Auth(
    aws_access_key_id,
    aws_secret_access_key,
    region,
    "healthlake"
)

# Headers
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}



# Make the POST request
response = requests.get(
    url,
    auth=auth,
    headers=headers
)

# Output the response
print(f"Status Code: {response.status_code}")
try:
    print(f"Response: {response.json()}")
except json.JSONDecodeError:
    print("Response:", response.text)
