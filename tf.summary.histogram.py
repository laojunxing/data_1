'''tf.summary.histogram():
输出一个直方图的Summary protocol buffer .

name：生成的节点名称.作为TensorBoard中的一个系列名称.
values：一个实数张量.用于构建直方图的值.
collections：图形集合键的可选列表.添加新的summary操作到这些集合中.默认为GraphKeys.SUMMARIES.
family： summary标签名称的前缀,用于在Tensorboard上显示的标签名称.(可选项)
'''
#!/usr/bin/python
# coding:utf-8
# TensorBoard直方图仪表板
import tensorflow as tf
k = tf.placeholder(tf.float32)
# 创建一个均值变化的正态分布（由0到5左右）
mean_moving_normal = tf.random_normal(shape=[1000], mean=(5*k), stddev=1)
# 将该分布记录到直方图汇总中
tf.summary.histogram("normal/moving_mean", mean_moving_normal)
sess = tf.Session()
writer = tf.summary.FileWriter("/tmp/histogram_example")
summaries = tf.summary.merge_all()
# 设置一个循环并将摘要写入磁盘
N = 400
for step in range(N):
    k_val = step/float(N)
    summ = sess.run(summaries, feed_dict={k: k_val})
    writer.add_summary(summ, global_step=step)
#tensorboard --logdir=/tmp/histogram_example