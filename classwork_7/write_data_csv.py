import csv


def write_csv(file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "City"])
        writer.writerow(["Alice", 28, "New York"])
        writer.writerow(["Bob", 35, "Los Angeles"])
        writer.writerow(["Clara", 22, "Chicago"])

# Example usage:
# write_csv("people.csv")
