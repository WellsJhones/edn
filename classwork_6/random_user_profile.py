import requests


def fetch_random_user():
    print("\n--- Random User Profile ---")
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        data = response.json()['results'][0]
        name = f"{data['name']['first']} {data['name']['last']}"
        email = data['email']
        country = data['location']['country']
        print(f"Name: {name}\nEmail: {email}\nCountry: {country}")
    else:
        print("Failed to fetch user data.")


fetch_random_user()
