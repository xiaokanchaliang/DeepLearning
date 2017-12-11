import numpy as np
import tensorflow as tf


# 0.定义添加层的方法
def add_layer(input_data, in_size, out_size, activity_function=None):
    a = tf.Variable(tf.random_normal([in_size, out_size]))
    b = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    result = tf.matmul(input_data, a) + b
    if activity_function is None:
        answer = result
    else:
        answer = activity_function(result)
    return answer


# 1.训练的数据
x_data = np.random.uniform(-1, 1, [1000, 5])
y_data = []
for i in range(1000):
    item_0 = [np.square(x_data[i][0]) + np.square(x_data[i][1]) + np.square(x_data[i][2]) + np.square(x_data[i][3]) + np.square(x_data[i][4])] + np.random.uniform(0, 0.1, size=1)
    item_1 = [(np.sin(x_data[i][0]) + np.sin(x_data[i][1]) + np.sin(x_data[i][2]) + np.sin(x_data[i][3]) + np.sin(x_data[i][4])) / 5] + np.random.uniform(0, 0.1, size=1)

    y_data.append(item_1 + np.random.uniform(0, 0.1, size=1))

# 2.定义结点准备接收数据
xs = tf.placeholder(tf.float32, [None, 5])
ys = tf.placeholder(tf.float32, [None, 1])

# 3.定义神经网络结构
hidden_0 = add_layer(xs, 5, 10, activity_function=tf.nn.relu)
prediction = add_layer(hidden_0, 10, 1, activity_function=None)

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
    sess.run(train, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
