def calculate_discounted_price():
    original_price = float(input("Enter the product price: $ "))
    discount_percentage = float(input("Enter the discount percentage: "))
    discount_value = original_price * (discount_percentage / 100)
    final_price = original_price - discount_value
    print(f"Final price after discount: $ {final_price:.2f}")


calculate_discounted_price()
