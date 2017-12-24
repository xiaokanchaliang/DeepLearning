import tensorflow as tf

a = tf.Variable(tf.random_normal([13, 10]))
b = tf.Variable(tf.zeros([1, 10]) + 0.1)

print(a)