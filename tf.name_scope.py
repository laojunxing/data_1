import tensorflow as tf
#tf.name_scope() 决定“对象”属于哪个范围，并不会对“对象”的“作用域”产生任何影响。
tf.reset_default_graph()
# 无tf.name_scope()
def no():
    a = tf.constant(1, name='my_a')  # 定义常量
    d = tf.constant(1, name='my_a')
    b = tf.Variable(2, name='my_b')  # 定义变量
    c = tf.add(a, b, name='my_add')  # 二者相加（操作）
    print("a.name = " + a.name)
    print("d.name = " + d.name)
    print("b.name = " + b.name)
    print("c.name = " + c.name)
    # 保存graph用于tensorboard绘图
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer = tf.summary.FileWriter("./test", sess.graph)
        print(sess.run(c))
        writer.close()
#no()
#有tf.name_scope()
def yes():
    with tf.name_scope('cgx_name_scope'): #定义一块名为cgx_name_scope的区域，并在其中工作
        a = tf.constant(1,name='my_a')
        b = tf.Variable(2,name='my_b')
        c = tf.add(a,b,name='my_add')
    print("a.name = "+a.name)
    print("b.name = "+b.name)
    print("c.name = "+c.name)
    z = tf.constant(1, name='my_a')
    print("z.name = " + z.name)
    # 保存graph用于tensorboard绘图
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer = tf.summary.FileWriter("./test", sess.graph)
        print(sess.run(c))
        print(sess.run(z))
        writer.close()
#yes()
def asd():
    with tf.name_scope('cgx_scope') as cgxscope: #把'cgx_scope'简写为cgxscope
        a = tf.Variable(1, name='my_a')
    with tf.name_scope(cgxscope):
        b = tf.Variable(2, name='my_b')
    c = tf.add(a, b, name='my_add')
    print("a.name = " + a.name)
    print("b.name = " + b.name)
asd()

def many():
    with tf.name_scope('cgx_scope_1'):  # 第一重命名空间
        with tf.name_scope('cgx_scope_2'):  # 第二重命名空间
            a = tf.Variable(10, name='my_a') #cgx_scope_1/cgx_scope_2/my_a:0 -- 最后的0值代表什么？
    with tf.name_scope('cgx_scope_3'):
        b = tf.Variable(88, name='my_b')
    c = tf.add(a, b, name='my_add')
    #print('a = ' , a)
    #print(a.dtype)
    print("a.name = " + a.name)
    print("b.name = " + b.name)
many()