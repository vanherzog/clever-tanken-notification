import requests
import json

def fetch_prices():
    url = "https://secure.clever-tanken.de/api/preise-abrufen/v2"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Ct-Hmac": "app-android 44ba216701eabe2bb223ad42e75ee1e4f457c45ab5f88d2f01dbc407c44b61cb",
        "Accept-Language": "de_DE",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; Galaxy S10 Build/SQ1D.220205.004)",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip, deflate, br"
    }

    params = {
        "campaign_switch": 0,
        "installation-id": "a134644612a0654b",
        "betriebssystem": "Android",
        "campaign_version": 1,
        "geraet": "Galaxy S10",
        "betriebssystemversion": "12",
        "app-version": "7.3.0_r9598c181a",
        "spritsortengruppe": 3,
        "ort": "Lohmar 53797",
        "radius": 5,
        "veraltete": 1,
        "limit": 50,
        "payment_only": 0
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching prices: {e}")
        return None

def main():
    prices_data = fetch_prices()

    if prices_data:
        # Assuming the prices are already sorted in descending order as per the requirement
        first_price = float(prices_data["tankstellen"][0]["preis"]["preis"])
        
        # Print the JSON data for GitHub Actions to capture as output
        print(json.dumps(prices_data))

        # Check if the first price is below 1.55
        if first_price < 1.55:
            print(f"Price below 1.55 detected: {first_price}")
        else:
            print("Price not below 1.55")
    else:
        print("No price data fetched")

if __name__ == "__main__":
    main()
