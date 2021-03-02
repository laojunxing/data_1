
import cv2
from PIL import Image
from math import *
import numpy as np
import os.path as osp
def rotate(filein,fileout,degree, type):#degree逆时针旋转的角度大小
    #img = cv2.imread("test/images/21_training.png")
    img = Image.open(filein)#图片路径
    #print(img) #<PIL.PngImagePlugin.PngImageFile image mode=1
    # size=256x256 at 0x1B3BCBBEB00>  mode=1图像的类型
    if (str(img.mode) == 'L'): #L:8位像素（位深度为8)，表示黑白。像素点的范围是2^8 -- 0-255（256个值）
        img = np.array(img)
    else: #str(img.mode) == '1' #1位像素（位深度为1)，表示黑白。像素点的范围是2^1 -- 0-2（2个值）
        img = 255 * np.array(img).astype('uint8') #目的将2值像素变为255值像素
    height, width = img.shape[:2]
    #print('height:',height,'width:',width)
    # 旋转后的尺寸
    heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    #print('heightNew',heightNew)
    widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
    #print('widthNew',widthNew)

    matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)#变换矩阵
    #M=cv2.getRotationMatrix2D(center, angle, scale)
    # center：图片的旋转中心
    # angle：旋转角度
    # scale：旋转后图像相比原来的缩放比例
    #print('matRotation\n',matRotation)
    #print('matRotation[0, 2]', matRotation[1, 2])
    matRotation[0, 2] += (widthNew - width) / 2
    #print('matRotation[0, 2]',matRotation[0, 2])
    matRotation[1, 2] += (heightNew - height) / 2  #继续变换矩阵

    imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255,255,255))#原图像经过变换矩阵输出的新图片
    #print(imgRotation)
    #cv2.warpAffine(src, M, dsize,dst,flags,borderMode,borderValue) → dst
    #其中：
    #src - 输入图像。
    # M - 变换矩阵。
    # dsize - 输出图像的大小。
    # flags - 插值方法的组合（int类型！）
    # borderMode - 边界像素模式（int类型！）
    # borderValue - （重点！）边界填充值;默认情况下，它为0。
    #print(imgRotation)
    Image.fromarray(imgRotation).save(fileout, type)#imgRotation是narry数组形式
    #Image.fromarray(imgRotation).save(osp.join('train/rotate', list1 + '.png')) #保存旋转后的图片
    # cv2.imshow('img', img)
    # cv2.imshow('imgRotation',imgRotation)
    # cv2.waitKey(0)#等待毫秒数后图片消失，0表示图片不消失
#rotate('datas1/train/images/01.png','datas1/train/images/033.png',60,'png')