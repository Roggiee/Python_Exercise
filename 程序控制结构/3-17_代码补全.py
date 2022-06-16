print("任务一")
pw = eval(input("请输入密码"))
if (pw == "1234"):
    print("欢迎光临")
else:
    print("密码错误")

print("任务二")
a = eval(input("输入变量值"))
if(a < 160):
    print("太小了")
elif(160 < a < 180):
    print("正合适")
else:
    print("太大了")
