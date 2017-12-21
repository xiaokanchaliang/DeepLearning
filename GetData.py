import csv
import numpy as np
import matplotlib.pyplot as plt

inputData = np.zeros((1000,13),dtype=np.float32)
outputData1 = np.zeros((1000,1),dtype=np.float32)
outputData2 = np.zeros((1000,1),dtype=np.float32)
outputData3 = np.zeros((1000,1),dtype=np.float32)

inputReader = csv.reader(open('inputDataFile.csv', encoding='utf-8'))
outputReader = csv.reader(open('outputDataFile.csv', encoding='utf-8'))

inputRowNumber = 0
outputRowNumber = 0

for inputRow in inputReader:
    inputData[inputRowNumber][0] = float(inputRow[0])
    inputData[inputRowNumber][1] = float(inputRow[1])
    inputData[inputRowNumber][2] = float(inputRow[2])
    inputData[inputRowNumber][3] = float(inputRow[3])
    inputData[inputRowNumber][4] = float(inputRow[4])
    inputData[inputRowNumber][5] = float(inputRow[5])
    inputData[inputRowNumber][6] = float(inputRow[6])
    inputData[inputRowNumber][7] = float(inputRow[7])
    inputData[inputRowNumber][8] = float(inputRow[8])
    inputData[inputRowNumber][9] = float(inputRow[9])
    inputData[inputRowNumber][10] = float(inputRow[10])
    inputData[inputRowNumber][11] = float(inputRow[11])
    inputData[inputRowNumber][12] = float(inputRow[12])
    inputRowNumber = inputRowNumber + 1

for outputRow in outputReader:
    outputData1[outputRowNumber][0] = float(outputRow[0])
    outputData2[outputRowNumber][0] = float(outputRow[1])
    outputData3[outputRowNumber][0] = float(outputRow[2])
    outputRowNumber = outputRowNumber + 1

