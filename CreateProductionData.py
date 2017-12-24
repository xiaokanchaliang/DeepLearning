import numpy as np
import csv

processData = np.empty((1000,13))
qualityData = np.empty((1000,3))

processReader = csv.reader(open('processDataForNormalized.csv', encoding='utf-8'))
qualityReader = csv.reader(open('qualityDataForNormalized.csv', encoding='utf-8'))

processCount = 0
qualityCount = 0

for processRow in processReader:
    processData[processCount][0] = (1350 - 1100) * float(processRow[0]) + 1100
    processData[processCount][1] = (1000 - 500) * float(processRow[1]) + 500
    processData[processCount][2] = (1300 - 800) * float(processRow[2]) + 800
    processData[processCount][3] = (0 - -15) * float(processRow[3]) + -15
    processData[processCount][4] = (-5 - -45) * float(processRow[4]) + -45
    processData[processCount][5] = (1200 - 600) * float(processRow[5]) + 600
    processData[processCount][6] = (1350 - 650) * float(processRow[6]) + 650
    processData[processCount][7] = (1350 - 650) * float(processRow[7]) + 650
    processData[processCount][8] = (120 - 30) * float(processRow[8]) + 30
    processData[processCount][9] = (-5 - -45) * float(processRow[9]) + -45
    processData[processCount][10] = (1200 - 400) * float(processRow[10]) + 400
    processData[processCount][11] = (1200 - 650) * float(processRow[11]) + 650
    processData[processCount][12] = (25 - 0) * float(processRow[12]) + 0
    processCount = processCount + 1

for qualityRow in qualityReader:
    qualityData[qualityCount][0] = (1.65 - 1.5) * float(qualityRow[0]) + 1.5
    qualityData[qualityCount][1] = (0.85 - 0.25) * float(qualityRow[1]) + 0.25
    qualityData[qualityCount][2] = (14.5 - 6.1) * float(qualityRow[2]) + 6.1
    qualityCount = qualityCount + 1

processDataFile=open('processDataForProduced.csv','w',newline='')
qualityDataFile=open('qualityDataForProduced.csv','w',newline='')

processDataWriter=csv.writer(processDataFile)
qualityDataWriter=csv.writer(qualityDataFile)

processDataWriter.writerows(processData)
qualityDataWriter.writerows(qualityData)