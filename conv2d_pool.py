#池化函数将平面内某一位置及其相邻位置的特征值进行统计汇总，并将汇总后的结果作为这一位置在该平面内的值。
'''
最大池化
①tf.nn.max_pool(value, ksize, strides, padding, name=None)
value：需要池化的输入，一般池化层接在卷积层后面，所以输入通常是feature map，依然是[batch, height, width, channels]这样的shape
ksize：池化窗口的大小，取一个四维向量，一般是[1, height, width, 1]，因为我们不想在batch和channels上做池化，所以这两个维度设为了1
strides：和卷积类似，窗口在每一个维度上滑动的步长，一般也是[1, stride,stride, 1]
padding：和卷积类似，可以取'VALID' 或者'SAME'
         SAME： 采取的是补全方式，尝试在左边和右边补0
         VALID：采用的是丢弃的方式，如果不够滑动一次则将剩下的数据丢弃。
返回一个Tensor，类型不变，shape仍然是[batch, height, width, channels]这种形式

②tf.layers.max_pooling2d(value , pool_size , strides, padding, data_format , name=None)

③tf.layers.MaxPooling2D(pool_size , strides , padding, data_format , name=name)
pool_size：一个整数或者2个整数的元组/列表：（pool_height，pool_width），指定池化窗口的大小。 可以是单个整数，以为所有空间维度指定相同值。
strides：一个整数或者2个整数的元组/列表，指定池操作的步幅。 可以是单个整数，以为所有空间维度指定相同值。
padding:字符串，“valid”或者”same”
data_format:一个字符串，channels_last（默认）或channels_first中的一个，输入中维度的排序，channels_last对应于具有形状(batch,height, width, channels)的输入，而channels_first对应于具有形状(batch, channels, height,width)的输入。
name:层的名称。
'''

'''
卷积 tf.nn.conv2d(input, filter, strides, padding, use_cudnn_on_gpu=None, name=None)
input：指需要做卷积的输入，要求是一个Tensor，具有[batch, in_height, in_width, in_channels]这样的shape，要求类型为float32和float64之一
filter：要求是一个Tensor，具有[filter_height, filter_width, in_channels, out_channels]这样的shape，第三维in_channels，就是参数input的第四维
strides：卷积时在图像每一维的步长，这是一个一维的向量，长度4
padding：string类型的量，只能是"SAME","VALID"其中之一
use_cudnn_on_gpu:bool类型，是否使用cudnn加速，默认为true
name参数用以指定该操作的name，与方法有关的一共五个参数 
结果返回一个Tensor，这个输出，就是我们常说的feature map
'''
import numpy as np
import tensorflow as tf
x_in = np.array([[
  [[2], [1], [2], [0], [1]], #2+2+3+12
  [[1], [3], [2], [2], [3]],
  [[1], [1], [3], [3], [0]],
  [[2], [2], [0], [1], [1]],
  [[0], [0], [3], [1], [2]], ]]) #shape  (1,5,5,1)
# [batch, in_height, in_width, in_channels]
kernel_in = np.array(
    [[ [[2, 1]], [[3, 2]] ],
     [ [[0, 3]], [[1, 4]] ], ])  #shape (2,2,1,2)
#[filter_height, filter_width, in_channels, out_channels]
x = tf.constant(x_in, dtype=tf.float32)
kernel = tf.constant(kernel_in, dtype=tf.float32)
conv = tf.nn.conv2d(x, kernel, strides=[1, 1, 1, 1], padding='VALID') #采用了valid所以conv.shape -- (1,4,4,2)
#max_pool()函数实现了最大池化层的前向传播过程
pool1 = tf.nn.max_pool(conv, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1], padding="SAME")
pool2 = tf.layers.MaxPooling2D(pool_size=[2,2], strides=1, padding='SAME')(conv)
#strides：一个整数或者2个整数的元组/列表，指定池操作的步幅。 可以是单个整数，以为所有空间维度指定相同值。
pool3 = tf.layers.max_pooling2d(conv,pool_size=[2,2],strides=[1,1],padding='SAME')
w2 = tf.Variable(tf.random_normal([2,1, 3], stddev=0.01) ,name='filter2')
with tf.Session() as sess:
    #sess.run(tf.global_variables_initializer())#初始化模型的参数
    ##当我们训练自己的神经网络的时候，无一例外的就是都会加上这一句
    #sess.run(tf.global_variables_initializer()) 就是run了所有global Variable 的assign op，这就是初始化参数的本来面目。
    #一个操作叫做Operation，操作可以看做是节点，所以Op表示节点。 assign op表示tf.assign
    print('conv\n',sess.run(conv))
    print('pool1',sess.run(pool1))
    print('pool2', sess.run(pool2))
    print('pool3', sess.run(pool3))

#结果输出
'''
conv
[[[[10. 19.][10. 22.][ 6. 16.][ 6. 20.]]
  [[12. 14.][15. 22.][13. 27.][13. 17.]]
  [[ 7. 17.][11. 13.][16. 13.][ 7. 10.]]
  [[10.  6.][ 7. 14.][ 4. 15.][ 7. 14.]]]]
pool
[[[[15. 22.][15. 27.][13. 27.][13. 20.]]
  [[15. 22.][16. 27.][16. 27.][13. 17.]]
  [[11. 17.][16. 15.][16. 15.][ 7. 14.]]
  [[10. 14.][ 7. 15.][ 7. 15.][ 7. 14.]]]]
'''