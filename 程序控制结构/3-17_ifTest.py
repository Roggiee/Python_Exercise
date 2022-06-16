a = eval(input("请输入一个数字："))
if(a < 0):
    print(a*-1)

input("双分支选择结构")
a = eval(input("请输入一个数字"))
if(a >= 0):
    print(a)
else:
    print(a*-1)

score = eval(input("请输入一个分数:"))
if(score >= 90):
    print("优秀")
elif(score >= 80):
    print("良好")
elif(score >= 70):
    print("中")
elif(score >= 60):
    print("及格")
else:
    print("不及格")
