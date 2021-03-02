'''
tf.summary.scalar(name,tensor,collections=None,family=None)
作用：显示标量的信息，一般在画loss，accuary时会用到这个函数。
name，生成Op节点的名字
tensor，包含一个值的实数tensor
collection，图的集合键值的可选列表。
family，可选项，设置时用作求和标签名称的前缀，这影响着tensorboard所显示的标签名。
返回：string类型的标量Tensor。其中包含一个Summary协议缓冲区。
'''
import tensorflow as tf
# 定义两个变量
a = tf.placeholder(dtype=tf.float32, shape=[])
b = tf.placeholder(dtype=tf.float32, shape=[])
#添加变量进去
tf.summary.scalar('a', a) #添加变量到直方图中
tf.summary.scalar('b', b)
# 将所有summary全部保存到磁盘，以便tensorboard显示
smy = tf.summary.merge_all()
with tf.Session() as sess:
    # 初始化变量
    sess.run(tf.global_variables_initializer())
    #把信息存储在具体的文件夹里面
    writer = tf.summary.FileWriter("tjn", sess.graph)#定义一个写入summary的目标文件，tjn为写入文件地址
    for i in range(5):
        sumers=sess.run(smy,feed_dict={a:i+9,b:i+2}) #调用sess.run运行图，生成五步的训练过程数据
        writer.add_summary(summary=sumers,global_step=i) #调用train_writer的add_summary方法将训练过程以及训练步数保存
#打开cmd，输入     cd C:\Users\39444\Desktop\最终数据处理包\tjn
#        再输入   tensorboard --logdir=C:\Users\39444\Desktop\最终数据处理包\tjn
#        打开页面 http://localhost:6006/