import requests

def fetch_data_from_api(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Hata : {e}")
        return None


custom_api_url = "https://www.disify.com/api/email/your@example.com"

custom_api_data = fetch_data_from_api(custom_api_url)

if custom_api_data:
    print(custom_api_data)
else:
    print("HATA.")
