import tensorflow as tf
'''
#tf.one_hot()函数规定输入的元素indices从0开始，最大的元素值不能超过（depth - 1），因此能够表示depth个单位的输入。若输入的元素值超出范围，输出的编码均为 [0, 0 … 0, 0]。
返回一个 one-hot tensor。
def one_hot(indices,       #代表了on_value所在的索引，其他位置值为off_value。类型为tensor
            depth,         #编码深度。
            on_value=None, #定义在 indices[j] = i 时填充输出的值的标量,默认值为1
            off_value=None,#定义在 indices[j] != i 时填充输出的值的标量,默认值为0
            axis=None,     #要编码的轴,默认为-1
            dtype=None     #输出张量的数据类型。若dtype缺省，则其根据on_value或off_value的数据类型自动保持一致；若dtype、on_value、off_value都缺省，则默认为tf.float32 
            name=None)     #本次one_hot操作的名称
'''
input={0:100,1:90,2:80}
indices = [0, 10, 2,3]  # 输入数据(是个向量)需要编码的索引是[0,1,2]
depth = 4
c=tf.one_hot(indices, depth)  # output: [4 x 4]
#print('one_hot_y_data\n',tf.Session().run(c))
'''
 [[1. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
'''
indices = [2]  # (4) 输入数据(是个向量)的需要编码的索引是[0,2,-1,1]
depth = 4
z=tf.one_hot(indices, depth,
           on_value=5.0, off_value=0.0,
           axis=-1)  # output: [4 x 3]
print('one_hot_y_data\n',tf.Session().run(z))
# [[5.0, 0.0, 0.0],  # one_hot(0)  对位置0处的数据进行one_hot编码
#  [0.0, 0.0, 5.0],  # one_hot(2)  对位置2处的数据进行one_hot编码
#  [0.0, 0.0, 0.0],  # one_hot(-1) 对位置-1处的数据进行one_hot编码
#  [0.0, 5.0, 0.0]]  # one_hot(1)  对位置1处的数据进行one_hot编码




#怎么理解
indices = [[0, 2], [1, -1]]  # 输入数据是个矩阵(2,2)
depth = 3
e=tf.one_hot(indices, depth,
           on_value=1.0, off_value=0.0,
           axis=-1)  # output: [2 x 2 x 3]
#print('one_hot_y_data\n',tf.Session().run(e))
# [[[1.0, 0.0, 0.0],   # one_hot(0)  对位置(0,0)处的数据进行one_hot编码
#   [0.0, 0.0, 1.0]],  # one_hot(2)  对位置(0,2)处的数据进行one_hot编码
#  [[0.0, 1.0, 0.0],   # one_hot(1)  对位置(2,1)处的数据进行one_hot编码
#   [0.0, 0.0, 0.0]]]  # one_hot(-1) 对位置(1,-1)处的数据进行one_hot编码
