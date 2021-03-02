# isinstance(object, classinfo)
        # object是变量或类
        # classinfo
        # 是类型(tuple, dict, int, float)
        # 判断变量是否是这个类型
class objA:
    pass
A = objA()
B = 'a', 'v'
C = 'a string'
print(isinstance(A, objA)) #判断A类里的东西是否为objA类
print(isinstance(B, tuple))# 判断B变量里的东西是否为tuple类型
#print(isinstance(C, basestring) ) #我的是3.6不能用 name 'basestring' is not defined
#basestring是str和unicode的超类（父类），用来判断一个对象是否为str或者unicode的实例，isinstance(obj, basestring)等价于isinstance(obj, (str, unicode))；
#注意：python3中舍弃了该函数，所以该函数不能在python3中使用。
n=2
value= 2
print((value,) * n)