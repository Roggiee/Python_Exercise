# 循环输入一些数(以输入0为结束)，并求这些数之和
sum = 0
n = eval(input("请输入一个数："))
while n != 0:
    sum = sum + n
    n = eval(input("请输入一个数："))
print(sum)
# 循环輪出10-20间所有的数
for i in range(10, 20):
    print(i)
# 找出5-100之间能被5或者7整除的数并输出
for i in range(5, 100):
    if(i % 5 == 0 or i % 7 == 0):
        print(i)

icount = 0
for i in range(0, 10):
    n = eval(input("请输入一个数："))
    if(n > 0):
        icount += 1
print(icount)
