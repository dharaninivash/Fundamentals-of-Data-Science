import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Price': [192.0, 215.0, 215.0, 274.0, 112.7, 185.0, 212.0, 220.0,
              276.0, 260.0, 221.5, 255.0, 260.0, 293.0, 375.0]
}
df = pd.DataFrame(data)

# Histogram
plt.hist(df['Price'], bins=8, color='green', edgecolor='black')
plt.title("Histogram of Sale Prices")
plt.xlabel("Price ($A000)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
