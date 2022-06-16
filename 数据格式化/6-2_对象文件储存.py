#1.利用pickle包存储对象
import pickle
d2={'name':'zhangsan','age':'22','gender':'male','address':'shanghai'}
output=open('d:保存字典.pkl','wb')
pickle.dump(d2,output)


#2.利用pickle包读取对象
import pickle
inp=open('d:保存字典.pkl','rb')
d3=pickle.load(inp)
print(d3)