import csv
import random

def generate_random_data(num_rows):
    data = [["Price", "Size", "Bedrooms", "Age"]]
    for _ in range(num_rows):
        price = random.randint(100000, 1000000)
        size = random.randint(500, 5000)
        bedrooms = random.randint(1, 6)
        age = random.randint(0, 50)
        data.append([price, size, bedrooms, age])
    return data

# Generate 100 rows of data
data = generate_random_data(100)

# File path to save the CSV file
file_path = 'data/house_prices.csv'

# Create the CSV file and write the data
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file created with {len(data) - 1} rows at {file_path}")
