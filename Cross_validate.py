import pandas as pd
import numpy as np
import os
from sklearn.model_selection import StratifiedKFold
#k折交叉验证
def Stratified(filename,n_splits,shuffle,random_state):
    list = os.listdir(filename)
    #filename_label = {'filename': [str(i) + '.jpg' for i in range(100)],'label': [np.random.randint(0, 5) for i in range(100)]}
    filename_label = {'filename':list , 'label':[np.random.randint(0,n_splits) for i in range(len(list))]}#np.random.randint(0,5)随机生成数值在[0, 5)区间内,每一个filename的label都是随机在[0,5)
    #print(filename_label)
    #train = pd.DataFrame(filename_label)# 默认生成整数索引, 字典的键作列,值作行
    train =pd.DataFrame(filename_label)
    #n_splits = 5  # K
    x = train['filename'].values
    y = train['label'].values
    skf = StratifiedKFold(n_splits=n_splits, shuffle=shuffle,random_state=random_state)
    # KFold(n_splits=3, shuffle=False, random_state=None)
    # n_splits：表示划分几等份
    # shuffle：在每次划分时，是否进行洗牌
    # ①若为Falses时，其效果等同于random_state等于整数，每次划分的结果相同
    # ②若为True时，每次划分的结果都不一样，表示经过洗牌，随机取样的
    # random_state：随机种子数
    for index,(train_index,test_index) in enumerate(skf.split(x,y), start=1):#index索引，(train_index,test_index)
        # print(index)
        # print('train_index',train_index,'\ntest_index',test_index)
        res_train = pd.DataFrame()
        res_train['filename'] = train['filename'].iloc[train_index]#获取train_index对应行的filename。iloc通过行号来取行数据，data.iloc[0]取data第0行的数据
        #print(res_train['filename'])
        res_train['label'] = train['label'].iloc[train_index] #获取train_index对应行的label为值
        #print(res_train['label'])
        res_train.to_csv("csv/datas{}train.csv".format(index),index=False)#将res_train保存在相对路径下。'name={}'.format('zhangsan') -- name=zhangsan
        #index=0 不保存行索引  =1 保存索引
        #dt.to_csv('C:/Users/think/Desktop/Result.csv') #绝对位置
        #print( res_train.to_csv)
        res_test = pd.DataFrame()
        res_test['filename'] = train['filename'].iloc[test_index]#获取test_index对应行的filename
        res_test['label'] = train['label'].iloc[test_index]#获取test_index对应行的label。存放在res_test的'label'键里
        res_test.to_csv("csv/datas{}test.csv".format(index),index=False)
#Stratified('json文件/',6,True,0)