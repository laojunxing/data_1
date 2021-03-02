'''
①tf.nn.softmax(logits, axis=None, name=None)
作用：把一个N*1的向量归一化为（0，1）之间的值，由于其中采用指数运算，使得向量中数值较大的量特征更加明显。
计算公式: softmax = tf.exp(logits) / tf.reduce_sum(tf.exp(logits), axis)
logits是一个张量，数据类型必须是half, float32, float64

②tf.nn.softmax_cross_entropy_with_logits(logits, labels, name=None)
作用：1.将logits转换成概率；2.计算交叉熵损失
logits：就是神经网络最后一层的输出，如果有batch的话，它的大小就是[batchsize，num_classes]，单样本的话，大小就是num_classes
labels：实际的标签，大小同上
第一步是先对网络最后一层的输出做一个softmax，这一步通常是求取输出属于某一类的概率，对于单样本而言，输出就是一个num_classes大小的向量（[Y1，Y2,Y3...]其中Y1，Y2，Y3...分别代表了是属于该类的概率）
第二步是softmax的输出向量[Y1，Y2,Y3...]和样本的实际标签做一个交叉熵
'''
import tensorflow as tf
def softmax():
    wx = tf.constant([[1., 2., 3.]])
    y=tf.Variable(initial_value=tf.random_normal(shape=[2,2], stddev=0.1), trainable=True)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())  #跑变量需要加上 初始化模型的参数
        print(sess.run(tf.nn.softmax(wx)))
        '''WX = [1, 2, 3]，经过softmax层得[0.09, 0.24, 0.67]，这三个数字表示这个样本属于第1, 2, 3
        类的概率分别是0.09, 0.24, 0.67。取概率最大的0.67，所以这里得到的预测值就是第三类。'''
        print(sess.run(tf.nn.softmax(y)))
#softmax1()
def softmax_cross_entropy_with_logits():
    logits = tf.constant([[1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [1.0, 2.0, 3.0]])
    y = tf.nn.softmax(logits) # step1:do softmax
    y_ = tf.constant([[0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [0.0, 0.0, 1.0]])  # true label
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))   # step2:do cross_entropy
    # do cross_entropy just one step
    #tf.nn.softmax_cross_entropy_with_logits可以由tf.nn.softmax+cross_entropy（也就是求y_*tf.log(y)）来代替 tf.reduce_sum只是求和，两种方法都是需要做的
    cross_entropy2 = tf.reduce_sum(tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels= y_)) # dont forget tf.reduce_sum()!!
    with tf.Session() as sess:
        softmax = sess.run(y)
        c_e = sess.run(cross_entropy)
        c_e2 = sess.run(cross_entropy2)
        print("step1:softmax result=")
        print(softmax)
        print("step2:cross_entropy result=")
        print(c_e)
        print("Function(softmax_cross_entropy_with_logits) result=")
        print(c_e2)
#softmax_cross_entropy_with_logits1()
