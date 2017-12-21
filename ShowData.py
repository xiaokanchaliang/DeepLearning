import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 1000, 1000)
y = np.random.random((1000, 13))
plt.plot(np.linspace(1, 1000, 1000), y)
plt.show()
