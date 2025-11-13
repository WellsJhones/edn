def calculate_tip():
    bill_amount = float(input("Enter the total bill amount: $ "))
    tip_percentage = float(input("Enter the desired tip percentage: "))
    tip = bill_amount * (tip_percentage / 100)
    print(f"Tip amount: $ {tip:.2f}")


calculate_tip()
