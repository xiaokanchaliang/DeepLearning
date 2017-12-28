import matplotlib.pyplot as plt
import numpy as np
import csv

x = np.linspace(1, 1000, 1000)
y = np.random.random((1000, 13))

data=np.empty((1000,1),dtype=np.float32)

reader = csv.reader(open('geneMaxium201712272331.csv', encoding='utf-8'))

count = 0

for row in reader:
    data[count][0] = row[0]
    count = count + 1

plt.plot(np.linspace(1, 1000, 1000), data)
plt.show()
