# 循环执行时，i=1，不符合1号2==0的条件，输出i;i=2时，符合i号2==0的条件，跳出循环。
# 因此.输出结果为1
for i in range(1, 6):
    if(i % 2 == 0):
        break
    print(i, end="")  # 输出结果为1
# 循环执行时，i=1，不符合i号2==0的条件，输出i;i=2时，符合1号2==0的条件，转至循环
# 起始处，继续i=3的操作。因此，输出结果为135
for i in range(1, 6):
    if(i % 2 == 0):
        continue
    print(i, end="")
# 请输出1~20 之间所有的数,遇到尾数为4时不输出
for i in range(1, 21):
    if(i % 10 == 4):
        continue
    print(i, end="")
