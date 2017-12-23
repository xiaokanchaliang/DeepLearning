import numpy as np
import csv

input=np.random.random((1000,13))
outputData=np.zeros((1000,3),dtype=np.float32)
outputLable=np.zeros((1000,3),dtype=np.int32)

output1=np.zeros((1000,10),dtype=np.int32)
output2=np.zeros((1000,10),dtype=np.int32)
output3=np.zeros((1000,10),dtype=np.int32)

noise1=np.random.uniform(-0.1,0.1,1000)
noise2=np.random.uniform(-0.1,0.1,1000)
noise3=np.random.uniform(-0.1,0.1,1000)

for i in range(1000):
    outputData[i][0]=input[i][0]*0.2+input[i][1]*0.05+input[i][2]*0.05+input[i][3]*0.1+input[i][4]*0.1+input[i][5]*0.1+input[i][6]*0.05+input[i][7]*0.15+input[i][8]*0.15+input[i][9]*0.05+input[i][10]*0+input[i][11]*0+input[i][12]*0+noise1[i]
    outputData[i][1]=input[i][0]*0+input[i][1]*0+input[i][2]*0.17+input[i][3]*0.03+input[i][4]*0.1+input[i][5]*0+input[i][6]*0.13+input[i][7]*0.07+input[i][8]*0.1+input[i][9]*0.1+input[i][10]*0.17+input[i][11]*0.03+input[i][12]*0.1+noise2[i]
    outputData[i][2]=input[i][0]*0.13+input[i][1]*0.07+input[i][2]*0.1+input[i][3]*0.1+input[i][4]*0+input[i][5]*0+input[i][6]*0.05+input[i][7]*0.05+input[i][8]*0.17+input[i][9]*0.03+input[i][10]*0.1+input[i][11]*0.1+input[i][12]*0.1+noise3[i]

    outputLable[i][0] = int(outputData[i][0]*10)
    outputLable[i][1] = int(outputData[i][1]*10)
    outputLable[i][2] = int(outputData[i][2]*10)

inputFile=open('input.csv','w',newline='')
outputDataFile=open('outputData.csv','w',newline='')
outputLableFile=open('outputLabel.csv','w',newline='')
inputWriter=csv.writer(inputFile)
outputWriter=csv.writer(outputDataFile)
outputLableWriter=csv.writer(outputLableFile)
inputWriter.writerows(input)
outputWriter.writerows(outputData)
outputLableWriter.writerows(outputLable)

processData=np.zeros((1000,13),dtype=np.int32)
qualityData=np.zeros((1000,3),dtype=np.float32)

for i in range(1000):
    processData[i][0] = (1350-1100) * input[i][0]+1100
    processData[i][1] = (1000-500) * input[i][1]+500
    processData[i][2] = (1300-800) * input[i][2]+800
    processData[i][3] = (0--15) * input[i][3]+-15
    processData[i][4] = (-5--45) * input[i][4]+-45
    processData[i][5] = (1200-600) * input[i][5]+600
    processData[i][6] = (1350-650) * input[i][6]+650
    processData[i][7] = (1350-650) * input[i][7]+650
    processData[i][8] = (120-30) * input[i][8]+30
    processData[i][9] = (-5--45) * input[i][9]+-45
    processData[i][10] = (1200-400) * input[i][10]+400
    processData[i][11] = (1200-650) * input[i][11]+650
    processData[i][12] = (25-0) * input[i][12]+0

    qualityData[i][0] = (1.65-1.5) * outputData[i][0]+1.5
    qualityData[i][1] = (0.85-0.25) * outputData[i][1]+0.25
    qualityData[i][2] = (14.5-6.1) * outputData[i][2]+6.1

processDataFile=open('processData.csv','w',newline='')
qualityDataFile=open('qualityData.csv','w',newline='')
processWriter=csv.writer(processDataFile)
qualityWriter=csv.writer(qualityDataFile)
processWriter.writerows(processData)
qualityWriter.writerows(qualityData)

print(outputLable)