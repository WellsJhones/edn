def calculate_total_payment(name, fixed_salary, total_sales):
    commission = total_sales * 0.15
    total_payment = fixed_salary + commission
    return total_payment

def main():
    try:
        name = input("Enter the salesperson's first name: ")
        fixed_salary = float(input("Enter the fixed salary: "))
        total_sales = float(input("Enter the total sales amount: "))

        total = calculate_total_payment(name, fixed_salary, total_sales)
        print(f"TOTAL = R$ {total:.2f}")
    except ValueError:
        print("Please enter valid numeric values for salary and sales.")

if __name__ == "__main__":
    main()
