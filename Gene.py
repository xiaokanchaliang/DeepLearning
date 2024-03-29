import numpy as np
import csv
from NeutralNetwork import backPropagation

def getData():

    result = np.random.uniform(-3, 3, size = (100, 130))

    return result

def getOptimizationData():

    result = np.empty((100, 130), dtype = np.float32)

    part0 = np.random.uniform(-3, -1.5, size = (25, 130))
    part1 = np.random.uniform(-1.5, 0, size=(25, 130))
    part2 = np.random.uniform(0, 1.5, size=(25, 130))
    part3 = np.random.uniform(1.5, 3, size=(25, 130))

    for i in range(25):

        for j in range(130):

            result[i][j] = part0[i][j]
            result[i + 25][j] = part1[i][j]
            result[i + 50][j] = part2[i][j]
            result[i + 75][j] = part3[i][j]

    return result;

def convertToMatrix(data):

    result = np.empty((13, 10), dtype = np.float32)

    for i in range(13):

        for j in range(10):

            result[i][j] = data[0][i * 10 + j]

    return result

def convertToOptimizatinMatrix(data):

    result = np.empty((13, 10), dtype = np.float32)

    for i in range(13):

        for j in range(10):

            result[i][j] = data[i * 10 + j]

    return result

def evaluation(data):

    result = np.empty((100, 1), dtype = np.float32)

    for i in range(100):

        matrix = convertToMatrix(data[i])

        result[i] = backPropagation(matrix)

        print("evalution result " + str(i) + ":" + str(result[i]))

    return result

def evaluationOptimization(data):

    result = np.empty((100, 1), dtype = np.float32)

    for i in range(100):

        matrix = convertToOptimizatinMatrix(data[i])

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

        rate = rate + (result[j] / sum)

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

    for i in range(100):

        children[0][i] = data[fatherIndex][i]

    for j in range(30):

        children[0][j + 100] = data[motherIndex][j + 100]

    rand = int(np.random.random(1)*130)

    if(rand < 120):
        children[0][rand] = 0
        children[0][rand + 1] = 0
        children[0][rand + 2] = 0
        children[0][rand + 3] = 0
        children[0][rand + 4] = 0
        children[0][rand + 5] = 0
        children[0][rand + 6] = 0
        children[0][rand + 7] = 0
        children[0][rand + 8] = 0
        children[0][rand + 9] = 0
    else:
        children[0][rand] = 0
        children[0][rand - 1] = 0
        children[0][rand - 2] = 0
        children[0][rand - 3] = 0
        children[0][rand - 4] = 0
        children[0][rand - 5] = 0
        children[0][rand - 6] = 0
        children[0][rand - 7] = 0
        children[0][rand - 8] = 0
        children[0][rand - 9] = 0

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

def getDataAndResultFromFile(dataName, resultName):

    dataReader = csv.reader(open(dataName, encoding='utf-8'))

    resultReader = csv.reader(open(resultName, encoding='utf-8'))

    data = np.empty((100, 130), dtype = np.float32)

    result = np.empty((100, 1), dtype = np.float32)

    resultCount = 0

    dataCount = 0

    for dataRow in dataReader:

            for j in range(130):

                data[dataCount][j] = float(dataRow[j])

            dataCount = dataCount + 1

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

    data = getOptimizationData()

    result = evaluationOptimization(data)

    save(data, "geneSourceOptimizationDataAnother")

    save(result, "geneSourceOptimizationResultAnother")

def getMaxium(data):

    result = 0

    for i in range(data.size):

        if data[i][0] > result:

            result = data[i][0]

    return result

def main():

    data, result = getDataAndResultFromFile("geneSourceData201712272331.csv", "geneSourceResult201712272331.csv")

    average = np.empty((1000, 1), dtype = np.float32)

    maxium = np.empty((1000, 1), dtype = np.float32)

    for m in range(1000):

        fatherIndex = select(result)

        motherIndex = select(result)

        children = cross(fatherIndex, motherIndex, data)

        worstIndex = getWorstIndex(result)

        for i in range(130):

            data[worstIndex][i] = children[0][i]

        result[worstIndex] = backPropagation(convertToMatrix(children))

        average[m][0] = getAverage(result)

        maxium[m][0] = getMaxium(result)

        print("iteration " + str(m) + ":" + str(result[worstIndex]) + " average:" + str(average[m][0]) + " maxium:" + str(maxium[m][0]))

    save(data, "geneData201712272331")

    save(result, "geneResult201712272331")

    save(average, "geneAverage201712272331")

    save(maxium, "geneMaxium201712272331")