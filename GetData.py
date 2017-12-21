import csv
import numpy as np

inputData = np.zeros((1000,13),dtype=np.float32)

outputData1 = np.zeros((1000,1),dtype=np.float32)
outputData2 = np.zeros((1000,1),dtype=np.float32)
outputData3 = np.zeros((1000,1),dtype=np.float32)

labelData1 = np.zeros((1000,1),dtype=np.int32)
labelData2 = np.zeros((1000,1),dtype=np.int32)
labelData3 = np.zeros((1000,1),dtype=np.int32)

inputReader = csv.reader(open('input.csv', encoding='utf-8'))
outputReader = csv.reader(open('output.csv', encoding='utf-8'))
labelReader = csv.reader(open('label.csv', encoding='utf-8'))

inputRowNumber = 0
outputRowNumber = 0
labelRowNumber = 0

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

for labelRow in labelReader:
    labelData1[labelRowNumber][0] = float(labelRow[0])
    labelData2[labelRowNumber][0] = float(labelRow[1])
    labelData3[labelRowNumber][0] = float(labelRow[2])
    labelRowNumber = labelRowNumber + 1

