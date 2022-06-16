#方法二
def isNum(s):
    for i in s:
        if s.isalnum():
            continue
        else:
            return("{}不是数字".format(s))
    else:
        return("{}是数字".format(s))

print(isNum("2019"))
print(isNum("sz2019"))

#方法三
def isNum1(n):
    try:
        int(n)
    except:
        return "{}不是数字".format(n)
    return "{}是数字".format(n)

print(isNum1("2019"))
print(isNum1("sz2019"))