import numpy as np
import tensorflow as tf
import csv
import matplotlib.pyplot as plt

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
def add_layer1(input_data, in_size, out_size, activity_function=None):
    weights = tf.Variable(tf.zeros([in_size, out_size]) + 0.4)
    biases = tf.Variable(tf.zeros([1, out_size]))
    result = tf.matmul(input_data, weights) + biases
    if activity_function is None:
        answer = result
    else:
        answer = activity_function(result)
    return answer
def add_layer2(input_data, in_size, out_size, activity_function=None):
    weights = tf.Variable(tf.zeros([in_size, out_size]) + 0.5)
    biases = tf.Variable(tf.zeros([1, out_size]))
    result = tf.matmul(input_data, weights) + biases
    if activity_function is None:
        answer = result
    else:
        answer = activity_function(result)
    return answer

# 2.定义结点准备接收数据
xs1 = tf.placeholder(tf.float32, [None, 13])
xs2 = tf.placeholder(tf.float32, [None, 13])
ys1 = tf.placeholder(tf.float32, [None, 1])
ys2 = tf.placeholder(tf.float32, [None, 1])

# 3.定义神经网络结构
hidden1_1 = add_layer1(xs1, 13, 10, activity_function=tf.nn.sigmoid)
hidden2_1 = add_layer2(xs2, 13, 10, activity_function=tf.nn.sigmoid)
prediction1 = add_layer1(hidden1_1, 10, 1, activity_function=tf.nn.sigmoid)
prediction2 = add_layer2(hidden2_1, 10, 1, activity_function=tf.nn.sigmoid)

# 4.定义误差表达式
loss1 = tf.reduce_mean(tf.reduce_sum(tf.square(ys1 - prediction1), reduction_indices=[1]))
loss2 = tf.reduce_mean(tf.reduce_sum(tf.square(ys2 - prediction2), reduction_indices=[1]))

# 5.选择optimizer使误差达到最小
train1 = tf.train.GradientDescentOptimizer(0.1).minimize(loss1)
train2 = tf.train.GradientDescentOptimizer(0.1).minimize(loss2)

# 6.对所有的变量进行初始化
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 7.迭代学习
for i in range(15000):
    sess.run(train1, feed_dict={xs1: input1, ys1: output11})
    sess.run(train2, feed_dict={xs2: input1, ys2: output11})

predictionResult1 = sess.run(prediction1, feed_dict={xs1: input2, ys1: output21})
predictionResult2 = sess.run(prediction2, feed_dict={xs2: input2, ys2: output21})

errorData1 = np.abs(predictionResult1 - output21)
errorData2 = np.abs(predictionResult2 - output21)

sum1 = 0
sum2 = 0

for i in range(200):
    sum1 = sum1 + errorData1[i][0]
    sum2 = sum2 + errorData2[i][0]

print(sum1/200)
print(sum2/200)

figureDataFile0050=open('figureData-0-50-201801061422.csv','w',newline='')
figureDataFile5010=open('figureData-50-100-201801061422.csv','w',newline='')
processWriter=csv.writer(figureDataFile0050)
qualityWriter=csv.writer(figureDataFile5010)
processWriter.writerows(errorData1)
qualityWriter.writerows(errorData2)

