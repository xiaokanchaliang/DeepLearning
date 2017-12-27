import numpy as np
import csv
from NeutralNetwork import backPropagation

def getData():

    result = np.random.uniform(-3, 3, size = (100, 130))

    return result

def convertToMatrix(data):

    result = np.empty((13, 10), dtype = np.float32)

    for i in range(13):

        for j in range(10):

            result[i][j] = data[0][i * 10 + j]

    return result

def evaluation(data):

    result = np.empty((100, 1), dtype = np.float32)

    for i in range(100):

        matrix = convertToMatrix(data[i])

        result[i] = backPropagation(matrix)

        print("evalution result " + str(i) + ":" + str(result[i]))

    return result

def select(result):

    rand = np.random.random(1)

    sum = 0

    rate = 0

    for i in range(result.size):

        sum = sum + result[i]

    for j in range(result.size):

        rate = rate + result[i] / sum

        if rand < rate:

            return j
    return 0

def selectBest(result):

    rand = np.random.random(1)

    fatherIndex = 0

    motherIndex = 0

    for i in range(result.size):

        if result[i] > result[fatherIndex]:

            motherIndex = fatherIndex

            fatherIndex = i

    return fatherIndex, motherIndex

def cross(fatherIndex, motherIndex, data):

    children = np.empty((1,130), dtype = np.float32)

    for i in range(65):

        children[0][i] = data[fatherIndex][i]

        children[0][i + 65] = data[motherIndex][i]

    return children

def getWorstIndex(result):

    index = 0

    for i in range(result.size):

        if result[i] < result[index]:

            index = i

    return index

def save(data, name):

    file = open(str(name) + '.csv', 'w', newline='')

    writer = csv.writer(file)

    writer.writerows(data)

def getDataAndResultFromFile():

    dataReader = csv.reader(open('geneSourceData.csv', encoding='utf-8'))

    resultReader = csv.reader(open('geneSourceResult.csv', encoding='utf-8'))

    data = np.empty((100, 130), dtype = np.float32)

    result = np.empty((100, 1), dtype = np.float32)

    resultCount = 0

    for dataRow in dataReader:

        for i in range(100):

            for j in range(130):

                data[i][j] = float(dataRow[j])

    for resultRow in resultReader:

        result[resultCount][0] = float(resultRow[0])

        resultCount = resultCount + 1

    return data, result

def getAverage(result):

    sum = 0

    for i in range(result.size):

        sum = sum + result[i]

    return sum / result.size

def saveDataAndResult():

    data = getData()

    result = evaluation(data)

    save(data, "geneSourceData")

    save(result, "geneSourceResult")

def main():

    data, result = getDataAndResultFromFile()

    average = []

    for m in range(1000):

        fatherIndex = select(result)

        motherIndex = select(result)

        children = cross(fatherIndex, motherIndex, data)

        worstIndex = getWorstIndex(result)

        for i in range(130):

            data[worstIndex][i] = children[0][i]

        result[worstIndex] = backPropagation(convertToMatrix(children))

        print("iteration " + str(m) + ":" + str(result[worstIndex]))

        average.append(getAverage(result))

    save(data, "geneData")

    save(result, "geneResult")