import csv

def read_csv_file(filename):
    with open('data.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Replace 'data.csv' with your CSV file path
read_csv_file('data.csv')

