print("Welcome to the currency calculator")

real = float(input("How many Real do you have? \n"))
option = input("Type the corresponding currency you want:\nType A for Dollar\nType B for Euro\n").upper()

if option == "A":
    result = round(real / 5.60, 1)
    print("You'll have $" + str(result) + " Dollar after conversion")
elif option == "B":
    result = round(real / 6.60, 1)
    print("You'll have $" + str(result) + " Euro after conversion")
else:
    print("bye bye")