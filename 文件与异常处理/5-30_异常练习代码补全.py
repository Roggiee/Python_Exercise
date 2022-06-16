#1.代码补全
try:
    age=eval(input("请输入你现在的年龄"))
    print("明年，你是{}岁".format(age+1))
except Exception:
    print("操作类型异常")
else:
     print("到2030年，你是{}岁".format(age+8))



#2.任务应用
meau={"番茄炒蛋":20}
try:
    price = int(price)
except  ValueError:
    print("输入类型错误")
else:
    meau["番茄炒蛋"]=price
    
