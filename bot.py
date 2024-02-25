import requests

# Replace these values with your actual API credentials
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"

# Example API request using requests library
url = "https://api.example.com/endpoint"
headers = {
    "API-ID": api_id,
    "API-HASH": api_hash,
    "Authorization": f"Bearer {bot_token}",
}

# Make a sample API request
response = requests.get(url, headers=headers)

# Print the API response
print(response.json())
