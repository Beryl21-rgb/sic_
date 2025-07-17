import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.violinplot(data)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Violin Plot")
plt.show()