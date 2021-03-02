# import numpy as np
# Normalized_x_data = np.zeros((100, 2))
# x_data=np.array([[  1.  ,10.],[  2. , 11.],[  3.  ,12.],[  4. , 13.],[  5. , 14.],[  6. , 15.],[  7. , 16.]])
# for i in range(10):  # len(Normalized_x_data)=100
#     Normalized_x_data[i, :] = (x_data[i, :] - min(x_data[i, :])) / (max(x_data[i, :]) - min(x_data[i, :]))  # 说明这是元组
#     print(Normalized_x_data[i, :])

import numpy as np
#
# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
#
# output = tf.multiply(input1, input2)
#
# with tf.Session() as sess:
#     print(sess.run(output, feed_dict={input1: [3.], input2: [4.]}))




#reshape(tensor, shape, name=None)
# tensor：一个Tensor
# shape：一个Tensor；必须是以下类型之一：int32,int64；用于定义输出张量的形状
# name：操作的名称(可选)
import tensorflow as tf
print([None, 2])
t1 = tf.constant([1,2,3,4,5,6,7,8,9])
c1=tf.reshape(t1, [3,3])
print('c1\n',tf.Session().run(c1))

t2=tf.constant([[[1, 1], [2, 2]],
                [[3, 3], [4, 4]]]) #(2,2,2)
c2=tf.reshape(t2, [2, 4])
print('c2\n',tf.Session().run(c2))

#shape的一个分量是特殊值-1，则计算该维度的大小，以使总大小保持不变
t3 = tf.constant([[[1, 1, 1],
                   [2, 2, 2]],
                  [[3, 3, 3],
                   [4, 4, 4]],
                  [[5, 5, 5],
                   [6, 6, 6]]]) #[3,2, 3]
c3= tf.reshape(t3, [-1])
print('c3\n',tf.Session().run(c3))
c4=tf.reshape(t3, [2, -1])
print('c4\n',tf.Session().run(c4))
c5=tf.reshape(t3, [-1, 9]) #-1为2
print('c5\n',tf.Session().run(c5))
c7=tf.reshape(t3, [-1, 3]) #-1为6
print('c7\n',tf.Session().run(c7))
c6=tf.reshape(t3, [-1, 2, 3]) #18个数，-1为3
print('c6\n',tf.Session().run(c6))