import re


def check_palindrome():
    text = input("Enter a word or phrase to check for palindrome: ")
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    result = "Yes" if cleaned_text == cleaned_text[::-1] else "No"
    print(f"Is it a palindrome? {result}")


check_palindrome()
