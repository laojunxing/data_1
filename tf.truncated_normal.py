'''
truncated_normal(
    shape, #输出张量的维度。1维整形张量或 array。
    mean=0.0, #均值
    stddev=1.0, #标准差
    dtype=tf.float32, #输出类型
    seed=None, #随机种子，若 seed 赋值，每次产生相同随机数
    name=None #运算名称
    )
功能：产生截断正态分布随机数，取值范围为 [ mean - 2 * stddev, mean + 2 * stddev ]。
'''
import tensorflow as tf
import matplotlib.pyplot as plt
tn = tf.truncated_normal([8], mean=5, stddev=1)
sess = tf.Session()
ov = sess.run(tn)
print(ov)
plt.plot(ov)
plt.show()
