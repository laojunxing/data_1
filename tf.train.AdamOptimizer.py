'''
tf.train.AdamOptimizer.__init__(
	learning_rate=0.001,
	beta1=0.9,
	beta2=0.999,
	epsilon=1e-08,
	use_locking=False,
	name='Adam')
作用：Adam优化算法：是一个寻找全局最优点的优化算法，引入了二次方梯度校正。
learning_rate：张量或浮点值。学习速率
beta1：一个浮点值或一个常量浮点张量。一阶矩估计的指数衰减率
beta2：一个浮点值或一个常量浮点张量。二阶矩估计的指数衰减率
epsilon：数值稳定性的一个小常数
use_locking：如果True，要使用lock进行更新操作
`name``：应用梯度时为了创建操作的可选名称。默认为“Adam”
本质上是带有动量项的RMSprop，它利用梯度的一阶矩估计和二阶矩估计动态调整每个参数的学习率。
Adam的优点主要在于经过偏置校正后，每一次迭代学习率都有个确定范围，使得参数比较平稳。

opt.minimize(loss,var_list)
(1)计算各个变量的梯度 (2)用梯度更新这些变量的值
loss:     `Tensor` ，需要优化的损失；
var_list: 需要更新的变量(tf.Varialble)组成的列表或者元组，默认值为`GraphKeys.TRAINABLE_VARIABLES`，即tf.trainable_variables() #不管
'''