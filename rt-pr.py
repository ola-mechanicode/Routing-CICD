import requests

# Define global variables for stage and API key
STAGE = 'stg'  # or 'prod', 'dev', etc., depending on your deployment stage
FUNCTION_KEY = 'function_key_here'  # Replace with your actual API key or token

def query_endpoint(base_url, stage, api_key):
    # Construct the full URL with stage and API key
    url = f"{base_url}{stage}/api/health?code={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        # Print the successful response content or do other processing here
        print("Response Status Code:", response.status_code)
        print("Response Body:", response.text)
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops: Something Else", err)

# Base URL for the routing processor API (without stage or API key)
BASE_URL = 'https://routing-processor-'
query_endpoint(BASE_URL, STAGE, FUNCTION_KEY)
