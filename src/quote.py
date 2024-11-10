import requests

print("Fetching a random quote..")
def get_random_stoic_quote():
    api_url = "https://stoic-quotes.com/api/quote"
    response = requests.get(api_url)
    data = response.json()
    print(data)
    return data.get("text"), data.get("author")