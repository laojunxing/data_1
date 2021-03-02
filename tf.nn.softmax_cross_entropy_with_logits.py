'''
tf.nn.softmax_cross_entropy_with_logits(logits, labels, name=None)
logits：就是神经网络最后一层的输出，如果有batch的话，它的大小就是[batchsize，num_classes]，单样本的话，大小就是num_classes
labels：实际的标签，大小同上
第一步是先对网络最后一层的输出做一个softmax，这一步通常是求取输出属于某一类的概率，对于单样本而言，输出就是一个num_classes大小的向量（[Y1，Y2,Y3...]其中Y1，Y2，Y3...分别代表了是属于该类的概率）
第二步是softmax的输出向量[Y1，Y2,Y3...]和样本的实际标签做一个交叉熵
'''
'''
reduce_mean(input_tensor,
                axis=None,
                keep_dims=False,
                name=None,
                reduction_indices=None)
第一个参数input_tensor： 输入的待降维的tensor;
第二个参数axis： 指定的轴，如果不指定，则计算所有元素的均值;
第三个参数keep_dims：是否降维度，设置为True，输出的结果保持输入tensor的形状，设置为False，输出结果会降低维度;
第四个参数name： 操作的名称;'''
import tensorflow as tf
# our NN's output
logits = tf.constant([ [8.0, 4.0, 6.0], [3.0, 2.0, 8.0]])
print(logits.shape)
# step1:do softmax
y = tf.nn.softmax(logits)
# true label
y_ = tf.constant([ [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]])
# step2:do cross_entropy
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
# do cross_entropy just one step
a=tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_)
print(a.shape)
cross_entropy2 = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_))  # dont forget tf.reduce_sum()!!

with tf.Session() as sess:
    softmax = sess.run(y)
    print(sess.run(a))
    c_e = sess.run(cross_entropy)
    c_e2 = sess.run(cross_entropy2)
    print("step1:softmax result=")
    print(softmax)
    print("step2:cross_entropy result=")
    print(c_e)
    print("Function(softmax_cross_entropy_with_logits) result=")
    print(c_e2)