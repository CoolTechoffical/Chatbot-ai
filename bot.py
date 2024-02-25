# bot.py

import json
import requests
from config import API_ID, API_HASH, BOT_TOKEN

# Example API request using requests library
url = "https://api.example.com/endpoint"
headers = {
    "API-ID": API_ID,
    "API-HASH": API_HASH,
    "Authorization": f"Bearer {BOT_TOKEN}",
}

# Make a sample API request
response = requests.get(url, headers=headers)

# Print the API response
print(response.json())
