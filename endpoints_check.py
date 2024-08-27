import requests

def check_google_endpoint():
    url = "https://www.google.com"
    try:
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            print(f"{url} is reachable. Status Code: {response.status_code}")
        else:
            print(f"{url} is reachable but returned a non-200 status. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to reach {url}. Error: {e}")

check_google_endpoint()
