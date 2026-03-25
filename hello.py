import numpy as np

# Sample data (list of numbers)
data = [12, 15, 14, 10, 18, 20, 14, 17, 19, 13]

# Calculate mean, median, and standard deviation
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)

# Output the results
print(f"Data: {data}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
