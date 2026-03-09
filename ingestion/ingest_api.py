import requests
import json

API_URL = "https://api.sampleapis.com/futurama/episodes"

response = requests.get(API_URL)
data = response.json()

# Save API data locally
with open("../data/api_data.json", "w") as f:
    json.dump(data, f, indent=2)

print("API data ingested successfully.")
