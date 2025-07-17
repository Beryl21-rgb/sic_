import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

data = np.random.randn(1000)

plt.hist(data, bins=30, color='green', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

sizes = [30, 20, 25, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['blue', 'red', 'green', 'purple']

# Create pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.show(