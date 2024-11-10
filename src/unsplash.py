# src/unsplash.py
import requests


def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
print("Image downloaded Successfully...")
def get_random_background(api_key, download_path):
    print("Fetching a random background image..")
    unsplash_url = "https://api.unsplash.com/photos/random"
    params = {
        'client_id': api_key,
        'query': 'nature',
        'orientation': 'landscape',
        'count': 1,
    }
    response = requests.get(unsplash_url, params=params)
    data = response.json()
    if data and len(data) > 0:
        image_url = data[0]['urls']['full']
        download_image(image_url, download_path)
        return download_path
    return None
