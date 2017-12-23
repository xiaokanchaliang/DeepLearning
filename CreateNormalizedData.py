import csv
import numpy as np

processData = np.random.random((1000,13))

qualityData = np.zeros((1000,3), dtype=np.float32)

noiseData1 = np.random.uniform(-0.1,0.1,1000)
noiseData2 = np.random.uniform(-0.1,0.1,1000)
noiseData3 = np.random.uniform(-0.1,0.1,1000)

for i in range(1000):
    qualityData[i][0] = processData[i][0]*0.3 + processData[i][1]*0.1 + processData[i][2]*0.05 + processData[i][3]*0.25 + processData[i][4]*0.15 + processData[i][10]*0.15 + noiseData1[i]
    qualityData[i][1] = processData[i][5]*0.3 + processData[i][6]*0.1 + processData[i][7]*0.05 + processData[i][8]*0.25 + processData[i][9]*0.15 + processData[i][11]*0.15 + noiseData2[i]
    qualityData[i][2] = processData[i][3]*0.3 + processData[i][4]*0.1 + processData[i][5]*0.05 + processData[i][6]*0.25 + processData[i][7]*0.15 + processData[i][12]*0.15 + noiseData3[i]

processDataFile=open('processDataForNormalized.csv','w',newline='')
qualityDataFile=open('qualityDataForNormalized.csv','w',newline='')

processDataWriter=csv.writer(processDataFile)
qualityDataWriter=csv.writer(qualityDataFile)

processDataWriter.writerows(processData)
qualityDataWriter.writerows(qualityData)
