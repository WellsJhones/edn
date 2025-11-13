import random
import string


def generate_password():
    print("\n--- Random Password Generator ---")
    length = int(input("Enter desired password length: "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated password: {password}")


generate_password()
