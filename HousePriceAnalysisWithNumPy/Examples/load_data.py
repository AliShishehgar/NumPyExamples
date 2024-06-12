import numpy as np

# Load the data from the CSV file
data = np.genfromtxt('data/house_prices.csv', delimiter=',', skip_header=1)

# Display the data
print("Data Loaded:")
print(data)
