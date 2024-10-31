import requests

def call_api():
    url = "https://fluffy-olva-digital-david-9c22a71a.koyeb.app/api/initiate_research"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "task": "Die aktuelle Entwicklung von Young Professionals in der IT in Deutschland",
        "report_type": "detailed_report",
        "agent": "multi-agent"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Response from API:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error calling API:", e)

if __name__ == "__main__":
    call_api()
