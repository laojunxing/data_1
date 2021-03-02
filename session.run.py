import tensorflow as tf
#session.run输出单个数
# a = tf.add(1, 2)  #原本3 变20
# b = tf.multiply(a, 2)  #=6
# session = tf.Session()
# replace_dict = {a: 20} #{<tf.Tensor 'Add:0' shape=() dtype=int32>: 20}  因为a是tensor
#
# v2 = session.run(b, feed_dict=replace_dict) #用20来代替b中a的值 即20*2=40
# print(v2)
# with tf.Session() as sess:
#     z, z1 = sess.run([a, b])
#     print('a =%s' % (z))
#     print('b =%s' % (z1))

#session.run输出多个数
a = tf.constant([[1, 2], [1, 2]])
b = tf.constant([[1, 1], [3, 2]])
c = tf.multiply(a, b) #对应元素相乘
session = tf.Session()
with tf.Session() as sess:
    z = sess.run([c])
    print('c =%s' % (z)) #c的值
replace_dict = {a: [[2, 1], [1, 1]],b:[[5, 5], [5, 5]]}
v1,v2,v3 = session.run([a,b,c], feed_dict=replace_dict) #用[[1, 1],[1, 1]]来代替a中的值,用[[5, 5], [5, 5]]代替b中的值，再输出c
print('v1\n',v1,'\nv2\n',v2,'\nv3\n',v3)