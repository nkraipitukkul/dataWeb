import requests

# The URL of your Flask API
url = "http://54.164.159.198/anime_recommendation"

# Data to be sent in JSON format
data = {
    "anime_name": "Oshi no Ko"
}

# Sending a POST request and saving the response
response = requests.post(url, json=data)
print(response)
# Printing the response
print(response.json())
