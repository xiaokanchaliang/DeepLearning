import csv
import numpy as np
import matplotlib.pyplot as plt

labelData = np.empty((1000,3))

reader = csv.reader(open('qualityDataForNormalized.csv', encoding='utf-8'))

count = 0

for row in reader:
    labelData[count][0] = int(float(row[0])*10)/10
    labelData[count][1] = int(float(row[1])*10)/10
    labelData[count][2] = int(float(row[2])*10)/10
    count = count + 1

labelDataFile=open('labelData.csv','w',newline='')

labelDataWriter=csv.writer(labelDataFile)

labelDataWriter.writerows(labelData)

plt.plot(np.linspace(1, 1000, 1000), labelData)
plt.show()