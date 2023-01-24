import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
# 1000 random integers between 0 and 50
x = np.random.randint(0, 150, 1000)
# Negative Correlation with some noise
y = 100 - x + np.random.normal(0, 1, 1000)
print(np.corrcoef(x, y))
plt.scatter(x, y)
plt.show()

