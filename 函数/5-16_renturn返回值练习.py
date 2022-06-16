#return返回一个值
def isNum(s):
    for i in s:
        if i in "1234567890":
            continue
        else:
            return("{}不是数字".format(s))
    else:
        return("{}是数字".format(s))
astr=isNum("2019")
bstr=isNum("sz2019")
print(astr)
print(bstr)

#return返回多个值
def rect(a,b):
    area=a*b
    perimeter=2*(a+b)
    return area,perimeter
s,p=rect(5,10)
print("面积",s)
print("周长",p)