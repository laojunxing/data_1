
# 将图片保存成 TFRecord
import tensorflow as tf
import os
def creat_txt(filename,label_name): #转换tfrecord格式所需的txt
    list = os.listdir(filename)#'./datas1/train/label'图片所在文件夹
    for i in range(0,len(list)):#循环获取所有图片的图片名和标签
        if(filename[-5:]=='label'): #如果是label文件夹里的图片
            label = label_name
        else:
            label = list[i][:-4] #如果不是标签图，标签为图片名。#suibianshe
        f = open(filename+'/image_information.txt', 'a')  #读取image_information.txt文件，没有则创建，‘a'表示再次写入时不覆盖之前的内容
        f.write(list[i])
        f.write(' ')
        f.write(label)
        f.write('\n')
# tf.train.Feature(**options)
# options可以选择如下三种数据格式：
# bytes_list = tf.train.BytesList(value=输入)  # 输入的元素的数据类型为string
# int64_list = tf.train.Int64List(value=输入)  # 输入的元素的数据类型为int(int32,int64)
# float_list = tf.trian.FloatList(value=输入)  # 输入的元素的数据类型为float(float32,float64)
# 注：value必须是list(向量)
def _Bytes_feature(value): #value是标签
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
def _bytes_feature(value): #value是...
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
def load(filename):  # 准备一个 writer 用来写 TFRecord 文件
    savedir = filename +'/data.tfrecords'  #tfrecord保存路径+文件名
    txtdir=filename+'/image_information.txt' #txt文件所在路径
    writer = tf.python_io.TFRecordWriter(savedir)#写入(储存）tfrecords文件
    txtlist = open(txtdir, 'r')#读的方式打开txt
    with tf.Session() as sess: #创建一个会话运行TensorFlow程序  sess = tf.sess
        for line in txtlist:  #用for迭代访问，获得图片的路径和类型
            tmp = line.strip().split(' ')
            #str.strip([chars])用于去除头尾的字符chars(头尾有回车字符转\n),,为空时默认删除空白符
            #str.split(' ')通过指定一个空格对字符串进行切片，返回分割后的字符串列表tmp -- ['01.png', '01']
            imgpath1 = tmp[0]  # 字符串列表tmp中tmp[0]代表该图像的路径 -- 01.png
            imgpath=filename+'/'+imgpath1 #图片所在地址 -- ./datas1/train/images/01.png
            label = str(tmp[1])  # 字符串列表tmp中tmp[1]代表该图像的标签 -- 01 #标签str '
            label=bytes(label, encoding="utf8")#转换为bytes型数据
            # 读取图片
            img = tf.gfile.FastGFile(imgpath, 'rb').read() #‘r’为utf-8(编码规则)，‘rb’为非utf-8[范围在0-255之间]
            #coding:utf-8或者#coding=utf-8的作用一样，声明Python代码的文本格式是UTF-8
            # 解码图片（如果是 jpg 格式就使用tf.image.decode_jpeg)）
            img = tf.image.decode_png(img)
            # 图片归一化，0-1之间的float32格式。为了将图片数据能够保存到 TFRecord 结构体中，所以需要将其图片矩阵转换成 string，
            img = tf.image.convert_image_dtype(img, dtype=tf.float32)
            # 把图片转换成希望的大小，由于本例子中两张图片大小都是650*434，所以此步骤可以省略。要注意的时候resize_images中输入图片的宽、高顺序
            #img = tf.image.resize_images(img, [height, width], method)
            img = sess.run(img)
            # 将其图片矩阵转换成string
            img_raw = img.tostring()
            # 将数据整理成 TFRecord 需要的数据结构
            example = tf.train.Example(features=tf.train.Features(feature= {'imge_raw': _bytes_feature(img_raw),'label': _Bytes_feature(label)}))   #label需要为bytes(字节数组)类型
            # 写 TFRecord
            writer.write(example.SerializeToString())  # SerializeToString()作用:把example序列化为一个字符串,因为在写入到TFRcorde的时候,write方法的参数是字符串的.
    writer.close()
load('train_1/label_one_hot')
# if __name__=='__main__':
# 	load("./image_information.txt_bak",650,434)
#creat_txt("datas1/test/images",'abc')
#load("datas1/test/images")