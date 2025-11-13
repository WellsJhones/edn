import requests


def fetch_currency_rate():
    print("\n--- Currency Exchange Rate ---")
    currency_code = input(
        "Enter currency code (e.g., USD, EUR, GBP): ").upper()
    response = requests.get(
        f"https://economia.awesomeapi.com.br/json/last/{currency_code}-BRL")
    if response.status_code == 200:
        data = response.json().get(f"{currency_code}BRL")
        if data:
            print(f"Currency: {currency_code} to BRL")
            print(f"Current value: R$ {data['bid']}")
            print(f"High: R$ {data['high']}")
            print(f"Low: R$ {data['low']}")
            print(f"Last update: {data['create_date']}")
        else:
            print("Currency not found.")
    else:
        print("Failed to fetch currency data.")


fetch_currency_rate()
