import csv
import numpy as np

input = np.zeros((1000,13),dtype=np.float32)

inputReader = csv.reader(open('input.csv', encoding='utf-8'))

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

output1 = np.zeros((1000,10),dtype=np.int32)
output2 = np.zeros((1000,10),dtype=np.int32)
output3 = np.zeros((1000,10),dtype=np.int32)

output1Reader = csv.reader(open('output1.csv', encoding='utf-8'))
output2Reader = csv.reader(open('output2.csv', encoding='utf-8'))
output3Reader = csv.reader(open('output3.csv', encoding='utf-8'))

output1RowNumber = 0
output2RowNumber = 0
output3RowNumber = 0

for outputRow1 in output1Reader:
    output1[output1RowNumber][0] = int(outputRow1[0])
    output1[output1RowNumber][1] = int(outputRow1[1])
    output1[output1RowNumber][2] = int(outputRow1[2])
    output1[output1RowNumber][3] = int(outputRow1[3])
    output1[output1RowNumber][4] = int(outputRow1[4])
    output1[output1RowNumber][5] = int(outputRow1[5])
    output1[output1RowNumber][6] = int(outputRow1[6])
    output1[output1RowNumber][7] = int(outputRow1[7])
    output1[output1RowNumber][8] = int(outputRow1[8])
    output1[output1RowNumber][9] = int(outputRow1[9])
    output1RowNumber = output1RowNumber + 1

for outputRow2 in output2Reader:
    output2[output2RowNumber][0] = int(outputRow2[0])
    output2[output2RowNumber][1] = int(outputRow2[1])
    output2[output2RowNumber][2] = int(outputRow2[2])
    output2[output2RowNumber][3] = int(outputRow2[3])
    output2[output2RowNumber][4] = int(outputRow2[4])
    output2[output2RowNumber][5] = int(outputRow2[5])
    output2[output2RowNumber][6] = int(outputRow2[6])
    output2[output2RowNumber][7] = int(outputRow2[7])
    output2[output2RowNumber][8] = int(outputRow2[8])
    output2[output2RowNumber][9] = int(outputRow2[9])
    output2RowNumber = output2RowNumber + 1

for outputRow3 in output3Reader:
    output3[output3RowNumber][0] = int(outputRow3[0])
    output3[output3RowNumber][1] = int(outputRow3[1])
    output3[output3RowNumber][2] = int(outputRow3[2])
    output3[output3RowNumber][3] = int(outputRow3[3])
    output3[output3RowNumber][4] = int(outputRow3[4])
    output3[output3RowNumber][5] = int(outputRow3[5])
    output3[output3RowNumber][6] = int(outputRow3[6])
    output3[output3RowNumber][7] = int(outputRow3[7])
    output3[output3RowNumber][8] = int(outputRow3[8])
    output3[output3RowNumber][9] = int(outputRow3[9])
    output3RowNumber = output3RowNumber + 1

outputLabel1 = np.zeros((1000,1),dtype=np.int32)
outputLabel2 = np.zeros((1000,1),dtype=np.int32)
outputLabel3 = np.zeros((1000,1),dtype=np.int32)

outputLabelReader = csv.reader(open('outputLabel.csv', encoding='utf-8'))

outputLabelRowNumber = 0

for outputLabelRow in outputLabelReader:
    outputLabel1[outputLabelRowNumber][0] = int(outputLabelRow[0])
    outputLabel2[outputLabelRowNumber][0] = int(outputLabelRow[1])
    outputLabel3[outputLabelRowNumber][0] = int(outputLabelRow[2])
    outputLabelRowNumber = outputLabelRowNumber + 1
