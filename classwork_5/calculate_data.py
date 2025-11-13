from datetime import datetime


def calculate_age_in_days():
    birth_year = int(input("Enter your birth year (e.g., 1990): "))
    today = datetime.now()
    birth_date = datetime(birth_year, 1, 1)
    age_days = (today - birth_date).days
    print(f"Your age in days: {age_days}")


calculate_age_in_days()
