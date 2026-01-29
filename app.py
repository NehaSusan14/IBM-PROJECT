import requests
import os
import uuid


# The complete API endpoint URL for this flow
url = "https://aws-us-east-2.langflow.datastax.com/lf/631841a6-ef57-4472-a0b3-1daeb903e05a/api/v1/run/c21ff5be-b17d-49b2-9a47-f63ba810729c"

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "hello world!"
}
payload["session_id"] = str(uuid.uuid4())

headers = {
    "X-DataStax-Current-Org": "bfadc8d3-4aa0-45f3-87db-c8ac2f7c8fd0", 
    "Authorization": "Bearer <YOUR_APPLICATION_TOKEN>",
    "Content-Type": "application/json", 
    "Accept": "application/json",
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
