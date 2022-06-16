greet1 = 'Hello'
greet2 = 'john!'
# 合并字符串赋值给greet
greet = greet1 + ' ' + greet2
# 打印grrete的子字符串
print(greet[6:len(greet)])

myid = str(input("请输入身份证号码："))
# 打印出生日期
print("出生日期：" + myid[6:10] + "年" +
      int(myid[10:12]) + "月" + int(myid[12:14]) + "日")
