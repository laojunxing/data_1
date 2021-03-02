#globals()最基本用法，获取全局变量表，前边为内置方法，后边为自定义的变量与方法。
a=123
b='hello'
c=True
class asd:  ###
    qq=123
    def d(z):
        e=456
        f='world' #e、f为局部变量
        print('locals\n',locals())
globals()
print('globals\n',globals()) #dict类型 ####
print('从globals()中获取当前py文件所在路径\n',globals().get('__file__'))

import time
import numpy as np
def tic(): #目的：获取模型开始运行时间
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()
    #print(globals())
    #print('startTime_for_tictoc' in globals())
    #获取到的是从1970-1-1 00:00:00 到现在的秒数（小数位还有6位）。
    #查看time.time.py，了解更多
#tic() #可以看到startTime_for_tictoc在globals()里面
tic()

def toc(): #目的：获取模型运行共花费的时间
    if 'startTime_for_tictoc' in globals():   #tic函数获取了startTime_for_tictoc为秒数
        time_counted = "模型运行花费的时间是 " + str(
            '{:.2f}'.format(time.time() - startTime_for_tictoc)) + " 秒" + " (" + str(
            '{:.2f}'.format((time.time() - startTime_for_tictoc) / 60)) + " 分)"
        print(time_counted)

    else:
        print("Toc: 没有设置开始时间tic")
    np.savetxt("time.txt", [time_counted], fmt="%s") #保存模型运行的时间
    #标黄的原因:局部变量' time_counts '可以在赋值之前引用   不懂

    # numpy.savetxt(fname,X)
    # fname 文件名
    # X    需要存的数组（一维或者二维）。
toc()
#中间是模型运行
#toc()

