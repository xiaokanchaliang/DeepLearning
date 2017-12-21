import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 1000, 1000)
y = np.random.random((1000, 13))

data=np.zeros((1000,1),dtype=np.float32)

for i in range(1000):
    data[i][0] = y[i][0]

plt.plot(np.linspace(1, 1000, 1000), data)
plt.show()
