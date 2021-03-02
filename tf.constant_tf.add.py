import tensorflow as tf
'''
tf.constant(value, shape, dtype=None, name=None)
释义：生成常量
value，值
shape，数据形状
dtype，数据类型
name，名称
'''
x = tf.constant([[1, 2], [1, 2]])  #生成常量
y = tf.constant([[1, 1], [1, 2]])
z = tf.add(x, y) #2个shape相同的矩阵相加，2个对应元素相加得到一个与原矩阵相同的shape的矩阵

x1 = tf.constant(1)
y1 = tf.constant(2)
z1 = tf.add(x1, y1) #两个数相加，得到另个一数

x2 = tf.constant(2)
y2 = tf.constant([1, 2])
z2 = tf.add(x2, y2) #矩阵每个元素都加上这个数，输出一个矩阵

x3 = tf.constant([[1, 2], [1, 2]])
y3 = tf.constant([[1, 2]])  #注意:为什么用[[]] -- x，y两个参数数据类型一定要相同
z3 = tf.add(x3, y3) #一个矩阵和一个维度不同的矩阵，得到的是在某个维度上相加之后得到的矩阵

with tf.Session() as sess: #
    z_result, z1_result, z2_result, z3_result = sess.run([z, z1, z2, z3])
    print('z =\n%s' % (z_result))
    print('z1 =%s' % (z1_result))
    print('z2 =%s' % (z2_result))
    print('z3 =%s' % (z3_result))