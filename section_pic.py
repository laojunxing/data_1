# 图像切片
from PIL import Image
import cv2
import math
def section(filein, fileout, width, height, type): #路径到图片名为止
    img = Image.open(filein)
# 图片尺寸
    img_size = img.size
    h = img_size[1]  # 图片高度
    w = img_size[0]  # 图片宽度
    #print(h,w)
# 开始截取
    a=math.ceil(h/height)#高可截取的次数
    #print(a)
    b=math.ceil(w/width)#宽可截取的次数
    #print(b)

    for i in range(0,a):#高
        for j in range(0,b):#宽
            # if(i<=a-1&j<=b-1):
            region = img.crop((i*height,j*width,i*height+height,j*width+width))
            region.save(fileout + 'sec' + str(i) + str(j)  + '.png'  , type) #fileout后面的名字只能在这里。要用这里面的ij做图片名
# 保存图片
    #region = img.crop((a * height, b * width, x, y))
            # cv2.imshow("region", region)
            # cv2.waitKey(0)

    # region = img.crop((a * height, b * width, h, w))#最后不足50部分的切片
    # region.save(fileout+'第' + str(k) + '张切片' + '.png', type)
#section('datas1/train/images/01rota180.png','datas1/train/images/033.png' , 200,200,'png')