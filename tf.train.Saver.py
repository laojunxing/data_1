#saver = tf.train.Save(max_to_keep=5)
#max_to_keep 参数表示要保留的最近检查点文件的最大数量，创建新文件时，将删除旧文件，默认为 5（即保留最近的 5 个检查点文件），max_to_keep=5。
#saver.save(sess,  '路径 + 模型文件名'） #连用
import tensorflow as tf
import os
import numpy as np
a = tf.Variable(1., tf.float32)
b = tf.Variable(2., tf.float32)
num = 10
model_save_path = './model/'
model_name = 'model'
saver = tf.train.Saver()
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    for step in np.arange(num):
        c = sess.run(tf.add(a, b))
        # checkpoint_path = os.path.join(model_save_path, model_name)
        # 默认最多同时存放 5 个模型
        saver.save(sess, os.path.join(model_save_path, model_name), global_step=step)