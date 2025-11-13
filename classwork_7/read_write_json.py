import json


def write_json(file_path):
    person = {
        "name": "John",
        "age": 30,
        "city": "San Francisco"
    }
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(person, file, ensure_ascii=False, indent=4)


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"City: {data['city']}")


# Example usage:
# write_json("person.json")
# read_json("person.json")
