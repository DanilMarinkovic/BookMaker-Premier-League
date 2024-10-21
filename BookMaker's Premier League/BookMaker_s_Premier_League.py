import requests

# Your API key (replace with your actual API key)
API_KEY = '021b157aa4893f56e5236a0d77b103ab'

# Define the endpoint URL
url = "https://api.the-odds-api.com/v4/sports/soccer_epl/"

# Define parameters to pass to the API, including your API key
params = {
    'apiKey': API_KEY  # Insert your API key here
}

# Send GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the sports data
    print(data)
else:
    # Print error message if the request failed
    print(f"Error: {response.status_code} - {response.text}")
