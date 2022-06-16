# 以下程序中的print(i,j,end="，")的语句会被执行4次，输出结果均为00,01,10,11
# for 语句中嵌套for 语句
for i in range(2):
    for j in range(2):
        print(i, j, end=", ")
print()

# for 语句中嵌套while语句
for i in range(2):
    j = 0
    while(j < 2):
        print(i, j, end=", ")
        j = j+1
print()

# while 语句中嵌套for 语句
i = 0
while(i < 2):
    for j in range(2):
        print(i, j, end=", ")
        i = i+1
