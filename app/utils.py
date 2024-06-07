import csv

def write_to_csv(data):
    with open('app/data/users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            grocery_items = [row for row in reader]
        return grocery_items
    except FileNotFoundError:
        return []

