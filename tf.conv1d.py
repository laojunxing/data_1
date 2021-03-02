'''
tf.nn.conv1d(value, filters, stride, padding)
value 的形状：[batch, in_width, in_channels]
    batch 表示多少个样本
    in_width 表示样本的宽度
    in_channels 表示样本有多少个通道可看作一个平铺开的二维数组：[batch, 行数, 列数]；
filter 的形状：[filter_width, in_channels, out_channels]
    filter_width 表示与 value 进行卷积的行数/每次
    in_channels 表示 value 一共有多少列 = value 中的 in_channels
    out_channels 表示卷积核数目
stride ：   一个整数，步长，filters窗口移动的步长
output 的形状：[batch, out_width, out_channels]
'''
'''
tf.layers.MaxPooling1D(pool_size,strides,padding,data_format,name)
参数：
pool_size:一个整数或者一个单个整数的tuple/list,表示池化窗口的大小
strides:一个整数或者一个单个整数的tuple/list,指定池化操作的移动步幅
padding:一个字符串。padding的方法：”valid”或者’same’
data_format:一个字符串，channels_last（默认）或channels_first中的一个，输入中维度的排序，channels_last对应于具有形状(batch, length, channels)的输入，而channels_first对应于具有形状(batch, channels, length)的输入。
name:一个字符串，表示层的名称。
'''


import numpy as np
import tensorflow as tf
x_in = np.array([
  [[2], [1], [2], [0], [1]],
  [[1], [3], [2], [2], [3]],
  [[1], [1], [3], [3], [0]],
  [[2], [2], [0], [1], [1]],
  [[0], [0], [3], [1], [2]], ]) #shape  (5,5,1)
kernel_in = np.array([[[ 2 , 1 ]],
                      [[ 0 , 2 ]]]) #shape (2,1,2) 最后的2是输出通道数
x = tf.constant(x_in, dtype=tf.float32)
kernel = tf.constant(kernel_in, dtype=tf.float32)
conv = tf.nn.conv1d(x, kernel, stride=1, padding='VALID') #shape(5, 4, 2)  4是因为valid,输出通道数对应卷积核
pool1 = tf.layers.MaxPooling1D(pool_size=2, strides=1, padding='VALID')(conv) #shape(5, 4, 1)
pool2 = tf.layers.max_pooling1d(conv,pool_size=2,strides=1,padding='VALID')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())#初始化模型的参数
    print('conv\n',sess.run(conv))
    print('pool1', sess.run(pool1))
    print('pool2', sess.run(pool2))

'''
一维卷积则只是在width或者说height方向上进行滑动窗口并相乘求和
conv
[[[4. 4.][2. 5.][4. 2.][0. 2.]]
 [[2. 7.][6. 7.][4. 6.][4. 8.]]
 [[2. 3.][2. 7.][6. 9.][6. 3.]]
 [[4. 6.][4. 2.][0. 2.][2. 3.]]
 [[0. 0.][0. 6.][6. 5.][2. 5.]]]
'''