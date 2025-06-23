import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data
data = {
    'Area': [694, 905, 802, 1366, 716, 963, 821, 714, 1018, 887,
             790, 696, 771, 1006, 1191],
    'Price': [192.0, 215.0, 215.0, 274.0, 112.7, 185.0, 212.0, 220.0,
              276.0, 260.0, 221.5, 255.0, 260.0, 293.0, 375.0]
}
df = pd.DataFrame(data)
df['LogPrice'] = np.log(df['Price'])

# Plot Log Price vs Area
plt.scatter(df['Area'], df['LogPrice'], color='purple')
plt.title("Log(Sale Price) vs Area")
plt.xlabel("Area (ha)")
plt.ylabel("Log Price")
plt.grid(True)
plt.show()

# Histogram of Log Prices
plt.hist(df['LogPrice'], bins=8, color='orange', edgecolor='black')
plt.title("Histogram of Log Sale Prices")
plt.xlabel("Log Price")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
