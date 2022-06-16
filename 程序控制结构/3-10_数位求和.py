print("请输入一个三位数：(100-999)")
f = eval(input("请输入一个数"))
num1 = f % 10
num4 = int(f/10)
num2 = num4 % 10
num3 = int(f/100)
total = num1+num2+num3
print("三位数之和为{}".format(total))
