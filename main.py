import requests

# Prompt the user for the website URL to monitor
url = input("Enter the website URL to monitor: ")

# Send a GET request to the website
try:
    response = requests.get(url)
    response.raise_for_status()
    print("Website is up and running.")

# Raise an exception if the website is down
except requests.exceptions.RequestException as e:
    print("Website is down.")
