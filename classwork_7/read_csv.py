import csv


def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))

# Example usage:
# read_csv("people.csv")
