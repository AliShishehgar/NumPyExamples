import numpy as np

# Load the data
data = np.genfromtxt('data/house_prices.csv', delimiter=',', skip_header=1)
prices = data[:, 0]  # Assuming the first column is the house price

# Calculate basic statistics
mean_price = np.mean(prices)
median_price = np.median(prices)
std_price = np.std(prices)

print(f"Mean Price: {mean_price}")
print(f"Median Price: {median_price}")
print(f"Standard Deviation of Prices: {std_price}")
