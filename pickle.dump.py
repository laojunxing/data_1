import pickle
#创建一个字典变量
data = {'a':[1,2,3],'b':('string','abc'),'c':'hello'}
#print(data)
#以二进制方式来存储,rb,wb,wrb,ab
pic = open('testdata.pkl','wb')
#将字典数据存储为一个pkl文件
pickle.dump(data,pic)
pic.close()