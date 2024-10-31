import requests

def call_api():
    url = "https://fluffy-olva-digital-david-9c22a71a.koyeb.app/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Response from API:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error calling API:", e)

if __name__ == "__main__":
    call_api()
