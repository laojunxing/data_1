import os
import glob #用它可以查找符合自己目的的文件，类似于Windows下的文件搜索
import pandas as pd #数据统计包
import xml.etree.ElementTree as ET #xml处理API模块

def xml_to_csv(path):
    xml_list = []
    # 读取注释文件
    for xml_file in glob.glob(path + '/*.xml'): #获得路径下*.xml的文件
        tree = ET.parse(xml_file) #载入数据
        root = tree.getroot() #获取xml的根节点
        for member in root.findall('object'): #获取所有object节点
            value = (root.find('filename').text, #filename
                     int(root.find('size')[0].text), #width
                     int(root.find('size')[1].text), #height
                     member[0].text, #第一个字节点的类型
                     int(member[4][0].text), #xmin
                     int(member[4][1].text), #ymin
                     int(member[4][2].text), #xmax
                     int(member[4][3].text) #ymax
                     )
            xml_list.append(value) #在列表末尾添加value
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

    # 将所有数据分为样本集和验证集，一般按照3:1的比例
    all_list = xml_list[0:]
    train_list = xml_list[0: int(len(xml_list) * 0.67)]
    eval_list = xml_list[int(len(xml_list) * 0.67) + 1: ]

    # 保存为CSV格式
    all_df = pd.DataFrame(all_list, columns=column_name)
    train_df = pd.DataFrame(train_list, columns=column_name)
    eval_df = pd.DataFrame(eval_list, columns=column_name)
    all_df.to_csv('C:/Users/39444/Desktop/标签/all.csv', index=None,sep='|')#写入到 csv 文件，使用|分隔数据，保存在绝对路径下
    train_df.to_csv('C:/Users/39444/Desktop/标签/train.csv', index=None)
    eval_df.to_csv('C:/Users/39444/Desktop/标签/eval.csv', index=None)

def main(): #数据的路径
    path = 'C:/Users/39444/Desktop/标签/aug'
    xml_to_csv(path)
    print('Successfully converted xml to csv.')
main()