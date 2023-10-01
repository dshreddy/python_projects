import csv

csv_file_path = '/Users/donthuboyinasaihemanthreddy/Downloads/Brave Passwords.csv'
passwords_dict = {}

with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        site = row['name']  # Change 'name' to the actual column name in your CSV
        username = row['username']  # Change 'username' to the actual column name in your CSV
        password = row['password']  # Change 'password' to the actual column name in your CSV
        passwords_dict[site] = {'username': username, 'password': password}

print(passwords_dict)
