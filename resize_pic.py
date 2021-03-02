# encoding=utf-8
# author: walker
# date: 2014-05-15
# function: 更改图片尺寸大小

from PIL import Image

'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''

def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)#img是PIL形式<PIL.PngImagePlugin.PngImageFile image mode=RGB size=565x584 at 0x18696F7BA58>
    out = img.resize((width, height), Image.ANTIALIAS)  # resize image with high-quality
    #print(out)
    out.save(fileout, type)#out
#
# if __name__ == "__main__":
#     filein = r'0.jpg'
#     fileout = r'testout.png'
#     width = 6000
#     height = 6000
#     type = 'png'
#     ResizeImage(filein, fileout, width, height, type)

#ResizeImage('datas1/test/images/04.png', 'datas1/test/resize/00.png', 50, 50, 'png')

# from PIL import Image
# import os.path
# import glob
# def convertjpg(jpgfile,outdir,width=1280,height=720):
#     img=Image.open('train/images')
#     new_img=img.resize((width,height),Image.BILINEAR)
#     new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
# for jpgfile in glob.glob("train/images/*.jpg"):#返回12文件夹下所有的jpg路径
#     convertjpg(jpgfile,"train/images/*.jpg")