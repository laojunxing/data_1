# tf.random_normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
#目的：从“服从指定正态分布的序列”中随机取出指定个数的值。
# shape: 输出张量的形状，必选
# mean: 正态分布的均值，默认为0
# stddev: 正态分布的标准差，默认为1.0
# dtype: 输出的类型，默认为tf.float32
# seed: 随机数种子，是一个整数，当设置之后，每次生成的随机数都一样
# name: 操作的名称

# -*- coding: utf-8 -*-)
import tensorflow as tf
w1 = tf.constant(123 ,name='filter1')
w2 = tf.Variable(tf.random_normal([2,1, 3], stddev=0.01) ,name='filter2')
with tf.Session() as sess:
    print(sess.run(w1))  #常量不用初始化方法
    sess.run(tf.global_variables_initializer()) #因为w1是变量，所以要初始化变量。这是初始化变量的方法
    print(sess.run(w2))