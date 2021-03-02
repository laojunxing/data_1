'''
tf.contrib.layers.xavier_initializer(uniform=True, seed=None, dtype=tf.float32)
该函数返回一个用于初始化权重的初始化程序 “Xavier” 。
这个初始化器是用来保持每一层的梯度大小都差不多相同。
参数：
uniform: 使用uniform或者normal分布来随机初始化。
seed: 可以认为是用来生成随机数的seed
dtype: 只支持浮点数。
返回值：初始化权重矩阵
'''