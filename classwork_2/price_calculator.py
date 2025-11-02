print("welcome to the price calculator")

print("price of the shirt is $50 but today you'll be gettin a 20% off \n")
amount = int(input("Type the number of shirts you want? \n"))

discount = 50 * (1 - 0.20)
total_amount = discount * amount
print("Your final price is " +  str(total_amount ))

