def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        year = int(input("Enter the year you want to check: "))
        if is_leap_year(year):
            print(f"The year {year} is a leap year.")
        else:
            print(f"The year {year} is not a leap year.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
