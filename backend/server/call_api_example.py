import requests

def call_api():
    url = "https://fluffy-olva-digital-david-9c22a71a.koyeb.app/"
    params = {
        'task': 'The impact of artificial intelligence on modern healthcare',
        'report_type': 'detailed_report',
        'report_source': 'web',
        'source_urls': ['https://example.com/source1', 'https://example.com/source2'],
        'tone': 'Formal',
        'config_path': 'path/to/config.yaml',
        'report_tone': 'Objective',
        'report_sources': ['source1', 'source2']
    }
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Response from API:", response.text)
    except requests.exceptions.RequestException as e:
        print("Error calling API:", e)

if __name__ == "__main__":
    call_api()
