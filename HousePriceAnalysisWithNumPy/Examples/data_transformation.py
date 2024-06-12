import numpy as np

# Load the data
data = np.genfromtxt('data/house_prices.csv', delimiter=',', skip_header=1)
prices = data[:, 0]  # Assuming the first column is the house price

# Normalize the prices (Min-Max Normalization)
normalized_prices = (prices - np.min(prices)) / (np.max(prices) - np.min(prices))

# Sort the prices
sorted_prices = np.sort(prices)

print("Normalized Prices:")
print(normalized_prices)

print("Sorted Prices:")
print(sorted_prices)
