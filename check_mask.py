from PIL import Image
f = open("asd.txt", 'w+')
# r 只能读 （带r的文件必须先存在）
# r+ 可读可写 不会创建不存在的文件 从顶部开始写 会覆盖之前此位置的内容
# rb 表示以二进制方式读取文件。该文件必须已存在。
# w+ 可读可写 如果文件存在 则覆盖整个文件不存在则创建
# w 只能写 覆盖整个文件 不存在则创建
# wb 表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，则覆盖写。
# a 只能写 从文件底部添加内容 不存在则创建
# a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建
im = Image.open('01.png')
rgb_im = im.convert('RGB') #convert()是图像实例对象的一个方法，接受一个mode参数，用以指定一种色彩模式
for i in range(256):
    for j in range(256):
        r, g, b = rgb_im.getpixel((i, j)) #返回i,j坐标下的rgb对应的值
        print(r, g, b, file=f) #输出到f文件里







# from PIL import Image
#
# img = Image.open("01.png")  # 读取系统的内照片
#
# width = img.size[0]  # 长度
# height = img.size[1]  # 宽度
# temp = 1
# for i in range(0, width):  # 遍历所有长度的点
#     temp += 1
#     for j in range(0, height):  # 遍历所有宽度的点
#         if temp % 2 == 0:
#             img.putpixel((i, j), (255, 255, 255))
# img = img.convert("RGB")  # 把图片强制转成RGB
# img.save("02.png")  # 保存修改像素点后的图片


#-*- coding:utf8 -*-
import os

# from PIL import Image
#
# im = Image.open('01.png')  # 打开图片
# pix = im.load()  # 导入像素
# width = im.size[0]  # 获取宽度
# height = im.size[1]  # 获取长度
#
# for x in range(width):
#     for y in range(height):
#         r, g, b, a = im.getpixel((x, y))
#         rgba = (r, g, b, a)
#         if (a == 0):
#             im.putpixel((x, y), (0, 0, 0, 0))
#         if (a == 255):
#             im.putpixel((x, y), (255, 255, 255, 255))
#
# im = im.convert('RGB')
# im.save('02.png')

# from PIL import Image
#
#
# def IsValidImage(img_path):
#     """
#     判断文件是否为有效（完整）的图片
#     :param img_path:图片路径
#     :return:True：有效 False：无效
#     """
#     bValid = True
#     try:
#         Image.open(img_path).verify()
#     except:
#         bValid = False
#     return bValid
#
#
# def transimg(img_path):
#     """
#     转换图片格式
#     :param img_path:图片路径
#     :return: True：成功 False：失败
#     """
#     if IsValidImage(img_path):
#         try:
#             str = img_path.rsplit(".", 1)
#             output_img_path = str[0] + ".jpg"
#             print(output_img_path)
#             im = Image.open(img_path)
#             im.save(output_img_path)
#             return True
#         except:
#             return False
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     img_path = 'wjk.png'
#     print(transimg(img_path))
# transimg('01.png')