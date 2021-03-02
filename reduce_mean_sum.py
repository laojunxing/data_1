'''③reduce_mean(input_tensor, axis=None, keep_dims=False, name=None, reduction_indices=None)
作用：用于计算张量tensor沿着指定的数轴（tensor的某一维度）上的的平均值，主要用作降维或者计算tensor（图像）的平均值。
input_tensor： 输入的待降维的tensor;
axis： 指定的轴，如果不指定，则计算所有元素的均值;
keep_dims：是否降维度，设置为True，输出的结果保持输入tensor的形状，设置为False，输出结果会降低维度;
name： 操作的名称;

④tf.reduce_sum(input_tensor, axis=None, keepdims=None, name=None)
作用：压缩求和，用于降维
input_tensor：待求和的tensor;
axis：指定的维，如果不指定，则计算所有元素的总和;
keepdims：是否保持原有张量的维度，设置为True，结果保持输入tensor的形状，设置为False，结果会降低维度，如果不传入这个参数，则系统默认为False;
name：操作的名称;
'''
import tensorflow as tf
def reduce_sum(): #压缩求和，用于降维

    a = tf.constant([[[1, 2, 3], [4 ,  5,  6]],
                     [[7, 8, 9], [10, 11, 12]]]) #shape(2, 2, 3)
    b = tf.reduce_sum(input_tensor=a, axis=0, keepdims=True) #shape(1, 2, 3)
    print(b.shape)
    sess = tf.Session()
    print(sess.run(b))
#reduce_sum()
'''我们把每一个元素进行编号
        [[[1,2,3],[ 4, 5, 6]]
         [[7,8,9],[10,11,12]]]
1->1_1_1。。。。。。2->1_1_2。。。。。。3->1_1_3
4->1_2_1。。。。。。5->1_2_2。。。。。。6->1_2_3
7->2_1_1。。。。。。。8->2_1_2。。。。。。9->2_1_3
10->2_2_1。。。。。。11->2_2_2。。。。。。12->2_2_3
    在axis = 0
    上求和就是在0维上相加，而1维和2维不变，即
    1_1_1 + 2_1_1 = 1 + 7 = 8
    1_1_2 + 2_1_2 = 2 + 8 = 10
    1_1_3 + 2_1_3 = 3 + 9 = 12
    1_2_1 + 2_2_1 = 4 + 10 = 14
    1_2_2 + 2_2_2 = 5 + 11 = 16
    1_2_3 + 2_2_3 = 6 + 12 = 18
    输出：
    [[[8, 10, 12], [14, 16, 18]]]'''

def reduce_mean(): #沿着指定的数轴上的的平均值
    x = [[1, 2, 3],
         [4, 5, 6]]
    y = tf.cast(x, tf.float32) #tensorflow 中张量数据类型转换
    mean_all = tf.reduce_mean(y) #取所有的平均值
    mean_0 = tf.reduce_mean(y, axis=0) #0维(列)上的平均值 为什么？
    mean_1 = tf.reduce_mean(y, axis=1) #1维(行)上的平均值
    with tf.Session() as sess:
        m_a, m_0, m_1 = sess.run([mean_all, mean_0, mean_1])
    print(m_a)
    print(m_0)
    print(m_1)
reduce_mean()