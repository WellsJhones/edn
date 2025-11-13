import requests


def lookup_address_by_cep():
    print("\n--- Address Lookup by CEP ---")
    cep = input("Enter CEP (only numbers): ").strip()
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if response.status_code == 200:
        data = response.json()
        if "erro" in data:
            print("Invalid CEP.")
        else:
            print(f"Street: {data['logradouro']}")
            print(f"Neighborhood: {data['bairro']}")
            print(f"City: {data['localidade']}")
            print(f"State: {data['uf']}")
    else:
        print("Failed to fetch address.")


lookup_address_by_cep()
