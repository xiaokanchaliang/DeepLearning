import numpy as np
import csv

inputData=np.random.random((1000,13))
outputData=np.zeros((1000,3),dtype=np.float32)

noise1=np.random.uniform(-0.1,0.1,1000)
noise2=np.random.uniform(-0.1,0.1,1000)
noise3=np.random.uniform(-0.1,0.1,1000)

for i in range(1000):
    outputData[i][0]=inputData[i][0]*0.2+inputData[i][1]*0.05+inputData[i][2]*0.05+inputData[i][3]*0.1+inputData[i][4]*0.1+inputData[i][5]*0.1+inputData[i][6]*0.05+inputData[i][7]*0.15+inputData[i][8]*0.15+inputData[i][9]*0.05+inputData[i][10]*0+inputData[i][11]*0+inputData[i][12]*0+noise1[i]
    outputData[i][1]=inputData[i][0]*0+inputData[i][1]*0+inputData[i][2]*0.17+inputData[i][3]*0.03+inputData[i][4]*0.1+inputData[i][5]*0+inputData[i][6]*0.13+inputData[i][7]*0.07+inputData[i][8]*0.1+inputData[i][9]*0.1+inputData[i][10]*0.17+inputData[i][11]*0.03+inputData[i][12]*0.1+noise2[i]
    outputData[i][2]=inputData[i][0]*0.13+inputData[i][1]*0.07+inputData[i][2]*0.1+inputData[i][3]*0.1+inputData[i][4]*0+inputData[i][5]*0+inputData[i][6]*0.05+inputData[i][7]*0.05+inputData[i][8]*0.17+inputData[i][9]*0.03+inputData[i][10]*0.1+inputData[i][11]*0.1+inputData[i][12]*0.1+noise3[i]

inputDataFile=open('input.csv','w',newline='')
outputDataFile=open('output.csv','w',newline='')
inputWriter=csv.writer(inputDataFile)
outputWriter=csv.writer(outputDataFile)
inputWriter.writerows(inputData)
outputWriter.writerows(outputData)

processData=np.zeros((1000,13),dtype=np.int32)
qualityData=np.zeros((1000,3),dtype=np.float32)

for i in range(1000):
    processData[i][0] = (1350-1100) * inputData[i][0]+1100
    processData[i][1] = (1000-500) * inputData[i][1]+500
    processData[i][2] = (1300-800) * inputData[i][2]+800
    processData[i][3] = (0--15) * inputData[i][3]+-15
    processData[i][4] = (-5--45) * inputData[i][4]+-45
    processData[i][5] = (1200-600) * inputData[i][5]+600
    processData[i][6] = (1350-650) * inputData[i][6]+650
    processData[i][7] = (1350-650) * inputData[i][7]+650
    processData[i][8] = (120-30) * inputData[i][8]+30
    processData[i][9] = (-5--45) * inputData[i][9]+-45
    processData[i][10] = (1200-400) * inputData[i][10]+400
    processData[i][11] = (1200-650) * inputData[i][11]+650
    processData[i][12] = (25-0) * inputData[i][12]+0

    qualityData[i][0] = (1.65-1.5) * outputData[i][0]+1.5
    qualityData[i][1] = (0.85-0.25) * outputData[i][1]+0.25
    qualityData[i][2] = (14.5-6.1) * outputData[i][2]+6.1

processDataFile=open('process.csv','w',newline='')
qualityDataFile=open('quality.csv','w',newline='')
processWriter=csv.writer(processDataFile)
qualityWriter=csv.writer(qualityDataFile)
processWriter.writerows(processData)
qualityWriter.writerows(qualityData)
