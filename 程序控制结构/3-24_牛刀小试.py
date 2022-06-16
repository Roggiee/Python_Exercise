k = 2
# 输出结果为 234
while(k < 5):
    print(k)
    k = k+1
i = 5
# 进行条件判断,5<10为卫rue,执行循环体．此时，i=7
while(i < 10):
    print("循环进行中")
    print(i)
    i = i+2
    # 再次进行条件判断,7<10，为true,执行循环体．此时,i=9
    # 再次进行条件判断,9<10，为true,执行循环体．此时,i=11
    # 再次进行条件判断,11<10，为false, 循环语句执行完毕，接着执行其他语句
print("循环结束了")
print(i)

##########################################
# 在屏幕上输出1~4这4个数宇
# 这里使用range（函数，作用是创建整数的有序列表，相当于(1,2,3,4)
for i in range(1, 5):
    print(i, end="")
    # 这里是循环体，会被多次执行，本程序中会执行4次
    # 在屏幕上輸出1~4这4个数宇
for i in range(1, 10):
    print(i, end="")
    # 这里直接使用 1 和5
for i in (1, 5):
    print(i, end="")
# 计算1~n的和
a = int(input("请输入一个数："))
sum = 0
for i in range(1, a + 1):
    sum = sum + i
    print(sum)
