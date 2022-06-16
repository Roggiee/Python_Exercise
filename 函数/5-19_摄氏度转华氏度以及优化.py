#
str=float(input("请输入摄氏度:"))
def cetofa(cetemp):
    return 32+1.8*cetemp
print("请输出华氏度:{}".format(cetofa(str)))


#优化版
str=float(input("请输入摄氏度:"))
def cetofa(cetemp):
    temper=cetemp[:-1]
    if cetemp[0:-1]=="F" or cetemp[0:-1]=="f":
        C=(eval(temper)-32)/1.8
        print(cetemp+"=",str(C)+"C")
    elif cetemp[0:1]=="C" or cetemp[0:1]=="c":
        F= eval(temper)*1.8+32
        print(cetemp+"=",str(F)+"F")
cetofa(str)