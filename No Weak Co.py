import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
x = np.random.randint(0, 50, 1000)
y = np.random.randint(0, 50, 1000)
print(np.corrcoef(x, y))
plt.scatter(x, y, color='green')
plt.show()
