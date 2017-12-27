from NeutralNetwork import backPropagation

import numpy as np
import csv


def getData():

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

            result[i][j] = data[i * 10 + j]

    return result

def evaluation(data):

    result = np.empty((100, 1), dtype = np.float32)

    for i in range(100):

        matrix = convertToMatrix(data[i])

        result[i] = backPropagation(matrix)

        print("evalution result " + str(i) + ":" + str(result[i]))

    return result

def save(data, name):

    file = open(str(name) + '.csv', 'w', newline='')

    writer = csv.writer(file)

    writer.writerows(data)

def saveDataAndResult():

    data = getData()

    result = evaluation(data)

    save(data, "geneData20171227")

    save(result, "geneResult20171227")