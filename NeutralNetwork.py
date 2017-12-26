import numpy as np
import tensorflow as tf
import csv

def backPropagation(data):
    # x_data = np.random.random((1000,13))
    # y_data = np.random.random((1000,1))

    input1 = np.empty((800,13))
    input2 = np.empty((200,13))

    inputReader = csv.reader(open('processDataForNormalized.csv', encoding='utf-8'))

    inputRowNumber = 0

    for inputRow in inputReader:
        if(inputRowNumber < 800):
            input1[inputRowNumber][0] = float(inputRow[0])
            input1[inputRowNumber][1] = float(inputRow[1])
            input1[inputRowNumber][2] = float(inputRow[2])
            input1[inputRowNumber][3] = float(inputRow[3])
            input1[inputRowNumber][4] = float(inputRow[4])
            input1[inputRowNumber][5] = float(inputRow[5])
            input1[inputRowNumber][6] = float(inputRow[6])
            input1[inputRowNumber][7] = float(inputRow[7])
            input1[inputRowNumber][8] = float(inputRow[8])
            input1[inputRowNumber][9] = float(inputRow[9])
            input1[inputRowNumber][10] = float(inputRow[10])
            input1[inputRowNumber][11] = float(inputRow[11])
            input1[inputRowNumber][12] = float(inputRow[12])
            inputRowNumber = inputRowNumber + 1
        else:
            input2[inputRowNumber-800][0] = float(inputRow[0])
            input2[inputRowNumber-800][1] = float(inputRow[1])
            input2[inputRowNumber-800][2] = float(inputRow[2])
            input2[inputRowNumber-800][3] = float(inputRow[3])
            input2[inputRowNumber-800][4] = float(inputRow[4])
            input2[inputRowNumber-800][5] = float(inputRow[5])
            input2[inputRowNumber-800][6] = float(inputRow[6])
            input2[inputRowNumber-800][7] = float(inputRow[7])
            input2[inputRowNumber-800][8] = float(inputRow[8])
            input2[inputRowNumber-800][9] = float(inputRow[9])
            input2[inputRowNumber-800][10] = float(inputRow[10])
            input2[inputRowNumber-800][11] = float(inputRow[11])
            input2[inputRowNumber-800][12] = float(inputRow[12])
            inputRowNumber = inputRowNumber + 1

    output11 = np.empty((800,1))
    output12 = np.empty((800,1))
    output13 = np.empty((800,1))
    output21 = np.empty((200,1))
    output22 = np.empty((200,1))
    output23 = np.empty((200,1))

    outputReader = csv.reader(open('processDataForNormalized.csv', encoding='utf-8'))

    outputRowNumber = 0

    for outputRow in outputReader:
        if (outputRowNumber < 800):
            output11[outputRowNumber][0] = float(outputRow[0])
            output12[outputRowNumber][0] = float(outputRow[1])
            output13[outputRowNumber][0] = float(outputRow[2])
            outputRowNumber = outputRowNumber + 1
        else:
            output21[outputRowNumber-800][0] = float(outputRow[0])
            output22[outputRowNumber-800][0] = float(outputRow[1])
            output23[outputRowNumber-800][0] = float(outputRow[2])
            outputRowNumber = outputRowNumber + 1

    weights1 = tf.Variable(tf.zeros([13, 10]))
    weights2 = tf.Variable(tf.zeros([13, 10]))
    biases1 = tf.Variable(tf.zeros([13, 1]))
    biases2 = tf.Variable(tf.zeros([13, 1]))

    # 1.定义添加层的方法
    def add_layer(ws, input_data, in_size, out_size, activity_function=None):
        if ws is None:
            weights = tf.Variable(tf.zeros([in_size, out_size]))
        else:
            weights = tf.Variable(ws,dtype=tf.float32)
        biases = tf.Variable(tf.zeros([1, out_size]))
        result = tf.matmul(input_data, weights) + biases
        if activity_function is None:
            answer = result
        else:
            answer = activity_function(result)
        return answer

    # 2.定义结点准备接收数据
    xs = tf.placeholder(tf.float32, [None, 13])
    ys = tf.placeholder(tf.float32, [None, 1])

    # 3.定义神经网络结构
    hidden_1 = add_layer(data, xs, 13, 10, activity_function=tf.nn.sigmoid)
    prediction = add_layer(None, hidden_1, 10, 1, activity_function=tf.nn.sigmoid)

    # 4.定义误差表达式
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

    # 5.选择optimizer使误差达到最小
    train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    # 6.对所有的变量进行初始化
    init = tf.global_variables_initializer()
    sess = tf.Session()
    sess.run(init)

    # 7.迭代学习
    for i in range(15000):
        sess.run(train, feed_dict={xs: input1, ys: output11})

    result = 0

    predictionResult = sess.run(prediction, feed_dict={xs: input2, ys: output21})

    for i in range(200):
        if(int(predictionResult[i]*10) == int(output21[i]*10)):
            result = result + 1;

    return result/200


