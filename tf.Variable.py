'''tensorflow中有两个关于variable的op(选项)
tf.Variable(initial_value, trainable, validate_shape, name)
1.initial_value：默认为None，可以搭配tensorflow随机生成函数，如上例。
2.trainable：默认为True，可以后期被算法优化的。如果不想该变量被优化，改为False。
3.validate_shape：默认为True，形状不接受更改，如果需要更改，validate_shape=False。
4.name：默认为None，给变量确定名称。

get_variable(name,shape, dtype, initializer,)
1.name：新变量或现有变量的名称。
2.shape：新变量或现有变量的形状。
3.dtype：新变量或现有变量的类型（默认为 DT_FLOAT）。
4.initializer：创建变量的初始化器。如果初始化器为 None（默认），则将使用在变量范围内传递的默认初始化器。初始化器也可以是张量，在这种情况下，变量被初始化为该值和形状。
返回值：创建或存在Variable（或者PartitionedVariable，如果使用分区器）。
'''
import tensorflow as tf
#Variable和get_variable区别1
#tf.Variable() 初始化是直接传入initial_value(初始值)
#tf.get_variable()初始化是传入一个initializer(初始化器)
def a1():
    a = tf.Variable(initial_value=tf.random_normal(shape=[200, 100], stddev=0.1), trainable=True)
    b = tf.get_variable(name = 'weights', shape=[200, 100], dtype=tf.float32, initializer=tf.random_normal_initializer(stddev=0.1))
#a1()
#区别2
#使用tf.Variable时，如果检测到命名冲突，系统会自己处理
#使用tf.get_variable()时，系统不会处理冲突，而会报错
def a2():
    w_1 = tf.Variable(3, name="w_1") # w_1:0
    w_2 = tf.Variable(1, name="w_1") # w_1_1:0
    print(w_1.name)
    print(w_2.name)
    w_3 = tf.get_variable(name="w_3", initializer=1)
    w_4 = tf.get_variable(name="w_3", initializer=2)
    # 错误信息
    # ValueError: Variable w_1 already exists, disallowed. Did
    # you mean to set reuse=True in VarScope?
#a2()
#区别3：当我们需要共享变量的时候，需要使用tf.get_variable()
def a3():
    #tf.variable_scope定义创建变量（层）的操作的上下文管理器。
    with tf.variable_scope("scope1"):  # 跟tf.name_scope很像
        w1 = tf.get_variable("w1", shape=[])
        w2 = tf.Variable(0.0, name="w2")
        print(w1.name)
        print(w2.name)
    with tf.variable_scope("scope1", reuse=True): #进入此范围的重用模式以及所有子范围
        w1_p = tf.get_variable("w1", shape=[])
        w2_p = tf.Variable(0.0, name="w2")
    print(w1 is w1_p, w2 is w2_p)  # True False
a3()

#tf.placeholder和tf.Variable的区别
#tf.Variable声明一个变量，该变量必须被赋初值。
#tf.placeholder为一个张量插入占位符，面向一些长期存在的需要被填充的张量，可以提高内存利用效率