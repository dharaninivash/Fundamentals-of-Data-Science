import matplotlib.pyplot as plt
import numpy as np

# Data
means = [0.2474, 0.1235, 0.1737, 0.1824]
stds = [0.3314, 0.2278, 0.2836, 0.2645]
labels = ['Sample 1', 'Sample 2', 'Sample 3', 'Sample 4']
x = np.arange(len(means))

# Bar plot with error bars
bars = plt.bar(x, means, yerr=stds, capsize=10, color='skyblue', edgecolor='black')

# Add text labels
for i in range(len(bars)):
    plt.text(bars[i].get_x() + bars[i].get_width()/2, bars[i].get_height() + 0.01,
             f"{means[i]:.4f}", ha='center')

plt.xticks(x, labels)
plt.title("Mean Velocity with Standard Deviation")
plt.ylabel("Mean Velocity")
plt.grid(axis='y')
plt.show()
