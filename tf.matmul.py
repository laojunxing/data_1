'''
tf.matmul(a, b, name) #矩阵或者tensor乘法
a: `Tensor` of type `float16`, `float32`, `float64`, `int32`, `complex64`,
b: `Tensor` with same type and rank as `a`.（也就是说a ，b的维度和类型必须一致）
1.输入a ，b必须是矩阵或者维度大于2的tensor
2.这个函数是专门矩阵或者tensor乘法，而不是矩阵元素对应元素相乘。这点要注意
'''
import tensorflow as tf
b1 = tf.Variable(tf.random_normal([2]), name='bias1')
CL = tf.constant([1., 2., 3., 4., 5., 6.], shape=[2, 3])
print(tf.Session().run(CL))
# W1 = tf.constant([7., 8., 9., 10., 11., 12.], shape=[3, 2])#偏置与W1最后维度一样
# c = tf.matmul(CL, W1) #[array([[ 39.,  54.,  69.],
#                             #  [ 49.,  68.,  87.],
#                               #[ 59.,  82., 105.]], dtype=float32)]
# print(c.shape)
# FCNL1 = tf.nn.relu(tf.matmul(CL, W1) + b1)
# FCNL1 = tf.nn.dropout(FCNL1, keep_prob=0.5)
# print(FCNL1.shape)
# with tf.Session() as sess:
#     print(sess.run([CL]))
'''[array([[1, 2, 3],
               [4, 5, 6]]), 
        array([[ 7,  8],
               [ 9, 10],
               [11, 12]]), 
        array([[ 58,  64],
               [139, 154]])]'''