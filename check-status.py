import requests

successful_requests = 0
failed_requests = 0

# Prompt the user for the website URL to monitor
url = input("Enter the website URL to monitor: ")
# Prompt the user for the number of requests to send
num_requests = int(input("Enter the number of requests to send: "))

while successful_requests + failed_requests < num_requests:
    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()
        successful_requests += 1
        print("Website is up and running.")
        print("Response time: ", response.elapsed.total_seconds(), " seconds")

    # Raise an exception if the website is down
    except requests.exceptions.RequestException as e:
        failed_requests += 1
        print("Website is down.")
        print("Failed requests: ", failed_requests)
