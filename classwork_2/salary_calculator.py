print("salary calculator")
employee_number = int(input("type the id of the employer: \n"))
hours_worked = int(input("type now the amount of hours worked: \n"))
hourly_rate = float(input("how much are paid for hour: \n"))

salary = hours_worked * hourly_rate

print(f"NUMBER = {employee_number}")
print(f"SALARY = $ {salary:.2f}")
