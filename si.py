import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import Credentials
from botocore.session import get_session

# Replace these with your actual AWS credentials
aws_access_key_id = 'your-access-key-id'
aws_secret_access_key = 'your-secret-access-key'
region = 'us-west-2'
service = 'execute-api'  # Example service name

# Create credentials object
credentials = Credentials(aws_access_key_id, aws_secret_access_key)

# Create a request
url = 'https://your-api-endpoint.amazonaws.com/your-path'
headers = {
    'Content-Type': 'application/json'
}
request = AWSRequest(method='GET', url=url, headers=headers)

# Sign the request
session = get_session()
auth = SigV4Auth(credentials, service, region)
auth.add_auth(request)

# Extract signed headers
signed_headers = dict(request.headers.items())

# Now you can use the signed headers to make your request
import requests

response = requests.get(url, headers=signed_headers)
print(response.status_code)
print(response.text)
