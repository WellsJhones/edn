def convert_temperature(value, source, target):
    source = source.lower()
    target = target.lower()

    # Convert source to Celsius
    if source == "celsius":
        celsius = value
    elif source == "fahrenheit":
        celsius = (value - 32) * 5/9
    elif source == "kelvin":
        celsius = value - 273.15
    else:
        raise ValueError("Invalid source unit.")

    # Convert Celsius to target
    if target == "celsius":
        return celsius
    elif target == "fahrenheit":
        return celsius * 9/5 + 32
    elif target == "kelvin":
        return celsius + 273.15
    else:
        raise ValueError("Invalid target unit.")

def main():
    try:
        value = float(input("Enter the temperature: "))
        source = input("Enter the source unit (Celsius, Fahrenheit, Kelvin): ")
        target = input("Enter the target unit (Celsius, Fahrenheit, Kelvin): ")

        result = convert_temperature(value, source, target)
        print(f"{value} {source.capitalize()} is equal to {result:.2f} {target.capitalize()}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
