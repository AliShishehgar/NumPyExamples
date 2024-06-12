import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = np.genfromtxt('data/house_prices.csv', delimiter=',', skip_header=1)
prices = data[:, 0]  # Assuming the first column is the house price
sizes = data[:, 1]   # Assuming the second column is the size of the house

# Scatter plot of house prices vs. sizes
plt.figure(figsize=(10, 6))
plt.scatter(sizes, prices, alpha=0.5)
plt.title("House Prices vs. Size")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price")
plt.grid(True)
plt.show()

# Histogram of house prices
plt.figure(figsize=(10, 6))
plt.hist(prices, bins=20, alpha=0.7)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
