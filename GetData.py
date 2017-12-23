import csv
import numpy as np

input = np.empty((1000,13))

inputReader = csv.reader(open('processDataForNormalized.csv', encoding='utf-8'))

inputRowNumber = 0

for inputRow in inputReader:
    input[inputRowNumber][0] = float(inputRow[0])
    input[inputRowNumber][1] = float(inputRow[1])
    input[inputRowNumber][2] = float(inputRow[2])
    input[inputRowNumber][3] = float(inputRow[3])
    input[inputRowNumber][4] = float(inputRow[4])
    input[inputRowNumber][5] = float(inputRow[5])
    input[inputRowNumber][6] = float(inputRow[6])
    input[inputRowNumber][7] = float(inputRow[7])
    input[inputRowNumber][8] = float(inputRow[8])
    input[inputRowNumber][9] = float(inputRow[9])
    input[inputRowNumber][10] = float(inputRow[10])
    input[inputRowNumber][11] = float(inputRow[11])
    input[inputRowNumber][12] = float(inputRow[12])
    inputRowNumber = inputRowNumber + 1

output1 = np.empty((1000,1))
output2 = np.empty((1000,1))
output3 = np.empty((1000,1))

outputReader = csv.reader(open('labelData.csv', encoding='utf-8'))

outputRowNumber = 0

for outputRow in outputReader:
    output1[outputRowNumber][0] = float(outputRow[0])
    output2[outputRowNumber][0] = float(outputRow[1])
    output3[outputRowNumber][0] = float(outputRow[2])
    outputRowNumber = outputRowNumber + 1
