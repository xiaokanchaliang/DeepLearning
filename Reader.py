import csv
from sklearn.cluster import KMeans

processReader = csv.reader(open('process.csv', encoding='utf-8'))
qualityReader = csv.reader(open('quality.csv', encoding='utf-8'))

processRowList = [row for row in processReader]
qualityRowList = [row for row in qualityReader]

processDataList = [[] for i in range(0, 1000)]
qualityDataList = [[] for i in range(0, 1000)]

for i in range(1, 1000):
    for j in range(0, 13):
        processDataList[i-1].append(float(processRowList[i][j]))

for i in range(1, 1000):
    for j in range(0, 3):
        qualityDataList[i-1].append(float(qualityRowList[i][j]))

print(processDataList)
print(qualityDataList)
