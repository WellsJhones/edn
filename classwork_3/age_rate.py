print("This program will classify a person by their age. Please type your age below:\n")

age = int(input("Age: \n"))

if age > 0 and age < 12:
    print("You're a child.")
elif age >= 12 and age < 18:
    print("You're a teenager.")
elif age >= 18 and age < 57:
    print("You're an adult.")
elif age >= 57 and age < 120:
    print("You're elderly.")
else:
    print("Sorry, try again.")
