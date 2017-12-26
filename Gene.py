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

            result[i][j] = data[i * 10 + j]

    return result

def evaluation(data):

    result = np.empty((100, 1), dtype = np.float32)

    for i in range(100):

        matrix = convertToMatrix(data[i])

        result[i] = backPropagation(matrix)

        print("evalution result " + str(i) + ":" + str(result[i]))

    return result

def selection(result):

    rand = np.random.random(1);

    sum = 0;

    rate = 0;

    for i in range(result.size):

        sum = sum + result[i]

    for j in range(result.size):

        rate = rate + result[i] / sum;

        if rand < rate:

            return j

def cross(fatherIndex, motherIndex, data):

    children = np.empty((1,130), dtype = np.float32)

    for i in range(65):

        children[0][i] = data[fatherIndex][i]

        children[0][i + 65] = data[motherIndex][i + 65]

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

def getAverage(result):

    sum = 0

    for i in range(result.size):

        sum = sum + result[i]

    return sum / result.size

def main():

    data = getData()

    result = evaluation(data)

    average = []

    for m in range(1000):

        fatherIndex = selection(result)

        motherIndex = selection(result)

        children = cross(fatherIndex, motherIndex, data)

        worstIndex = getWorstIndex(result)

        for i in range(int(data.size / 100)):

            data[worstIndex][i] = children[i]

        result[worstIndex] = backPropagation(convertToMatrix(children))

        print("iteration " + str(m) + ":" + str(result[worstIndex]))

        average.append(getAverage(result))

    save(data, "geneData")

    save(result, "geneResult")