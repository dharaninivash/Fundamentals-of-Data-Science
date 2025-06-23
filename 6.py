import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    'Area': [694, 905, 802, 1366, 716, 963, 821, 714, 1018, 887,
             790, 696, 771, 1006, 1191],
    'Price': [192.0, 215.0, 215.0, 274.0, 112.7, 185.0, 212.0, 220.0,
              276.0, 260.0, 221.5, 255.0, 260.0, 293.0, 375.0]
}
df = pd.DataFrame(data)

# Plot
plt.scatter(df['Area'], df['Price'], color='blue')
plt.title("Sale Price vs Area")
plt.xlabel("Area (ha)")
plt.ylabel("Price ($A000)")
plt.grid(True)
plt.show()
