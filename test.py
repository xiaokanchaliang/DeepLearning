import numpy as np
import tensorflow as tf
import csv

error=np.zeros((1000,1),dtype=np.float32)

# x_data = np.random.random((1000,13))
# y_data = np.random.random((1000,1))

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

outputLabel1 = np.zeros((1000,1),dtype=np.float32)
outputLabel2 = np.zeros((1000,1),dtype=np.float32)
outputLabel3 = np.zeros((1000,1),dtype=np.float32)

outputLabelReader = csv.reader(open('outputLabel.csv', encoding='utf-8'))

outputLabelRowNumber = 0

for outputLabelRow in outputLabelReader:
    outputLabel1[outputLabelRowNumber][0] = round(float(outputLabelRow[0]),1)
    outputLabel2[outputLabelRowNumber][0] = round(float(outputLabelRow[1]),1)
    outputLabel3[outputLabelRowNumber][0] = round(float(outputLabelRow[2]),1)
    outputLabelRowNumber = outputLabelRowNumber + 1

# 1.定义添加层的方法
def add_layer(input_data, in_size, out_size, activity_function=None):
    a = tf.Variable(tf.random_normal([in_size, out_size]))
    b = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    result = tf.matmul(input_data, a) + b
    if activity_function is None:
        answer = result
    else:
        answer = activity_function(result)
    return answer

# 2.定义结点准备接收数据
xs = tf.placeholder(tf.float32, [None, 13])
ys = tf.placeholder(tf.float32, [None, 1])

# 3.定义神经网络结构
hidden_1 = add_layer(xs, 13, 10, activity_function=tf.nn.sigmoid)
prediction = add_layer(hidden_1, 10, 1, activity_function=tf.nn.sigmoid)

# 4.定义误差表达式
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

# 5.选择optimizer使误差达到最小
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

# 6.对所有的变量进行初始化
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# 7.迭代1000次学习
for i in range(1000):
    sess.run(train, feed_dict={xs: input, ys: outputLabel1})
    error[i][0] = sess.run(loss, feed_dict={xs: input, ys: outputLabel1})

prediction = sess.run(prediction, feed_dict={xs: input, ys: outputLabel1})

print(outputLabel1)
