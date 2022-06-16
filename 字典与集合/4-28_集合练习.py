#创建集合
teams={'日本','苏联','苏联','日本','苏联','中国','苏联','古巴','古巴','古巴','中国','巴西','巴西','中国'}
print('有多少支球队曾经获得过奥运会女排冠军:',len(teams))
print(teams)

print(set([1,3,5,5,7,1]))
print(set(["apple"]))


x0=[1,1,2,2,3,3,4,4,5,5]
print('含有重复元素发的一个列表x0',x0)

x0_set=set(x0)
print('将列表x0转化一个集合:',x0_set)

print("关于集合set的计算")
set1={1,2,3,4,5,6}
set2={2,3,6}
print('集合set1:',set1,'\n集合 set2:',set2)
print("集合set1和set2的差集:",set2-set1)
print("集合set1和set2的并集",set1&set2)
print("集合set1和set2的交集",set1|set2)