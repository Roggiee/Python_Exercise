#创建列表
ls=[90,93,85,93]
#列表转换为集合
S=set(ls)

#键列表
k=['k1','k2','k3','k4']
#值列表
v=['v1','v2','v3']
#zip组合，当两个列表的长度不一致时，多出的元素将被忽略
z=zip(k,v)
#转成字典
d=dict(z)

#创建字典
d2={'name':'zhangsan','age':'22','gender':'male','address':'shanghai'}
#将字典的key转换为列表
list1=list(d2)
print(list1)

#将字典的value转换为列表
list2=list(d2.values())
print(list2)